from celery import Celery
from app.services.sentiment_analysis import analyze_sentiment

celery_app = Celery("tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

@celery_app.task
def process_sentiment(comment: str):
    return analyze_sentiment(comment)
