from fastapi import Depends, HTTPException, APIRouter
from typing import List
from sqlalchemy.orm import Session
from queries.groups import (
    db_get_group_by_id,
    db_get_groups,
    db_get_group_by_name,
    GroupSchema,
)
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    tags=["groups"],
    responses={404: {"description": "Not Found"}},
)


@router.get("/groups", response_model=List[GroupSchema])
def get_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = db_get_groups(db, skip=skip, limit=limit)
    return groups


@router.get("/group_by_id/{group_id}", response_model=GroupSchema)
def get_group_by_id(group_id: int, db: Session = Depends(get_db)):
    group_by_id = db_get_group_by_id(db, group_id)
    if group_by_id is None:
        raise HTTPException(status_code=400, detail="group not found")
    return group_by_id


@router.get("/group_by_name/{groupname}", response_model=GroupSchema)
def get_group_by_name(groupname: str, db: Session = Depends(get_db)):
    group_by_name = db_get_group_by_name(db, groupname)
    if group_by_name is None:
        raise HTTPException(status_code=400, detail="user not found")
    return group_by_name
