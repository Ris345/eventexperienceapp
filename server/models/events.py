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
Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

class Event(Base):
  __tablename__= "events"
  id = Column(Integer, primary_key = True, index = True)
  properties_id = Column(Integer, ForeignKey("event_properties.id"))
  properties = relationship("EventProperties", back_populates = "event")
  rsvp = Column(Boolean, default = False)
  date_created = Column(DateTime, default = func.now())
  last_modified_time = Column(DateTime, default = func.now())


#
# event_id say #3
# user_id say #2

# need another table to join event participant id to a user?
# many to one?
