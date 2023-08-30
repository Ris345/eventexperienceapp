import models.users as user_m
from sqlalchemy.orm import Session, joinedload
from schemas.users import UserSchema, UserCreate


class DuplicateAccountError(ValueError):
    pass


def db_get_users(db: Session, skip: int = 0, limit: int = 100):
    users = (
        db.query(user_m.User)
        .options(joinedload(user_m.User.groups))
        .options(joinedload(user_m.User.authored_tasks))
        .options(joinedload(user_m.User.task_assignments))
        .offset(skip)
        .limit(limit)
        .all()
    )
    user_schemas = [UserSchema.from_orm(user) for user in users]
    return user_schemas


def db_check_email_and_username(db: Session, username: str, email: str):
    user_id_and_email = (
        db.query(user_m.User)
        .where(user_m.User.username == username and user_m.User.email == email)
        .all()
    )
    return user_id_and_email


def db_check_email_or_username(db: Session, username: str, email: str):
    user_id_or_email = db.query(user_m.User).where(
        user_m.User.username == username or user_m.User.email == email
    )
    return user_id_or_email


def db_get_user_by_id(
    db: Session,
    user_id: int,
):
    user_by_id = (
        db.query(user_m.User)
        .options(joinedload(user_m.User.groups))
        .where(user_m.User.id == user_id)
        .first()
    )
    return user_by_id


def db_get_user_by_username(
    db: Session,
    username: str,
):
    user_username = (
        db.query(user_m.User)
        .options(joinedload(user_m.User.groups))
        .where(user_m.User.username == username)
        .first()
    )
    return user_username


def db_get_user_by_email(
    db: Session,
    email: str,
):
    user = (
        db.query(user_m.User)
        .options(joinedload(user_m.User.groups))
        .where(user_m.User.email == email)
        .first()
    )
    return user


# desire: attempt OAuth2 w/ password + hashing, bearer w/ JWT tokens
def db_create_user(db: Session, user: UserCreate):
    try:
        fake_hashed_password = hash(user.password)
        db_user = user_m.User(
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
