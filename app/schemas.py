from datetime import date, datetime, time, timedelta
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    about: str
    profile_photo: str


class GroupBase(BaseModel):
    pass


class Group(GroupBase):
    pass


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime = None
    groups: list[Group]


class GroupCreate(GroupBase):
    pass
