from celery_app import celery_app
from datetime import datetime
import time


@celery_app.task
def process_numbers():
    results = []

    for number in range(1, 101):
        processed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Processing number: {number} | Time: {processed_at}")

        results.append({
            "number": number,
            "processed_at": processed_at
        })

        time.sleep(5)

    return results
