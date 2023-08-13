from datetime import datetime
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


Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

"""
Calendar Model

Event Model

Location Model

for test db:
calendar | events
calendar1 | [event1, event2]
calendar2 | [event2, event3]
"""

"""
Events polled in from google calendar would resemble this model:

# via calendar_list_data.json in the data folder

class Calendar(Base):
    id = str
    kind = str
    etag = str
    htmlLink = str
    created = datetime
    updated = datetime
    timeZone = str
    access Role = str
    nextSyncToken = str
    items ('events') = [ ]

Going to test using jsonencooder 'ACL' in order to see if i can get events from json file to show up in current db sessions
"""


# This model is for events created through the app
class Calendar(Base):
    __tablename__ = "calendars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    summary = Column(Text)
    description = Column(Text)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.now())


"""
Calendar<->Events
multiple events to one calendar

Groups<->Events
multiple groups to one event
multiple events to one group
"""

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    summary = Column(Text)
    description = Column(Text)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.now())
    html_link=Column(String)
    event_calendar = relationship("Calendar", back_populates="events", lazy="joined")
    groups = relationship("Group", secondary="event_group", back_populates="events")
    author =
    organizer =
    start =
    end =
    duration =
    max_rsvps =
    attendees =
    type = relationship('EventType', back_populates='events', lazy='joined')
    attachment =

'''
one event has one type
'''
class EventType(Base):
    __tablename__ = 'event_type'
    id =
    name =



class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name =
    room_count =
    zip_code =
    created =
    photo_url =
