from models.users import User
from sqlalchemy.orm import Session, joinedload
from schemas.users import UserSchema, UserCreate
from typing import Annotated
from fastapi import Depends
from schemas.users import scheme, decode_token


class DuplicateAccountError(ValueError):
    pass


# testing security
async def get_current(token: Annotated[str, Depends(scheme)]):
    user = decode_token(token)
    return user


def db_get_users(db: Session, skip: int = 0, limit: int = 100):
    users = (
        db.query(User)
        .options(joinedload(User.groups))
        .options(joinedload(User.authored_tasks))
        .options(joinedload(User.task_assignments))
        .offset(skip)
        .limit(limit)
        .all()
    )
    user_schemas = [UserSchema.from_orm(user) for user in users]
    return user_schemas


def db_check_email_and_username(db: Session, username: str, email: str):
    user_id_and_email = (
        db.query(User).where(User.username == username and User.email == email).all()
    )
    return user_id_and_email


def db_check_email_or_username(db: Session, username: str, email: str):
    user_id_or_email = db.query(User).where(
        User.username == username or User.email == email
    )
    return user_id_or_email


def db_get_user_by_id(
    db: Session,
    user_id: int,
):
    user_by_id = (
        db.query(User)
        .options(joinedload(User.groups))
        .where(User.id == user_id)
        .first()
    )
    return user_by_id


def db_get_user_by_username(
    db: Session,
    username: str,
):
    filtered_username = username.strip()
    user_username = (
        db.query(User)
        .filter(User.username.ilike(f"%{filtered_username}%"))
        .options(joinedload(User.groups))
        .first()
    )
    return user_username


def db_get_user_by_email(
    db: Session,
    email: str,
):
    user = (
        db.query(User)
        .options(joinedload(User.groups))
        .where(User.email == email)
        .first()
    )
    return user


# desire: attempt OAuth2 w/ password + hashing, bearer w/ JWT tokens
def db_create_user(db: Session, user: UserCreate):
    try:
        fake_hashed_password = hash(user.password)
        db_user = User(
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
    except:
        return {"message": "create did not work"}


"""
endpoint can only be performed by specific user from profile page
"""
# def db_update_user('/users/{user_id}')
# def db_update_user('/users/{username})

# protected endpoint
# def db_delete_user('/users/{user_id}')

"""
def db_get_user_notifications(
    db:Session,
    user_id: int,
):
"""
