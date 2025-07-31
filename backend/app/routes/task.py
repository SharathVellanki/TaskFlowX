from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.database import get_db
from app.schemas.task import TaskCreate, TaskOut
from app.services import task_service

router = APIRouter()

@router.post("/", response_model=TaskOut)
def create(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = task_service.create_task(task, db)
    return new_task

@router.get("/{task_id}", response_model=TaskOut)
def get(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/{task_id}/run")
def run_task(task_id: int):
    task_service.publish_task(task_id)
    return {"message": f"Task {task_id} published to queue"}
