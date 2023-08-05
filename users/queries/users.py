import models
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from schemas import UserSchema, UserCreate


def db_get_users(db: Session, skip: int = 0, limit: int = 100):
    users = (
        db.query(models.User)
        .options(joinedload(models.User.groups))
        .offset(skip)
        .limit(limit)
        .all()
    )
    user_schemas = [UserSchema.from_orm(user) for user in users]
    return user_schemas


def db_confirm_user(db: Session, username: str, email: str):
    user_id_and_email = (
        db.query(models.User)
        .where(models.User.username == username and models.User.email == email)
        .first()
    )
    return user_id_and_email


def db_get_user_by_id(
    db: Session,
    user_id: int,
):
    user_by_id = (
        db.query(models.User)
        .options(joinedload(models.User.groups))
        .where(models.User.id == user_id)
        .first()
    )
    return user_by_id


def db_get_user_by_username(
    db: Session,
    username: str,
):
    user_username = (
        db.query(models.User)
        .options(joinedload(models.User.groups))
        .where(models.User.username == username)
        .first()
    )
    return user_username


def db_get_user_by_email(
    db: Session,
    email: str,
):
    user = (
        db.query(models.User)
        .options(joinedload(models.User.groups))
        .where(models.User.email == email)
        .first()
    )
    return user


# attempted OAuth2 w/ password + hashing, bearer w/ JWT tokens
def db_create_user(db: Session, user: UserCreate):
    fake_hashed_password = hash(user.password)
    db_user = models.User(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        about=user.about,
        profile_photo=user.profile_photo,
        hashed_password=fake_hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
