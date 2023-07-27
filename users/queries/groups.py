import models
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends


def db_get_groups(db: Session, skip: int = 0, limit: int = 100):
    db_groups = (
        db.query(models.Group)
        .options(joinedload(models.Group.users))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_groups


def db_get_group(
    db: Session,
    group_id: int,
):
    db_group = (
        db.query(models.Group)
        .options(joinedload(models.Group.users))
        .where(models.Group.id == group_id)
        .first()
    )
    return db_group
