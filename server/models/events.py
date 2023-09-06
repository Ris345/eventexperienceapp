from datetime import datetime, timedelta
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    String,
    DateTime,
    Integer,
    Text,
    func,
    select,
    and_,
)
from sqlalchemy.orm import relationship, joinedload
import database
from sqlalchemy.ext.hybrid import hybrid_property

# from models.users import User, RSVP, Bookmark

Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

"""
! subject to change !

Calendar Model

Event Model

Location Model

for test db:
calendar | events
calendar1 | [event1, event2]
calendar2 | [event2, event3]
"""

"""
! need to think about poller for google calendar date !

Calendar polled in from google calendar would resemble this model:
# via calendar_list_data.json in /data

class CalendarVO(Base):
    __tablename__ = 'events'
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

Going to test using jsonencooder in order to see if i can get events from json file to show up in current db sessions

Events polled in from google calendar would resemble this model:
# via calendar_event_data.json in /data

class EventVO(Base):
    __tablename__='event_vos'
    id = str
    kind = str
    etag = str
    status = str
    htmlLink = str
    created = datetime
    updated = datetime
    summary = text
    description = text
    creator (dict)
        email = str
    organizer (dict)
        email
        displayName
    start
        dateTime
        timeZone
    end
        dateTime
        timeZone
    icalUID
    attendees = []
    eventType = str
"""


# This model is for events created through the app
class Calendar(Base):
    __tablename__ = "calendars"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.now())
    events = relationship("Event", back_populates="calendar", lazy="joined")


class UserCalendar(Base):
    __tablename__ = "user_calendar"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.now())
    event_id = Column(Integer, ForeignKey("events.id"))
    events = relationship("Event", foreign_keys=[event_id], lazy="joined")
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="user_calendar", foreign_keys=[user_id])


"""
Calendar<->Events
multiple events to one calendar

Groups<->Events
multiple groups to one event
multiple events to one group
"""

"""
Based the event model on the returned json found in data/calendar_event_data.json

(attributes to be implemented)
class Event(Base):
    author - which is the foreign key relationship to the users table
        an event can only have one author which is a user, author is the event creator

    organizer which has a foreign key to the users table
        - im assuming that an organizer would be an individual with admin privileges that handles a different role vs author (! again i am basing it off the json i got back when using google calendar which u can view in the data folder !)

    start - datetime, start time of event

    duration - datetimedelta which is time quantity difference between start and end of event

    end - datetime, end time of event

    max_rsvps - max number of allowed rsvps, int

    attendees - number of users that are registered for event, type is list []
        - this will have to read from the rsvp table from users

    attachment - str, attachment for the event maybe like a pdf for flier

    location - foreign key to locations table
"""


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(Text)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.now())
    html_link = Column(String)
    event_calendar_id = Column(Integer, ForeignKey("calendars.id"))
    calendar = relationship(
        "Calendar", back_populates="events", foreign_keys=[event_calendar_id]
    )
    groups = relationship("Group", secondary="event_group", back_populates="events")
    type_id = Column(Integer, ForeignKey("event_type.id"))
    type = relationship("EventType", foreign_keys=[type_id])
    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", foreign_keys=[author_id])
    organizers = relationship(
        "User", secondary="user_organized_events", back_populates="organized_events"
    )
    max_rsvps = Column(Integer)
    attachments = relationship("Attachment", back_populates="events")
    location_id = Column(Integer, ForeignKey("locations.id"))
    location = relationship("Location", back_populates="events")
    start = Column(DateTime)
    duration = Column(Integer)
    rsvps = relationship("RSVP", back_populates="event")
    bookmark_id = Column(Integer, ForeignKey("bookmarks.id"))
    bookmarks = relationship(
        "Bookmark", back_populates="event", foreign_keys=[bookmark_id]
    )
    tasklist_id = Column(Integer, ForeignKey("tasklist.id"))
    tasklist = relationship(
        "TaskList", back_populates="events", foreign_keys=[tasklist_id]
    )
    # user_calendars = relationship(
    #     "UserCalendar",
    #     foreign_keys="[UserCalendar.event_id]",
    #     secondary="rsvps",
    #     back_populates="events",
    # )
    """
    users are able to favorite an event to check on it later and not rsvp, an example being an admin that is working on the tasks for a given x event (functions like a bookmark)

    count the number of events that favorite a particular event
    """

    @property
    def end(self) -> datetime:
        if self.start:
            if self.duration < 60:
                return self.start + timedelta(minutes=self.duration)
            if self.duration >= 60:
                hours = self.duration // 60
                minutes = self.duration - (hours * 60)
                return self.start + timedelta(hours=hours, minutes=minutes)
        return None

    """
    user_calendars = relationship(
        "UserCalendar",
        secondary="rsvps",
        primaryjoin="and_(Event.id == RSVP.event_id, RSVP.is_attending == True)",
        secondaryjoin="RSVP.user_calendar_id == UserCalendar.id",
        back_populates="events",
    )
    """


class EventType(Base):
    __tablename__ = "event_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)


"""
For locations

(attributes)
class Location(Base):
    name - type str
    room_count - type int, will be optional in the pedantic model i.e schema
    zip_code (or some sort of real location identifier)
    created - datetime, func.now()
    photo_url - url, s3 blob store

class Attachments(Base):
    id
    name
    file_string
"""


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    room_count = Column(Integer)
    zip_code = Column(Integer)
    created = Column(DateTime, default=func.now())
    photo_url = Column(String)
    events = relationship("Event", back_populates="location")


class Attachment(Base):
    __tablename__ = "attachments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    file_string = Column(String)
    event_id = Column(Integer, ForeignKey("events.id"))
    events = relationship("Event", foreign_keys=[event_id])
