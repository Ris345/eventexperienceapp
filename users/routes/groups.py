import schemas

from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    FastAPI,
)
from typing import List
from sqlalchemy.orm import Session
from queries.groups import db_get_group, db_get_groups
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/groups", response_model=List[schemas.GroupSchema])
def get_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = db_get_groups(db, skip=skip, limit=limit)
    return groups


@router.get("/groups/{group_id}", response_model=schemas.GroupSchema)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = db_get_group(db, group_id)
    print(group)
    if group is None:
        raise HTTPException(status_code=400, detail="group not found")
    return group
