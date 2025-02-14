from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..core.database import Base

class Comment(Base):
    __tablename__ = "sentiment_results"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String, nullable=False)
    sentiment = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
