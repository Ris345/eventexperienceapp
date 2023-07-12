from datetime import date, datetime, time, timedelta
from pydantic import BaseModel


class Group(GroupBase):
    pass


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    about: str
    profile_photo: str
    groups: list[Group]


class GroupBase(BaseModel):
    pass


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    created_at: datetime = None
    groups: list[Group]


class GroupCreate(GroupBase):
    pass
