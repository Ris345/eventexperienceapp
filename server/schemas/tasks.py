from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List, Text

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
    about: str
    profile_photo: str

    class Config:
        orm_mode = True
        from_attributes = True


class GroupBase(BaseModel):
    name: str
    description: Optional[str] = None
    users: List[UserBase]

    class Config:
        orm_mode = True
        from_attributes = True


class GroupSchema(GroupBase):
    id: int
    users: Optional[List[UserBase]] = None
    owner: Optional[UserBase] = None


class TaskPriorityBase(BaseModel):
    name: str
    level: int


class TaskPriorityCreate(TaskPriorityBase):
    pass


class TaskPrioritySchema(TaskPriorityBase):
    id: int


class TaskTypeBase(BaseModel):
    name: str


class TaskTypeCreate(TaskTypeBase):
    pass


class TaskTypeSchema(TaskTypeBase):
    id: int


# we want author to get auto assigned to current user
class TaskBase(BaseModel):
    name: str
    description: str
    author: UserBase

    # assignedUser : int
    class Config:
        orm_mode = True
        from_attributes = True

    # SQL Alchemy does not return dict, which pydantic expects by default. Config allows loading from standard orm parameters (attributes on object as opposed to a dict lookup)


class TaskCreate(TaskBase):
    pass


class TaskSchema(TaskBase):
    id: int
    isCompleted: bool
    quantity: Optional[int] = None
    type: Optional[TaskTypeSchema] = None
    priority: Optional[TaskPrioritySchema] = None
    assignedUser: Optional[UserBase] = None

    class Config:
        orm_mode = True
        from_attributes = True


class TasklistBase(BaseModel):
    name: str
    owner: UserBase
    description: Text

    class Config:
        orm_mode = True
        from_attributes = True


class TaskListCreate(TasklistBase):
    pass


class TaskListSchema(TasklistBase):
    id: int
    isCompleted: bool
    priority: Optional[TaskPrioritySchema] = None
    assignedGroup: Optional[List[GroupSchema]] = None
