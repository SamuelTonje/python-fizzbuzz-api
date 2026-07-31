from sqlalchemy import text
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI

from app.core.settings import get_settings
from app.db.database import get_db

settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.app_version,)


@app.get("/health")
def health(db: Session = Depends(get_db)):
    return {"status": "ok"}

@app.get("/db")
def db_check(db: Session = Depends(get_db)):
    db.execute(text("select 1"))
    return {"database": "connected"}