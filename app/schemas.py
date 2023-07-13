from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional

"""
ModelBase - common attributes when creating or reading data

ModelCreate - inherit from BaseModel and include additional info for creation

Model - schemas used when reading data,w hen returning it from API
    - For User
"""


class GroupBase(BaseModel):
    pass


class Group(GroupBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    about: str
    profile_photo: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime = None
    groups: Optional[list[Group]]

    class Config:
        orm_mode = True


class GroupCreate(GroupBase):
    pass
