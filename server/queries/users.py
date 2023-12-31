from datetime import datetime, timedelta
from models.users import User
from sqlalchemy.orm import Session, joinedload
from schemas.users import UserSchema, UserCreate
from typing import Annotated
from fastapi import Depends, HTTPException, status, Security, FastAPI
from database import SessionLocal
from schemas.users import scheme
from jose import JWTError, jwt
from passlib.context import CryptContext
from typing import Optional
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import and_, func
from fastapi.security import SecurityScopes
from dependencies import SECURITY_KEY, ALGO

# temporary import for token model
from pydantic import BaseModel, ValidationError

# should move secret and algo to a .env later
SECRET = SECURITY_KEY
ALGORITHM = ALGO
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# putting it here for now
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str]
    scopes: list[str] = []


# init bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class DuplicateAccountError(ValueError):
    pass


def decode_token(db: Session, token):
    user_token = db_get_user_by_username(db=db, username=token)
    return user_token


# helper function to hash password
# ! no longer in use !
def fake_hash_password(password: str):
    return "fakehashed" + password


# helper function to verify db password with form data password
# received password  = hash stored
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# the real hashing helper function
def get_password_hash(password):
    return pwd_context.hash(password)


# creating access token, goes to another file?
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encoded_jwt


# to authenticate? don't know why this is needed yet
# authenticate and return user (need to know user exists and ensure received password matches hash stored)
def authenticate_user(username: str, password: str, db: Session = Depends(get_db)):
    user = db_get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


# testing security
async def get_current_user(
    security_scopes: SecurityScopes,
    token: Annotated[str, Depends(scheme)],
    db: Session = Depends(get_db),
):
    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = "Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception
    user = db_get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    for scope in security_scopes.scopes:
        if scope not in token_data.scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )
    return user


async def get_current_active_user(
    current_user: Annotated[User, Security(get_current_user, scopes=["me"])]
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


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
    try:
        username_and_email = (
            db.query(User)
            .options(joinedload(User.groups))
            .where(and_(User.username == username, User.email == email))
            .first()
        )
    except SQLAlchemyError as e:
        print(e)
    return username_and_email


def db_check_first_and_last(db: Session, first_name: str, last_name: str):
    try:
        first_and_last = (
            db.query(User)
            .options(joinedload(User.groups))
            .where(and_(User.first_name == first_name, User.last_name == last_name))
            .first()
        )
    except SQLAlchemyError as e:
        print(e)
    return first_and_last


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
    filtered_username = username.strip().lower()
    username = username.lower()
    user_username = (
        db.query(User)
        .filter(func.lower(User.username) == filtered_username)
        .options(joinedload(User.groups))
        .first()
    )
    print(user_username)
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
        hashed_password = get_password_hash(user.password)
        db_user = User(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            about=user.about,
            profile_photo=user.profile_photo,
            hashed_password=hashed_password,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except:
        return {"message": "create did not work"}


"""
def db_update_user(
    db: Session,
    user_to_update: UserCreate,
    update_data: dict
):
    filtered_username = username.strip()
    try:
        user_to_update = (
            db.query(User)
            .filter(User.username.ilike(f"%{filtered_username}%"))
            .options(joinedload(User.groups))
            .first()
        )
        if user_to_update:
            for field, value in update_data:
                setattr(user_to_update, field, value)
        db.commit()
        db.refresh()
    except SQLAlchemyError as e:
        print(f'found this error: {e}')
"""


"""
endpoint can only be performed by specific user from profile page
"""
# def db_update_user('/users/{user_id}')
# protected endpoint
# def db_delete_user('/users/{user_id}')

"""
def db_get_user_notifications(
    db:Session,
    user_id: int,
):
"""
pw = get_password_hash("aaa123")
