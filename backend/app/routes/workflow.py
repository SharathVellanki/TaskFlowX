from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.database import get_db
from app.services import workflow_service
from app.schemas.workflow import WorkflowCreate, WorkflowOut

router = APIRouter()

@router.post("/", response_model=WorkflowOut)
def create(data: WorkflowCreate, db: Session = Depends(get_db)):
    return workflow_service.create_workflow(data, db)

@router.get("/{workflow_id}", response_model=WorkflowOut)
def get(workflow_id: int, db: Session = Depends(get_db)):
    wf = workflow_service.get_workflow(workflow_id, db)
    if not wf:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return wf

@router.post("/{workflow_id}/run")
def run_workflow(workflow_id: int, db: Session = Depends(get_db)):
    workflow = workflow_service.get_workflow(workflow_id, db)
    if not workflow or not workflow.steps:
        raise HTTPException(status_code=404, detail="Workflow or steps not found")

    first_step = sorted(workflow.steps, key=lambda s: s.step_order)[0]

    from app.services.task_service import publish_task
    publish_task(first_step.task_id)

    return {"message": f"Workflow {workflow_id} started with Task {first_step.task_id}"}
