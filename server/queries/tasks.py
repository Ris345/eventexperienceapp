from models.tasks import Task
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from schemas.tasks import TaskSchema, TaskCreate


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
