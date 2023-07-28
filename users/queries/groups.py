import models
from schemas import GroupSchema
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from typing import List


def db_get_groups(db: Session, skip: int = 0, limit: int = 100) -> List[GroupSchema]:
    db_groups = (
        db.query(models.Group)
        .options(joinedload(models.Group.users))
        .offset(skip)
        .limit(limit)
        .all()
    )
    group_schemas = [GroupSchema.from_orm(group) for group in db_groups]
    return group_schemas


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
