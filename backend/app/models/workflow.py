from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.services.database import Base

class Workflow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"))

    steps = relationship("WorkflowStep", back_populates="workflow", order_by="WorkflowStep.step_order")


class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey("workflows.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    step_order = Column(Integer)

    workflow = relationship("Workflow", back_populates="steps")
