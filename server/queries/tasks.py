from models.tasks import Task, TaskProperties
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from fastapi import Depends
from schemas.tasks import TaskSchema, TaskCreate


# use joinedload in order to join other tables to Task model
def db_get_tasks(db: Session, skip: int = 0, limit: int = 100):
    tasks = (
        db.query(Task)
        # .options(joinedload(Task.tasklist))
        # .options(joinedload(Task.assignee))
        # .options(joinedload(Task.task_type))
        # .options(joinedload(Task.priority))
        .options(joinedload(Task.properties))
        # .options(joinedload(Task.author))
        .offset(skip)
        .limit(limit)
        .all()
    )
    # print(tasks[0])
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

def db_post_task_properties(task_prop_obj, db : Session):
    new_task_props = TaskProperties(
        description = task_prop_obj.description,
        quantity = task_prop_obj.quantity,
        # assignee_id = task_prop_obj.assignee_id,
    )
    db.add(new_task_props)
    db.commit()
    # unlike some other ORM, adding a new item to the db doesn't return anything to get the ide, we need to refresh the item and grab the id. Which is actually just short hand for querying the new item
    db.refresh(new_task_props)
    return new_task_props.id

def db_post_tasks(properties_id, db: Session):
    task = Task(
        properties_id = properties_id
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    # print(task.id)
    db_tasks = (
        db.query(Task)
        .where(Task.id == task.id)
        .first()
    )
    print(db_tasks)
    return db_tasks

def db_get_properties(properties_id, db:Session):
    task_prop = (
        db.query(TaskProperties)
        .where(TaskProperties.id == properties_id)
        .first())
    print(task_prop)
    return task_prop

def db_assign_user(task_id, user_id, db :Session):
    print("aaaaaaaaaaaaaaaaaa", user_id)
    task = db_get_task_by_id(db, task_id)
    task_prop = db_get_properties(task.properties.id, db)
    # task_prop.update({
    #     "assignee_id" : user_id
    # })
    task.last_modified_time= func.now()
    task_prop.assignee_id = user_id
    print(task_prop.assignee_id)
    db.commit()
    db.flush()


def db_delete_task(task_id, db : Session):
    # get task
    task = db_get_task_by_id(db,task_id)
    print("234564234655423564545623454562344556234",task.properties.id)
    # from the task, get prop id
    task_prop = db_get_properties(task.properties.id,db)
    # get task_prop from prop_id
    # delete task from task_id
    db.delete(task)
    db.delete(task_prop)
    db.commit()
    db.flush()
    # delete task_prop from prop_id

