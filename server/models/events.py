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
from models.users import User, EventGroup, UserAuthoredEvents, RSVP, Favorite
from sqlalchemy.ext.hybrid import hybrid_property

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
    summary = Column(Text)
    description = Column(Text)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.now())
    events = relationship("Event", back_populates="calendars", lazy="joined")


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
    summary = Column(Text)
    description = Column(Text)
    created = Column(DateTime, default=func.now())
    updated = Column(DateTime, onupdate=func.now())
    html_link = Column(String)
    event_calendar = relationship("Calendar", back_populates="events", lazy="joined")
    groups = relationship("Group", secondary="event_group", back_populates="events")
    type = relationship("EventType", ForeignKey("event_type.id"))
    author = relationship(
        "User", secondary="user_authored_events", back_populates="authored_events"
    )
    organizers = relationship(
        "User", secondary="user_organized_events", back_populates="organized_events"
    )
    max_rsvps = Column(Integer)
    # attachments = Column(String) or relationship to Attachments Table?
    location = relationship("Location", secondary="locations", back_populates="events")
    start = Column(DateTime)
    duration = Column(Integer)

    # edited from suggestion
    # count number of attendees from the number of RSVPS to add to Event model
    """
    an example being there are 5 rsvp users to event 2, attendees = 5 on Events model
    """

    @hybrid_property
    def attendees(self) -> int:
        attendee_count = select(
            func.count(RSVP.id).where(
                and_(RSVP.event_id == self.id, RSVP.is_attending == True)
            )
        )
        return self.session.execute(attendee_count).scalar()

    """
    users are able to favorite an event to check on it later and not rsvp, an example being an admin that is working on the tasks for a given x event (functions like a bookmark)

    count the number of events that favorite a particular event
    """

    @hybrid_property
    def favorites(self) -> int:
        favorite_count = select(
            func.count(Favorite.id).where(Favorite.event_id == self.id)
        )
        return self.session.execute(favorite_count).scalar()

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
one event has one type
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


class Attachment(Base):
    __tablename__ = "attachments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    file_string = Column(String)
