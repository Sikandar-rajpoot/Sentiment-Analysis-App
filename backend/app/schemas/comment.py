from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
    comment: str

class CommentCreate(CommentBase):
    pass

class CommentResponse(CommentBase):
    id: int
    sentiment: str
    created_at: datetime

    class Config:
        from_attributes = True
