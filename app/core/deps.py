
from typing import Generator, Annotated
from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.pq_db import SessionLocal

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session, Depends(get_db)]