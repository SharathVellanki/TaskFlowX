from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.services.database import Base
import enum

class TaskStatus(str, enum.Enum):
    pending = "pending"
    running = "running"
    success = "success"
    fail = "fail"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(Enum(TaskStatus), default=TaskStatus.pending)
    action = Column(String)  # description of what to do
    next_task_id = Column(Integer, ForeignKey("tasks.id"), nullable=True)

    next_task = relationship("Task", remote_side=[id])
