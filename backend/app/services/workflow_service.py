from sqlalchemy.orm import Session
from app.models.workflow import Workflow, WorkflowStep
from app.schemas.workflow import WorkflowCreate

def create_workflow(data: WorkflowCreate, db: Session):
    workflow = Workflow(name=data.name, created_by=data.created_by)
    db.add(workflow)
    db.commit()
    db.refresh(workflow)

    for step in data.steps:
        db.add(WorkflowStep(
            workflow_id=workflow.id,
            task_id=step.task_id,
            step_order=step.step_order
        ))

    db.commit()
    db.refresh(workflow)
    return workflow

def get_workflow(workflow_id: int, db: Session):
    return db.query(Workflow).filter(Workflow.id == workflow_id).first()
