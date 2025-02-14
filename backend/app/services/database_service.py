from sqlalchemy.orm import Session
from ..models.comment import Comment
from ..schemas.comment import CommentCreate
from ..services.sentiment_analysis import analyze_sentiment

def save_comment(db: Session, comment_data: CommentCreate):
    sentiment = analyze_sentiment(comment_data.comment)
    db_comment = Comment(comment=comment_data.comment, sentiment=sentiment)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_all_comments(db: Session):
    return db.query(Comment).all()
