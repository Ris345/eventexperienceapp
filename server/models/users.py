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
from models.tasks import Task, TaskList, TaskType
from models.events import Event, Location, EventType, Calendar, UserCalendar

Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

"""
for test db:
username | password | role
user1   | secret1 | admin
user2 | secret2 | organizer
user3 | secret3 | volunteer
"""

# Creating classes that inherit from Base
"""
 User Model that contains the attributes of id, username, ..., profile_photo to be a url coming from an s3 storage bucket, many to many relationship with groups meaning that there can be many users in one group, many groups assigned to one user
 """


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    about = Column(Text)
    hashed_password = Column(String)
    profile_photo = Column(String)
    created_at = Column(DateTime, default=func.now())
    # M2M
    groups = relationship("Group", secondary="group_users", back_populates="users")
    is_active = Column(Boolean, default=True)
    authored_tasks = relationship(
        "Task", back_populates="author", foreign_keys="[Task.author_id]"
    )
    task_assignments = relationship("Task", foreign_keys="[Task.assignee_id]")
    """
    authored_vo_events - possible parameter for events imported through gc api
    """
    authored_events = relationship("Event", back_populates="author")
    organized_events = relationship(
        "Event", secondary="user_organized_events", back_populates="organizers"
    )
    # if user is deleted, we want rsvps and bookmarks as well as user calendar to be deleted
    rsvps = relationship("RSVP", back_populates="user", cascade="all, delete-orphan")
    bookmarks = relationship(
        "Bookmark", back_populates="user", cascade="all, delete-orphan"
    )
    user_calendar = relationship(
        "UserCalendar",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    owned_groups = relationship("Group", back_populates="owner")


"""
Favorites Model
many bookmarks to one event, 1 bookmark ties to one event fk to events

RSVP Model
many rsvps to one event, fk to events, 1 rsvp ties to one event
"""


class Bookmark(Base):
    __tablename__ = "bookmarks"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    event = relationship("Event", back_populates="bookmarks")
    user = relationship("User", foreign_keys=[user_id])


class RSVP(Base):
    __tablename__ = "rsvps"
    id = Column(Integer, primary_key=True, index=True)
    is_attending = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="rsvps", foreign_keys=[user_id])
    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="rsvps", foreign_keys=[event_id])


"""
tbd - [ many to one relationships ] [x - solved]
(user assignments)
we want 1 user assigned per task, 1 user can be assigned to many tasks

(task authors)
we want a user to be an author of multiple tasks, we want 1 task to have 1 author

(event authors)
we want a user to be an author of several tasks, we want 1 event to have 1 author
"""

"""
We need to flesh this idea out more

class UserNotfication(Base):
    user = relationship('User')
    ... (Not sure about rest)
"""

"""
Groups<->Events
multiple groups to one event
multiple events to one group

needs to have a formed relationship with events
"""


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    # M2M
    users = relationship("User", secondary="group_users", back_populates="groups")
    description = Column(Text)
    # establish bidirectional relation between objects
    # user foreignkey relationship prior to indicate to sqlalchemy to load related obj at attribute access time
    owner = relationship("User", back_populates="groups", lazy="joined")
    tasklist = relationship("TaskList", back_populates="assignedGroup", lazy="joined")
    events = relationship("Event", secondary="event_group", back_populates="groups")


# GroupUser, EventGroup Table facilitates Many to Many relationship
"""
junction table, primary keys are declared as pair of columns
! users can belong to several groups, groups can have several users !

Can further add to GroupUser table
1. timestamps - track when user joins group or relationships are established
2. role or permission - can include column in GroupUser table to specify role or permission level of user in group
3. invitation track - if user is invited to join groups, provide columns illustrating invitation status, sender info, invitation data
4. notifications - implement notifications for user-group interactions
5. historical data - design table to store change history (users join, left groups)
6. analytics - add columns for analyzing user-group relations
"""


class GroupUser(Base):
    __tablename__ = "group_users"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))


"""
Theoretical implementation
Required for many to many relationship with events

many organizers to 1 event and many events to 1 organizer
many groups to 1 event and many events to 1 group
"""


class EventOrganizers(Base):
    __tablename__ = "user_organized_events"
    id = Column(Integer, primary_key=True)
    organizer_id = Column(Integer, ForeignKey("users.id"))
    event_id = Column(Integer, ForeignKey("events.id"))


class EventGroup(Base):
    __tablename__ = "event_group"
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))


# Testing Data Insertion
Base.metadata.create_all(engine)
with SessionLocal() as session:
    Group1 = Group(name="group1", description="group1 description")
    Group2 = Group(name="group2", description="group2 description")
    type1 = TaskType(name="critical")
    tasklist1 = TaskList(name="tasklist1", isCompleted=True, description="taskl 1")
    tasklist2 = TaskList(name="tasklist2", isCompleted=True, description="taskl 2")
    Task1 = Task(
        name="get eggs", description="we need eggs", isCompleted=False, quantity="10"
    )
    Task2 = Task(
        name="task2", description="desc2", isCompleted=True, quantity="task2 q"
    )
    User1 = User(
        username="user1",
        first_name="first1",
        last_name="last1",
        email="user1@user.com",
        about="about user1",
        hashed_password="user1 password",
        profile_photo="aws3.privatebucket.com/user1_photo",
        is_active=True,
    )
    User2 = User(
        username="user2",
        first_name="first2",
        last_name="last2",
        email="user2@user.com",
        about="about user2",
        hashed_password="user2 password",
        profile_photo="aws3.privatebucket.com/user2_photo",
        is_active=True,
    )
    User3 = User(
        username="user3",
        first_name="first3",
        last_name="last3",
        email="user3@user.com",
        about="about user3",
        hashed_password="user3 password",
        profile_photo="aws3.privatebucket.com/user3_photo",
        is_active=True,
    )
    InPerson = EventType(name="networking")
    specific_datetime = datetime(2021, 8, 1, 15, 30)
    specific_datetime2 = datetime(2020, 8, 1, 15, 30)
    Event1 = Event(
        name="event1",
        description="event1 description",
        html_link="event1_link",
        author=User1,
        organizers=[User1, User2],
        start=specific_datetime,
        duration=10,
        tasklist=tasklist1,
    )
    Event2 = Event(
        name="event2",
        description="event2 description",
        html_link="event2_link",
        author=User2,
        organizers=[User1, User2],
        start=specific_datetime2,
        duration=10,
        tasklist=tasklist2,
    )
    Calendar1 = Calendar(
        name="calendar 1", description="calendar description", events=[Event1, Event2]
    )
    Group1.owner_id = 1
    Group2.owner_id = 2
    Group1.users = [User1, User2]
    Group2.users = [User2, User3]
    User1.rsvps = [Event1, Event2]
    User2.rsvps = [Event1]
    session.add_all([Group1, Group2, User1, User2, User3])
    session.commit()

    # Get group with id 1 and print name, description
    with SessionLocal() as session:
        g1 = session.query(Group).where(Group.id == 1).one()
        g1_description = session.query(Group.description).where(Group.id == 1).one()
        g2 = session.query(Group).where(Group.id == 2).one()
        g2_description = session.query(Group.description).where(Group.id == 2).one()

with SessionLocal() as session:
    g1 = session.query(Group).where(Group.id == 1).one()
    print(g1.owner_id)
    print("group1 owner " + g1.owner.username)
    for u in g1.users:
        print(u.username)
    g2 = session.query(Group).where(Group.id == 2).one()
    print(g2.owner_id)
    print("group2 owner " + g2.owner.username)
    for u in g2.users:
        print(u.username)

# Fix N+1 SELECTS problem
with SessionLocal() as session:
    g1 = (
        session.query(Group).options(joinedload(Group.users)).where(Group.id == 1).one()
    )
print(g1.name)
