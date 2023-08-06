from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import joinedload


# To do change these to a tasks

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
