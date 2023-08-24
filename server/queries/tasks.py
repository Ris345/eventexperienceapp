from models.tasks import Task
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends


def db_get_tasks(db: Session, skip: int = 0, limit: int = 100):
    db_tasks = (
        db.query(Task)
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
        db.query(Task)

        .where(Task.id == task_id)
        .first()
    )
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

