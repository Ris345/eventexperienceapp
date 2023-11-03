from datetime import timedelta
from fastapi import (
    Depends,
    HTTPException,
    APIRouter,
)
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from queries.users import (
    authenticate_user,
    create_access_token,
)
from schemas.users import UserCreate
from typing import Annotated
from database import SessionLocal

ACCESS_TOKEN_EXPIRE_MINUTES = 30


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
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    user_obj = authenticate_user(
        db=db, username=form_data.username, password=form_data.password
    )
    if not user_obj:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserCreate(
        username=user_obj.username,
        first_name=user_obj.first_name,
        last_name=user_obj.last_name,
        email=user_obj.email,
        about=user_obj.about,
        profile_photo=user_obj.profile_photo,
        password=user_obj.hashed_password,
    )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token, "token_type": "bearer"}
