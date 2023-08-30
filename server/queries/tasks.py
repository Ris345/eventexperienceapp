import models.tasks as task_m
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from schemas.tasks import TaskSchema, TaskCreate


def db_get_tasks(db: Session, skip: int = 0, limit: int = 100):
    tasks = (
        db.query(task_m.Task)
        .options(joinedload(task_m.Task.tasklist))
        .options(joinedload(task_m.Task.assignee))
        .options(joinedload(task_m.Task.task_type))
        .options(joinedload(task_m.Task.priority))
        .options(joinedload(task_m.Task.author))
        .offset(skip)
        .limit(limit)
        .all()
    )
    task_schemas = [TaskSchema.from_orm(task) for task in tasks]
    return task_schemas


def db_get_task(
    db: Session,
    task_id: int,
):
    db_task = db.query(Task).where(Task.id == task_id).first()
    return db_task


# def db_post_tasks(task_name, description, db: Session):
#     newTask = Task(
#         name=task_name,
#         description = description
#     )
#     db.add(newTask)
#     db.commit()
#     db_tasks = (
#         db.query(Task)
#         .where(Task.name == task_name)
#         .all()
#     )
#     return db_tasks
