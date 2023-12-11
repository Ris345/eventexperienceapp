from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    String,
    DateTime,
    Integer,
    Text,
    func,
)
from sqlalchemy.orm import relationship, joinedload
import database
from models.users import User
Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

class Event(Base):
  __tablename__= "events"
  id = Column(Integer, primary_key = True, index = True)
  properties_id = Column(Integer, ForeignKey("event_properties.id"))
  properties = relationship("EventProperties", back_populates = "events", foreign_keys = [properties_id])
  rsvp = Column(Boolean, default = False)
  date_created = Column(DateTime, default = func.now())
  last_modified_time = Column(DateTime, default = func.now())

class EventProperties(Base):
  __tablename__ = "event_properties"
  id = Column(Integer, primary_key = True, index = True)
  event_name = Column(String)
  event_date = Column(DateTime)
  start_time = Column(DateTime)
  end_time = Column(DateTime)
  event_location = Column(String)
  participants_id = Column(Integer, ForeignKey("event_particpants.id"))
  participants = relationship("EventParticipants",  back_populates = "event_properties")
  organizer_id = Column(Integer, ForeignKey = "user.id")
  organizer = relationship("User", back_populates = "event_properties")

# joining table for users with event?

class EventParticipants(Base):
  __tablename__ = "events_participants"
  id = Column(Integer, primary_key = True)
  event_properties_id = Column(Integer, ForeignKey("event_properties.id"))
  event_prop = relationship("EventProperties", back_populates = "event_participants")
#
# event_id say #3
# user_id say #2

# need another table to join event participant id to a user?
# many to one?
