from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List

from models.users import User

class EventPropertiesBase(BaseModel):
  eventName : str
  eventDate : datetime
  startTime : datetime
  endTime : datetime
  eventLocation : str
  participants : Optional[List[User]]
  organizer : Optional[User] = None
  class Config:
      orm_mode = True
      from_attributes = True

class EventBase(BaseModel):
  date_created : datetime
  last_modified_time : datetime
  rsvp : bool
  properties : EventPropertiesBase
  class Config:
    orm_mode = True
    from_attributes = True

class EventPropertiesSchema(EventPropertiesBase):
  id : int

class EventSchema(EventBase):
  id : int
