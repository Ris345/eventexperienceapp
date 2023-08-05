
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from schemas import UserSchema, UserCreate
import models


def db_get_users(db: Session, skip: int = 0, limit: int = 100):
    users = (db.query(models.User)
        .options(joinedload(models.User.groups))
        .offset(skip)
        .limit(limit)
        .all()
    )
    # Azari - Changed from_orm to validate UserSchema.from_orm(user) -> UserSchema.model_validate(user)
    user_schemas = [UserSchema.model_validate(user) for user in users]
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
def db_create_user(
        db:Session,userInfo):
    
    ## this is really hashed now , python has a built in method for hashing 
    
    hashed_password = hash(user.password) 
    print(UserCreate)
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)


    User1 = User(
    username=user[username],
    first_name="first1",
    last_name="last1",
    email="user1@user.com",
    about="about user1",
    hashed_password="user1 password",
    profile_photo="aws3.privatebucket.com/user1_photo",
    is_active=True,
    )
    return db_user
    
    


