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
import database
from models.users import User
from models.events import Event
Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

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
# yes, will need a join table
EventsUserTable = Table(
  "eventsuser",
  Base.metadata,
  Column("events_id", ForeignKey("events_participants.id")),
  Column("users.id", ForeignKey("users.id"))
)

class EventParticipants(Base):
  __tablename__ = "events_participants"
  id = Column(Integer, primary_key = True)
  event_properties_id = Column(Integer, ForeignKey("event_properties.id"))
  event_prop = relationship("EventProperties", back_populates = "event_participants")
  participants = relationship("User", secondary = EventsUserTable, back_populates = "events_participants")
