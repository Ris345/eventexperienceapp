from Models import TasksModel
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends


def db_get_tasks(db: Session, skip: int = 0, limit: int = 100):
    db_tasks = (
        db.query(TasksModel.Task)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_tasks


def db_get_task(
    db: Session,
    task_id: int,
):
    db_task = (
        db.query(TasksModel.Task)
        # .options(joinedload(models.User.groups))
        .where(TasksModel.Task.id == task_id)
        .first()
    )
    return db_task

def db_post_tasks(task_name, quantity, db: Session):
    newTask = TasksModel.Task(
        task=task_name,
        quantity = quantity
    )
    db.add(newTask)
    db.commit()
    db_tasks = (
        db.query(TasksModel.Task)
        .where(TasksModel.Task.task == task_name)
        .all()
    )
    return db_tasks

