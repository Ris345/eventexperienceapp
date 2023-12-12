from datetime import date, datetime, time, timedelta
from pydantic import BaseModel
from typing import Optional, List

from schemas.users import UserSchema
# class UserBase(BaseModel):
#     username: str
#     first_name: str
#     last_name: str
#     email: str
#     about: str
#     profile_photo: str

#     # SQL Alchemy does not return dict, which pydantic expects by default. Config allows loading from standard orm parameters (attributes on object as opposed to a dict lookup)
#     class Config:
#         orm_mode = True
#         from_attributes = True


class EventPropertiesBase(BaseModel):
  eventName : str
  eventDate : datetime
  startTime : datetime
  endTime : datetime
  eventLocation : str
  participants : Optional[List[UserSchema]]
  organizer : Optional[UserSchema] = None
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
