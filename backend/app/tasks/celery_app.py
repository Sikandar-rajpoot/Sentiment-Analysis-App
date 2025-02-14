from celery import Celery

celery_app = Celery(
    "sentiment_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task
def analyze_comment(comment):
    from app.services.sentiment_analysis import analyze_sentiment
    return analyze_sentiment(comment)
