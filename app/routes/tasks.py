from queries import users
from Schema import TaskSchema
from queries.tasks import db_get_tasks, db_get_task
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
from typing import List
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/tasks", response_model=List[TaskSchema.TaskSchema])
def get_tasks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = db_get_tasks(db, skip=skip, limit=limit)
    return tasks


@router.get("/tasks/{task_id}", response_model=TaskSchema.TaskSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db_get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=400, detail="task not found")
    return task
