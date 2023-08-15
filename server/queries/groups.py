import models.userGroups as models
from schemas.userGroups import GroupSchema
from sqlalchemy.orm import Session, joinedload
from fastapi import Depends
from typing import List


# now returns with owner data
"""
db = Session object via sqlalchemy
skip = number of records to skip when querying
list = integer max number of records to retrieve
points to List[GroupSchema] i.e return all json objects matching groupschema

query method creates query object from Group model. use options w/ joinedload to eager load users-Group model
Associated users fetched in single query

.from_orm using list comprehension iterate through instances of Group model and use .from_orm to map attribute from group model instance to fields of groupSchema

I am under the belief that this .from_orm takes advantage of orm_mode=True which allows pydantic to use the built in orm for attribute mapping
"""


def db_get_groups(db: Session, skip: int = 0, limit: int = 100) -> List[GroupSchema]:
    db_groups = (
        db.query(models.Group)
        .options(joinedload(models.Group.users))
        .offset(skip)
        .limit(limit)
        .all()
    )
    group_schemas = [GroupSchema.from_orm(group) for group in db_groups]
    return group_schemas


def db_get_group(
    db: Session,
    group_id: int,
):
    db_group = (
        db.query(models.Group)
        .options(joinedload(models.Group.users))
        .where(models.Group.id == group_id)
        .first()
    )
    return db_group


"""
potentially protected endpoints
(1) who can create new groups?
(2) who can update/delete groups?
"""

# def db_create_group

# def db_update_grouo
# def db_delete_group

"""
def db_get_group_notifications(
    db:Session,
    group_id: int,
):
"""
