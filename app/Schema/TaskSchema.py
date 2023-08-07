from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List
from sqlalchemy.orm import joinedload


# To do change these to a tasks

class TaskBase(BaseModel):
    id: int
    task: str
    quantity: int


    # SQL Alchemy does not return dict, which pydantic expects by default. Config allows loading from standard orm parameters (attributes on object as opposed to a dict lookup)
    class Config:
        orm_mode = True


class TaskSchema(TaskBase):

    created_at: datetime = None

    class Config:
        orm_mode = True
