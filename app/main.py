import models, schemas, crud
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    FastAPI,
)
from typing import List, Optional, Union
from database import SessionLocal, engine
from sqlalchemy.orm import joinedload, Session

#  to get uvicorn to run, type in uvicorn main:app --reload in the command line, be sure to delete the sql_app.db and pycache
import crud


models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# router = APIRouter()
app = FastAPI()


@app.get("/users", response_model=List[schemas.UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    print(user)
    if user is None:
        raise HTTPException(status_code=400, detail="user not found")
    return user


@app.get("/groups", response_model=List[schemas.GroupSchema])
def get_groups(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    groups = crud.get_groups(db, skip=skip, limit=limit)
    return groups


@app.get("/groups/{group_id}", response_model=schemas.GroupSchema)
def get_group(group_id: int, db: Session = Depends(get_db)):
    group = crud.get_group(db, group_id)
    print(group)
    if group is None:
        raise HTTPException(status_code=400, detail="group not found")
    return group
