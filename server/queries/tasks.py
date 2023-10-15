from models.tasks import Task, TaskList
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from schemas.tasks import TaskCreate, TaskListCreate, TaskSchema, TaskListSchema
from fastapi import HTTPException


# use joinedload in order to join other tables to Task model
def db_get_tasks(db: Session, skip: int = 0, limit: int = 100):
    tasks = (
        db.query(Task)
        .options(joinedload(Task.tasklist))
        .options(joinedload(Task.assignee))
        .options(joinedload(Task.task_type))
        .options(joinedload(Task.priority))
        .options(joinedload(Task.author))
        .offset(skip)
        .limit(limit)
        .all()
    )
    task_schemas = [TaskSchema.from_orm(task) for task in tasks]
    return task_schemas


def db_get_task_by_id(
    db: Session,
    task_id: int,
):
    db_task = db.query(Task).where(Task.id == task_id).first()
    return db_task


"""
using .ilike() function allowing for matching of strings via case insenstivitiy
and then wildcard allowing for matching of string regardless of characters
"""


def db_get_task_by_name(
    db: Session,
    taskname: str,
):
    filtered_taskname = taskname.strip()
    task_by_username = (
        db.query(Task).filter(Task.name.ilike(f"%{filtered_taskname}%")).first()
    )
    return task_by_username


def db_create_task(db: Session, task: TaskCreate):
    try:
        newTask = Task(name=task.name, description=task.description, author=task.author)
        db.add(newTask)
        db.commit()
        db.refresh(newTask)
        return newTask
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="could not create task") from e
        print(e)


def db_get_tasklists(db: Session, skip: int = 0, limit: int = 100):
    tasklists = db.query(TaskList).offset(skip).limit(limit).all()
    tasklist_schemas = [TaskListSchema.from_orm(task) for task in tasklists]
    return tasklist_schemas


def db_get_tasklist_by_name(
    db: Session,
    name: str,
):
    db_tasklist_by_name = db.query(TaskList).where(TaskList.name == name).first()
    return db_tasklist_by_name


def db_create_tasklist(db: Session, tasklist: TaskListCreate):
    try:
        newTasklist = TaskList(
            name=tasklist.name,
            owner=tasklist.owner,
            description=tasklist.description,
            priority=tasklist.priority,
            assignedGroup=tasklist.assignedGroup,
        )
        db.add(newTasklist)
        db.commit()
        db.refresh(newTasklist)
        return newTasklist
    except:
        {"alert": "could not create tasklist"}
