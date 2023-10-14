from schemas.tasks import TaskSchema
from queries.tasks import db_get_tasks, db_get_task_by_id, db_get_task_by_name
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    FastAPI,
)
from routes.users import get_user_by_username
from fastapi import Depends, HTTPException, APIRouter, Form, status, Request
from fastapi.exceptions import ResponseValidationError
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    tags=["tasks"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}},
)


# Validation error here for some reason after trying to display users
@router.get("/tasks", response_model=List[TaskSchema])
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = db_get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get("/task_by_id/{task_id}", response_model=TaskSchema)
def get_task_by_id(task_id: int, db: Session = Depends(get_db)):
    task_by_id = db_get_task_by_id(db, task_id)
    if task_by_id is None:
        raise HTTPException(status_code=400, detail="task not found with that id")
    return task_by_id


@router.get("/task_by_task_name/{task_name}", response_model=TaskSchema)
def get_task_by_taskname(taskname: str, db: Session = Depends(get_db)):
    task_by_username = db_get_task_by_name(db, taskname)
    if task_by_username is None:
        raise HTTPException(status_code=400, detail="task not found with that name")
    return task_by_username


# @router.post("/tasks/create", response_model=TaskBase)
# def post_task(task : TaskBase, db: Session = Depends(get_db)):
#     tasks = db_post_tasks(task.name, task.description, db)
#     if tasks is None:
#         raise HTTPException(status_code=400, detail="task not found")
#     return task
