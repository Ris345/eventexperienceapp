from queries.tasks import (
    db_get_tasks,
    db_get_task,
    db_create_tasklist,
    db_get_tasklists,
    db_get_task_by_name,
    db_get_tasklist_by_name,
    db_create_tasks,
    TaskCreate,
    TaskListCreate,
    TaskSchema,
    TaskListSchema,
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


router = APIRouter()


# Validation error here for some reason after trying to display users
@router.get("/tasks", response_model=List[TaskSchema])
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = db_get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get("/tasks/{task_id}", response_model=TaskSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db_get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=400, detail="task not found")
    return task


@router.post("/tasks", response_model=TaskSchema)
def post_task(
    name: str = Form(...),
    description: str = Form(...),
    author: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        print("attempt")
        existingTask = db_get_task_by_name(db, name=name)
        if existingTask is not None:
            raise HTTPException(status_code=400, detail="task found")
        user_author = get_user_by_username(username=author, db=db)
        print(user_author.username)
        task = TaskCreate(name=name, description=description, author=user_author)
        print(task)
        return db_create_tasks(db=db, task=task)
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(
            status_code=400, detail="Can not create a task with these details"
        ) from e


@router.get("/tasklists", response_model=TaskListSchema)
def get_tasklists(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasklists = db_get_tasklists(db, skip=skip, limit=limit)
    return tasklists


@router.post("/takslists", response_model=TaskListCreate)
def post_tasklist(
    name: str = Form(...),
    description: str = Form(...),
    owner: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        existingTasklist = db_get_tasklist_by_name(db, name=name)
        if existingTasklist is not None:
            raise HTTPException(status_code=400, detail="tasklist found")
        tasklist = TaskListCreate(name=name, description=description, owner=owner)
        return db_create_tasklist(db=db, tasklist=tasklist)
    except HTTPException:
        raise
    except ResponseValidationError as e:
        print(e)
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400, detail="can not create tasklist with these details"
        ) from e
