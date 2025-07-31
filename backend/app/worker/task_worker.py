import redis
import json
import time
from sqlalchemy.orm import Session
from app.services.database import SessionLocal
from app.models.task import Task, TaskStatus

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def process_task(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return
    print(f"Running task: {task.id} - {task.name}")
    task.status = TaskStatus.running
    db.commit()

    time.sleep(2)  # simulate work

    task.status = TaskStatus.success
    db.commit()
    print(f"Completed task: {task.id}")

    if task.next_task_id:
        print(f"Triggering next task: {task.next_task_id}")
        r.publish("task_queue", json.dumps({"task_id": task.next_task_id}))

def start_worker():
    pubsub = r.pubsub()
    pubsub.subscribe("task_queue")
    print("Worker started. Listening for tasks...")

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
