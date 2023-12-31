from schemas.tasks import TaskSchema, TaskBase,TaskPropertiesBase
from queries.tasks import db_get_tasks, db_get_task_by_id, db_get_task_by_name, db_post_tasks, db_post_task_properties, db_assign_user, db_delete_task
from queries.users import db_get_user_by_username
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    FastAPI,
    Form
)
from sqlalchemy.orm import Session
from sqlalchemy import func
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

@router.post("/tasks/create_prop", response_model = TaskPropertiesBase)
def create_task_properties(description: str = Form(...), quantity : int = Form(...), db :Session = Depends(get_db)):
    new_task_prop = TaskPropertiesBase(description = description, quantity = quantity)
    print(new_task_prop)
    db_post_task_properties(new_task_prop, db)
    return new_task_prop

@router.post("/tasks/create", response_model=TaskSchema)
def post_task(

    # should take a user name, which will call get_user_by_username to get id and use that as assignee
    # name : str = Form(...),
    description : str = Form(...),
    quantity : int = Form(...),
    assignee_username : str = Form(None),
    db: Session = Depends(get_db)
    ):
    new_task_prop = TaskPropertiesBase(description = description, quantity = quantity)
    new_task_prop_id = db_post_task_properties(new_task_prop, db)
    # it task has a json of all the stuff nested, so will probably just need to create the stuff and manually set it?
    # new_task = TaskBase(
    # isCompleted=False,
    # properties_id = new_task_prop_id
    # )
    tasks = db_post_tasks(new_task_prop_id, db)
    if tasks is None:
        raise HTTPException(status_code=400, detail="task not found")
    return tasks

# response_model = TaskSchema will need to put this in after
@router.put("/tasks/assign")
def assign_user(
    task_id : int = Form(...),
    username : str = Form(...),
    db: Session = Depends(get_db)
):
    # todo check task_id, if does not exist, return not found
    user = db_get_user_by_username(db, username)
    # todo if user does not exist, return user does not exist
    user_id = user.id
    print(task_id, username, user_id)
    db_assign_user(task_id, user_id, db)
    return {
        task_id,
        username,
        user_id
    }

@router.delete("/tasks/delete")
def delete_task(
    task_id : int = Form(...),
    db: Session = Depends(get_db)):
    db_delete_task(task_id, db)

    return {
        "testing"
    }
