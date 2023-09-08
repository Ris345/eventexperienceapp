from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    FastAPI,
)
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from queries.users import db_get_user_by_username, fake_hash_password
from schemas.users import UserCreate
from typing import Annotated
from database import SessionLocal
# from queries.token import get_token
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
router = APIRouter(
    tags=["token"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Invalid token"}},
)

@router.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)):
  # def get_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print(f"in function, ${form_data}")
    print(form_data.username)
    user_obj = db_get_user_by_username(db= db, username = form_data.username)
    if not user_obj:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    print("user print", user_obj.hashed_password)
    user = UserCreate(
            username=user_obj.username,
            first_name=user_obj.first_name,
            last_name=user_obj.last_name,
            email=user_obj.email,
            about=user_obj.about,
            profile_photo=user_obj.profile_photo,
            password=user_obj.hashed_password,)

    hashed_password = (form_data.password)
    print(hashed_password, "checking", user.password)
    if not hashed_password == user.password:
        print("not hased pass")
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

  # return get_token(form_data)