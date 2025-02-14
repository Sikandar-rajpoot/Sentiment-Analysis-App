from fastapi import FastAPI
from .api.v1.endpoints import comments, analysis
from .core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(comments.router, prefix="/comments", tags=["comments"])
app.include_router(analysis.router, prefix="/analysis", tags=["analysis"])
