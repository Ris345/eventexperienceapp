# from datetime import datetime, timedelta
# from sqlalchemy import (
#     Boolean,
#     Column,
#     ForeignKey,
#     String,
#     DateTime,
#     Integer,
#     Text,
#     func,
# )
# from sqlalchemy.orm import relationship, joinedload
# import database


# Base = database.Base
# engine = database.engine
# SessionLocal = database.SessionLocal

# """
# ! subject to change !

# Calendar Model

# Event Model

# Location Model

# for test db:
# calendar | events
# calendar1 | [event1, event2]
# calendar2 | [event2, event3]
# """

# """
# ! need to think about poller for google calendar date !

# Calendar polled in from google calendar would resemble this model:
# # via calendar_list_data.json in /data

# class CalendarVO(Base):
#     id = str
#     kind = str
#     etag = str
#     htmlLink = str
#     created = datetime
#     updated = datetime
#     timeZone = str
#     access Role = str
#     nextSyncToken = str
#     items ('events') = [ ]

# Going to test using jsonencooder in order to see if i can get events from json file to show up in current db sessions

# Events polled in from google calendar would resemble this model:
# # via calendar_event_data.json in /data

# class EventVO(Base):
#     id = str
#     kind = str
#     etag = str
#     status = str
#     htmlLink = str
#     created = datetime
#     updated = datetime
#     summary = text
#     description = text
#     creator (dict)
#         email = str
#     organizer (dict)
#         email
#         displayName
#     start
#         dateTime
#         timeZone
#     end
#         dateTime
#         timeZone
#     icalUID
#     attendees = []
#     eventType = str
# """


# # This model is for events created through the app
# class Calendar(Base):
#     __tablename__ = "calendars"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     summary = Column(Text)
#     description = Column(Text)
#     created = Column(DateTime, default=func.now())
#     updated = Column(DateTime, onupdate=func.now())


# """
# Calendar<->Events
# multiple events to one calendar

# Groups<->Events
# multiple groups to one event
# multiple events to one group
# """

# """
# Based the event model on the returned json found in data/calendar_event_data.json

# (attributes to be implemented)
# class Event(Base):
#     author - which is the foreign key relationship to the users table
#         an event can only have one author which is a user, author is the event creator

#     organizer which has a foreign key to the users table
#         - im assuming that an organizer would be an individual with admin privileges that handles a different role vs author (! again i am basing it off the json i got back when using google calendar which u can view in the data folder !)

#     start - datetime, start time of event

#     duration - datetimedelta which is time quantity difference between start and end of event

#     end - datetime, end time of event

#     max_rsvps - max number of allowed rsvps, int

#     attendees - number of users that are registered for event, type is list []
#         - this will have to read from the rsvp table from users

#     attachment - str, attachment for the event maybe like a pdf for flier

#     location - foreign key to locations table
# """


# class Event(Base):
#     __tablename__ = "events"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, unique=True, index=True)
#     summary = Column(Text)
#     description = Column(Text)
#     created = Column(DateTime, default=func.now())
#     updated = Column(DateTime, onupdate=func.now())
#     html_link = Column(String)
#     event_calendar = relationship("Calendar", back_populates="events", lazy="joined")
#     groups = relationship("Group", secondary="event_group", back_populates="events")
#     type = relationship("EventType", ForeignKey("event_type.id"))
#     # author =
#     # organizer =
#     # start =
#     # end =
#     # duration =
#     # max_rsvps =
#     # attendees =
#     # attachment
#     # location =


# """
# one event has one type
# class EventType(Base):
#     __tablename__ = 'event_type'

#     this should have id, name
#     id is primary key, integer
# """

# """
# For locations

# (attributes)
# class Location(Base):
#     name - type str
#     room_count - type int, will be optional in the pedantic model i.e schema
#     zip_code (or some sort of real location identifier)
#     created - datetime, func.now()
#     photo_url - url, s3 blob store
# """


# class Location(Base):
#     __tablename__ = "locations"
#     id = Column(Integer, primary_key=True, index=True)
