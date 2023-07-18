import models, schemas
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends


# def get_db():
#     db = Session(bind=engine)
#     try:
#         yield db
#     finally:
#         db.close()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    db_users = (
        db.query(models.User)
        .options(joinedload(models.User.groups))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_users


def get_user(
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


def get_groups(db: Session, skip: int = 0, limit: int = 100):
    db_groups = (
        db.query(models.Group)
        .options(joinedload(models.Group.users))
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_groups


def get_group(
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
