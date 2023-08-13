import models
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends


def db_get_users(db: Session, skip: int = 0, limit: int = 100):
    db_users = (
        db.query(models.User)
        .options(joinedload(models.User.groups))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_users


def db_get_user(
    db: Session,
    user_id: int,
):
    db_user = (
        db.query(models.User)
        .options(joinedload(models.User.groups))
        .where(models.User.id == user_id)
        .first()
    )
    return db_user
