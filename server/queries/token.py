from typing import Annotated
from schemas.users import UserCreate
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from queries.users import db_get_user_by_username, fake_hash_password



def get_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    print(f"in function, $form_data")
    user_obj = db_get_user_by_username(form_data.username)
    if not user_obj:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    user = UserCreate(**user_obj)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}
