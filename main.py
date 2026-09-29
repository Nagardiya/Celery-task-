
from task import process_numbers
def start_task():
    task = process_numbers.delay()

    return {
        "message": "Task started successfully",
        "task_id": task.id
    }
start_task()
