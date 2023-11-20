from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List

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

    # SQL Alchemy does not return dict, which pydantic expects by default. Config allows loading from standard orm parameters (attributes on object as opposed to a dict lookup)
    class Config:
        orm_mode = True
        from_attributes = True


class TaskPriorityBase(BaseModel):
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class TaskPriority(TaskPriorityBase):
    id: int


class TaskTypeBase(BaseModel):
    name: str

    class Config:
        orm_mode = True
        from_attributes = True


class TaskType(TaskTypeBase):
    id: int

class TaskPropertiesBase(BaseModel):
    description : str
    quantity : int


    class Config:
        orm_mode = True
        from_attributes = True

class TaskProperties(TaskPropertiesBase):
    id : int
    assignee: Optional[UserBase] = None

class TaskBase(BaseModel):
    # name: str
    # description: str
    isCompleted: bool
    # priority: TaskPriority
    properties : TaskProperties
    # task_type: TaskType

    class Config:
        orm_mode = True
        from_attributes = True


class TaskCreate(TaskBase):
    pass


class TaskSchema(TaskBase):
    id: int
    date_created : datetime
    last_modified_time : datetime
    # assignee: Optional[UserBase]
    # author: Optional[UserBase]

    class Config:
        orm_mode = True
        from_attributes = True


class TasklistBase(BaseModel):
    pass


# changed groupbase and group schema in order to incoporate owner data, so removed owner_id from groupbase and added an owner field for owner data in group schema
# groups already had an owner relation on its model
# class GroupBase(BaseModel):
#     id: int
#     name: str
#     description: str | None = None
#     users: List[UserBase]

#     class Config:
#         orm_mode = True
#         from_attributes = True


# class GroupSchema(GroupBase):
#     users: Optional[List[UserBase]]
#     owner: Optional[UserBase]

#     class Config:
#         orm_mode = True
#         from_attributes = True


# class UserCreate(UserBase):
#     password: str


# class UserBase(UserBase):
#     id: int
#     is_active: bool
#     created_at: datetime = None
#     groups: Optional[List[GroupSchema]]

#     class Config:
#         orm_mode = True
#         from_attributes = True


# class GroupCreate(GroupBase):
#     pass


# class DuplicateAccountError(ValueError):
#     pass
