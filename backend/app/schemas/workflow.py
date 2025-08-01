from pydantic import BaseModel
from typing import List

class StepCreate(BaseModel):
    task_id: int
    step_order: int

class WorkflowCreate(BaseModel):
    name: str
    created_by: int
    steps: List[StepCreate]

class StepOut(BaseModel):
    id: int
    task_id: int
    step_order: int

    class Config:
        orm_mode = True

class WorkflowOut(BaseModel):
    id: int
    name: str
    steps: List[StepOut]

    class Config:
        orm_mode = True
