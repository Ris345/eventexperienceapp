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
    about: Text
    profile_photo: str

    # SQL Alchemy does not return dict, which pydantic expects by default. Config allows loading from standard orm parameters (attributes on object as opposed to a dict lookup)
    class Config:
        orm_mode = True
        from_attributes = True


# changed groupbase and group schema in order to incoporate owner data, so removed owner_id from groupbase and added an owner field for owner data in group schema
# groups already had an owner relation on its model
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

    class Config:
        orm_mode = True
        from_attributes = True


class UserCreate(UserBase):
    password: str


class TaskUser(UserBase):
    id: int
    is_active: bool


class UserSchema(UserBase):
    id: int
    is_active: bool
    created_at: datetime = None
    groups: Optional[List[GroupSchema]] = None

    class Config:
        orm_mode = True
        from_attributes = True


class GroupCreate(GroupBase):
    pass


class DuplicateAccountError(ValueError):
    pass
