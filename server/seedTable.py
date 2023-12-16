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
)
from sqlalchemy.orm import relationship, joinedload
import database
from models.tasks import Task, TaskProperties
from models.eventsUserJoinTable import EventsUserTable, EventsOrganizerTable, EventParticipants, EventProperties
from models.events import Event
from models.users import User
# from models.events import Event, EventProperties, EventParticipants, EventsUserTable


Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

# Testing Data Insertion - models, tasks
Base.metadata.create_all(engine)
with SessionLocal() as session:
    # Priority1 = Priority(name="urgent", level=10)
    # Priority2 = Priority(name="semi-urgent", level=5)
    # Type1 = TaskType(name="type1")
    # Type2 = TaskType(name="type2")
    # Tasklist1 = TaskList(
    #     name="tasklist1",
    #     isCompleted=False,
    #     description="tasklist1 desc",
    #     priority=Priority1,
    # )
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
    Task1 = Task(
        isCompleted=False,
    )

    Task2 = Task(
        isCompleted=False,

    )
#     Group1 = Group(name="group1", description="group1 description")
#     Group2 = Group(name="group2", description="group2 description")
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
    eprops1 = EventProperties(event_name = "ename1", event_date = datetime.now(), start_time = datetime.now() + timedelta(hours = 1), end_time = datetime.now() + timedelta(hours = 3), event_location = "location1")
    eprops2 = EventProperties(event_name = "ename2", event_date = datetime.now(), start_time = datetime.now() + timedelta(hours = 12), end_time = datetime.now() + timedelta(hours = 15), event_location = "location1")
    epart1 = EventParticipants()
    epart2 = EventParticipants()
    epart1.event_properties_id = 1
    epart2.event_properties_id = 2
    event1 = Event()
    event2 = Event()
    event1.properties_id = 1
    event2.properties_id = 2
    eprops1.event_id = 1
    eprops2.event_id = 2

    tprops1 = TaskProperties(description = "desc1", quantity = 1)
    tprops2 = TaskProperties(description = "desc2", quantity = 2)
    # Type1.tasks = [Task1, Task2]
    # Tasklist1.tasks = [Task1, Task2]
    # Tasklist1.priority = Priority1
    # Task1.priority = Priority1
    Task1.properties_id = 1
    Task2.properties_id = 2
    # TaskList.tasks = [Task1, Task2]
    # Group1.owner_id = 1
    # Group2.owner_id = 2
    # Group1.users = [User1, User2]
    # Group2.users = [User2, User3]
    # User1.task_assignments = [Task1]
    # User2.task_assignments = [Task2]
    # User1.authored_tasks = [Task2]
    # User2.authored_tasks = [Task1]
    session.add_all(
        [
            # Group1,
            # Group2,
            User1,
            User2,
            User3,
            Task1,
            Task2,
            # Tasklist1,
            tprops1,
            tprops2,
            # Priority1,
            # Priority2,
            # Type1,
            # Type2,
            eprops1,
            eprops2,
            epart1,
            epart2,
            event1,
            event2

        ]
    )
    session.commit()

# Get group with id 1 and print name, description
#     with SessionLocal() as session:
#         g1 = session.query(Group).where(Group.id == 1).one()
#         g1_description = session.query(Group.description).where(Group.id == 1).one()
#         g2 = session.query(Group).where(Group.id == 2).one()
#         g2_description = session.query(Group.description).where(Group.id == 2).one()

# with SessionLocal() as session:
#     g1 = session.query(Group).where(Group.id == 1).one()
#     print(g1.owner_id)
#     print("group1 owner " + g1.owner.username)
#     for u in g1.users:
#         print(u.username)
#     g2 = session.query(Group).where(Group.id == 2).one()
#     print(g2.owner_id)
#     print("group2 owner " + g2.owner.username)
#     for u in g2.users:
#         print(u.username)

# Fix N+1 SELECTS problem
# with SessionLocal() as session:
#     g1 = (
#         session.query(Group).options(joinedload(Group.users)).where(Group.id == 1).one()
#     )
# print(g1.name)

# example of adding one to many and many to many relationships

with SessionLocal() as session:
    e1 = session.query(Event).where(Event.id == 1).one()
    eProp = session.query(EventProperties).where(EventProperties.id == 1).one()
    ePart = session.query(EventParticipants).where(EventParticipants.id == 1).one()
    print(e1,eProp, ePart)
    user = session.query(User).where(User.id == 1).one()
    user2 = session.query(User).where(User.id == 2).one()
    user3 = session.query(User).where(User.id == 3).one()
    # eProp.event.append(e1)
    eProp.organizer.append(user)
    ePart.participants.append(user)
    ePart.participants.append(user2)

    session.commit()
