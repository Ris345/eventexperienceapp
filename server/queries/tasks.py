from models.tasks import Task
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from schemas.tasks import TaskSchema, TaskCreate


# use joinedload in order to join other tables to Task model
def db_get_tasks(db: Session, skip: int = 0, limit: int = 100):
    tasks = (
        db.query(Task)
        .options(joinedload(Task.tasklist))
        .options(joinedload(Task.assignee))
        .options(joinedload(Task.task_type))
        .options(joinedload(Task.priority))
        .options(joinedload(Task.properties))
        .options(joinedload(Task.author))
        .offset(skip)
        .limit(limit)
        .all()
    )
    print("1111111111111111111111111111111111111111111111111111")
    print(tasks[0])
    task_schemas = [TaskSchema.from_orm(task) for task in tasks]
    return task_schemas


def db_get_task_by_id(
    db: Session,
    task_id: int,
):
    task_by_id = db.query(Task).where(Task.id == task_id).first()
    return task_by_id


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
