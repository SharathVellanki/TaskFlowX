import redis
import json
import time
from sqlalchemy.orm import Session
from app.services.database import SessionLocal
from app.models.task import Task, TaskStatus
from app.models.workflow import WorkflowStep

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def publish_task(task_id: int):
    r.publish("task_queue", json.dumps({"task_id": task_id}))

def process_task(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return

    print(f"[WORKER] Running task: {task.id} - {task.name}")
    task.status = TaskStatus.running
    db.commit()

    time.sleep(2)  # Simulate task execution

    task.status = TaskStatus.success
    db.commit()
    print(f"[WORKER] Completed task: {task.id}")

    # 🔁 Step-based chaining
    current_step = db.query(WorkflowStep).filter(WorkflowStep.task_id == task.id).first()
    if current_step:
        workflow_id = current_step.workflow_id
        current_order = current_step.step_order

        next_step = (
            db.query(WorkflowStep)
            .filter(WorkflowStep.workflow_id == workflow_id)
            .filter(WorkflowStep.step_order == current_order + 1)
            .first()
        )

        if next_step:
            print(f"[CHAIN] Triggering next task in workflow: Task {next_step.task_id}")
            publish_task(next_step.task_id)

def start_worker():
    pubsub = r.pubsub()
    pubsub.subscribe("task_queue")
    print("[WORKER] Started. Listening for tasks...")

    for message in pubsub.listen():
        if message["type"] == "message":
            data = json.loads(message["data"])
            db = SessionLocal()
            try:
                process_task(data["task_id"], db)
            finally:
                db.close()

if __name__ == "__main__":
    start_worker()
