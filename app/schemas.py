from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import joinedload
from models import Group, User

"""
ModelBase - common attributes when creating or reading data

ModelCreate - inherit from BaseModel and include additional info for creation

ModelSchema - schemas used when reading data,w hen returning it from API
    - For User
"""


class UserBase(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: str
    about: str
    profile_photo: str

    # SQL Alchemy does not return dict, which pydantic expects by default. Config allows loading from standard orm parameters (attributes on object as opposed to a dict lookup)
    class Config:
        orm_mode = True


class GroupBase(BaseModel):
    id: int
    owner_id: int
    name: str
    description: str | None = None
    users: List[UserBase]

    class Config:
        orm_mode = True


class GroupSchema(GroupBase):
    users: Optional[List[UserBase]]

    class Config:
        orm_mode = True


class UserSchema(UserBase):
    is_active: bool
    created_at: datetime = None
    groups: Optional[List[GroupBase]]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class GroupCreate(GroupBase):
    pass
