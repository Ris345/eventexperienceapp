from datetime import date, datetime, time, timedelta
from typing import Annotated
from fastapi import Depends
from pydantic import BaseModel
from typing import Optional, List
from schemas.tasks import TaskPriority, TaskType
import dependencies

scheme = dependencies.ouath2_scheme

"""
ModelBase - common attributes when creating or reading data

ModelCreate - inherit from BaseModel and include additional info for creation

ModelSchema - schemas used when reading data, when returning it from API
"""


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    about: Optional[str] = None
    profile_photo: Optional[str] = None

    # SQL Alchemy does not return dict, which pydantic expects by default. Config allows loading from standard orm parameters (attributes on object as opposed to a dict lookup)
    class Config:
        orm_mode = True
        from_attributes = True


class TaskBase(BaseModel):
    name: str
    description: str
    isCompleted: bool
    priority: TaskPriority
    task_type: TaskType

    # assignedUser : int
    class Config:
        orm_mode = True
        from_attributes = True


# changed groupbase and group schema in order to incoporate owner data, so removed owner_id from groupbase and added an owner field for owner data in group schema
# groups already had an owner relation on its model
class GroupBase(BaseModel):
    id: int
    name: str
    description: Optional[str]
    users: List[UserBase]

    class Config:
        orm_mode = True
        from_attributes = True


class GroupSchema(GroupBase):
    id: int
    users: Optional[List[UserBase]]
    owner: Optional[UserBase]

    class Config:
        orm_mode = True
        from_attributes = True


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: Optional[int] = None
    is_active: Optional[bool] = None
    created_at: datetime = None
    groups: Optional[List[GroupSchema]] = None
    task_assignments: Optional[List[TaskBase]] = None
    authored_tasks: Optional[List[TaskBase]] = None

    class Config:
        orm_mode = True
        from_attributes = True


class GroupCreate(GroupBase):
    pass


class DuplicateAccountError(ValueError):
    pass
