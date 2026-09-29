from celery import Celery

celery_app = Celery(
    "number_processor",
    broker="redis://localhost:6380/0",
    backend="redis://localhost:6380/0",
)
