from datetime import datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List, Text


class CalendarBase(BaseModel):
    pass


class EventBase(BaseModel):
    name: str
    description: Text
    created: datetime
    updated: datetime
    html_link: str


class EventSchema(EventBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True


"""
class EventVOCreate(EventBase):
    pass
"""
