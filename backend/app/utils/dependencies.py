from sqlalchemy.orm import Session
from app.core.database import SessionLocal

# Dependency to get a database session
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
