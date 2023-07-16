from . import models, schemas
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from typing import List, Optional, Union
from database import engine, SessionLocal
from sqlalchemy.orm import joinedload


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/users", response_model=List[schemas.UserSchema])
def get_users(db: SessionLocal = Depends(get_db)):
    db_users = db.query(models.User).options(joinedload(models.User.groups)).all()
    return db_users


@router.get("/users/{user_id}", response_model=schemas.UserSchema)
def get_user(id: int, db: SessionLocal = Depends(get_db)):
    db_user: db.query(models.User).options(joinedload(models.User.groups)).where(
        models.User.id == id
    ).one()
    return db_user


@router.get("/groups", response_model=List[schemas.GroupSchema])
def get_groups(db: SessionLocal = Depends(get_db)):
    db_groups = db.query(models.Group).options(joinedload(models.Group.users)).all()
    return db_groups


@router.get("/groups/{group_id}", response_model=schemas.GroupSchema)
def get_group(id: int, db: SessionLocal = Depends(get_db)):
    db_group = (
        db.query(models.Group)
        .option(joinedload(models.Group.users))
        .where(models.Group.id == id)
        .one()
    )
    return db_group
