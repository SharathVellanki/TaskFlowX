from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    pending = "pending"
    running = "running"
    success = "success"
    fail = "fail"

class TaskCreate(BaseModel):
    name: str
    action: str
    next_task_id: Optional[int] = None

class TaskOut(BaseModel):
    id: int
    name: str
    status: TaskStatus
    action: str
    next_task_id: Optional[int]

    class Config:
        orm_mode = True
