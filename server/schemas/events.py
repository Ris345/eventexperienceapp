from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List, Text


class EventBase(BaseModel):
    id: int
    # other common fields


class EventCreate(BaseModel):
    pass


"""
class EventVOCreate(EventBase):
    pass
"""
