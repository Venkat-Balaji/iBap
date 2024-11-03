# backend/app.py

from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import time

app = FastAPI()

# Task Automation Example
class TaskRequest(BaseModel):
    task_name: str
    task_data: dict

# Function for background processing (can be a Celery task)
def perform_task(task_name, task_data):
    time.sleep(5)  # Simulate processing time
    print(f"Task '{task_name}' completed with data: {task_data}")

@app.post("/run-task/")
async def run_task(task: TaskRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(perform_task, task.task_name, task.task_data)
    return {"status": "Task is being processed in the background"}
