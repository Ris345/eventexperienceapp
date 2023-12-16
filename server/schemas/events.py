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

class EventParticipantsBase(BaseModel):
  participants : Optional[List[UserSchema]] = None
  # id : int
  class Config:
    orm_mode = True
    from_attributes = True


class EventParticipantsSchema(EventParticipantsBase):
  id: int
  # pass

class EventPropertiesBase(BaseModel):
  event_name : str
  event_date : datetime
  start_time : datetime
  end_time : datetime
  event_location : str
  # event_participants : object
  event_participants : Optional[EventParticipantsSchema] = None
  # organizer : Optional[UserSchema] = None
  class Config:
      orm_mode = True
      from_attributes = True

class EventPropertiesSchema(EventPropertiesBase):
  id : int

class EventBase(BaseModel):
  date_created : datetime
  last_modified_time : datetime
  rsvp : bool
  properties : Optional[EventPropertiesSchema] = None
  class Config:
    orm_mode = True
    from_attributes = True

class EventSchema(EventBase):
  id : int
