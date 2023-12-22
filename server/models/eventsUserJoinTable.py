from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    String,
    DateTime,
    Integer,
    Text,
    func,
    Table
)
from sqlalchemy.orm import relationship, joinedload
from datetime import datetime, timedelta
import database

# from models.events import Event
Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

EventsOrganizerTable = Table(
  "eventsorganizer",
  Base.metadata,
  Column("events_id", ForeignKey("event_properties.id"), primary_key = True),
  Column("organizer_id", ForeignKey("users.id"), primary_key = True)
)

class EventProperties(Base):
  __tablename__ = "event_properties"
  id = Column(Integer, primary_key = True, index = True)
  event_name = Column(String)
  event_date = Column(DateTime)
  start_time = Column(DateTime)
  end_time = Column(DateTime)
  event_location = Column(String)
  # event_id = Column(Integer, ForeignKey("events.id"))
  event = relationship("Event",  back_populates = "properties")
  # event_participants_id = Column(Integer, ForeignKey("events_participants.id"))
  event_participants = relationship("EventParticipants",back_populates = "event_properties", uselist = False)
  # organizer_id = Column(Integer, ForeignKey("user.id"))
  organizer = relationship("User", secondary = EventsOrganizerTable,  back_populates = "event_organizee")

# joining table for users with event?
# yes, will need a join table
EventsUserTable = Table(
  "eventsuser",
  Base.metadata,
  Column("events_id", ForeignKey("events_participants.id"), primary_key = True),
  Column("users_id", ForeignKey("users.id"), primary_key = True)
)

# from models.users import User
class EventParticipants(Base):
  __tablename__ = "events_participants"
  id = Column(Integer, primary_key = True)
  event_properties_id = Column(Integer, ForeignKey("event_properties.id"))
  event_properties = relationship("EventProperties", back_populates = "event_participants")
  participants = relationship("User", secondary = EventsUserTable, back_populates = "events_participants")

#  need to add event_description as well 




# evt1 = Event()
# evtProp = EventProperties(
#   event_name = "event1",
#   event_date = datetime.now(),
#   start_time = datetime.now() + timedelta(hours=2),
#   end_time = datetime.now + timedelta(hours=5, minutes=30),
#   event_location = "location1"
# )
# evtParts = EventParticipants(

# )
# Base.metadata.create_all(engine)
