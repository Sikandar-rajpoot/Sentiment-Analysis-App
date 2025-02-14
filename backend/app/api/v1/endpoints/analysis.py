from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.database_service import get_all_comments
from app.utils.dependencies import get_db

router = APIRouter()

@router.get("/")
def analyze_sentiments(db: Session = Depends(get_db)):
    comments = get_all_comments(db)
    sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for comment in comments:
        sentiments[comment.sentiment] += 1

    return sentiments
