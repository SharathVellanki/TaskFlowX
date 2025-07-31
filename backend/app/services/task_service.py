from sqlalchemy.orm import Session
from app.models.task import Task, TaskStatus
from app.schemas.task import TaskCreate
import redis
import json

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def create_task(task_data: TaskCreate, db: Session):
    new_task = Task(**task_data.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_task(task_id: int, db: Session):
    return db.query(Task).filter(Task.id == task_id).first()

def publish_task(task_id: int):
    r.publish("task_queue", json.dumps({"task_id": task_id}))
