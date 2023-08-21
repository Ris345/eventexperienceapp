from models.tasks import Task, TaskList
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from schemas.tasks import TaskCreate, TaskListCreate, TaskSchema, TaskListSchema


def db_get_tasks(db: Session, skip: int = 0, limit: int = 100):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    task_schemas = [TaskSchema.from_orm(task) for task in tasks]
    return task_schemas


def db_get_task(
    db: Session,
    task_id: int,
):
    db_task = db.query(Task).where(Task.id == task_id).first()
    return db_task


def db_get_task_by_name(
    db: Session,
    name: str,
):
    db_task_by_name = db.query(Task).where(Task.name == name).first()
    return db_task_by_name


def db_create_tasks(db: Session, task: TaskCreate):
    try:
        newTask = Task(name=task.name, description=task.description, author=task.author)
        db.add(newTask)
        db.commit()
        db.refresh(newTask)
        return newTask
    except:
        {"alert": "could not create task"}


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
