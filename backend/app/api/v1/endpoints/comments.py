from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.comment import CommentCreate, CommentResponse
from app.services.database_service import save_comment, get_all_comments
from app.utils.dependencies import get_db

router = APIRouter()

@router.post("/", response_model=CommentResponse)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return save_comment(db, comment)

@router.get("/", response_model=list[CommentResponse])
def fetch_comments(db: Session = Depends(get_db)):
    return get_all_comments(db)
