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
from models.tasks import Task, TaskProperties


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
    # older relationship
    # task_assignments = relationship(
    #     "Task", back_populates="assignee", foreign_keys="[Task.assignee_id]"
    # )
    task_assignments2 = relationship(
        "TaskProperties", back_populates="assignee", foreign_keys="[TaskProperties.assignee_id]"
    )
    # authored_tasks = relationship(
    #     "Task", back_populates="author", foreign_keys="[Task.author_id]"
    # )


"""
Favorites Model
many favorites to one event, fk to events

class Favorite(Base):
    __tablename__='favorites'
    (attributes)
        event
        user

RSVP Model
many rsvps to one event, fk to events

class RSVP(Base):
    __tablename__='rsvps'
    (attributes)
        event
        user
        is_attending = Column(Boolean, default=True)
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

events = relationship("Event", secondary="event_group", back_populates="groups")
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

class EventGroup(Base):
    __tablename__ = "event_group"
    event_id = Column(Integer, ForeignKey("events.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
"""


# Testing Data Insertion - models, tasks
# Base.metadata.create_all(engine)
# with SessionLocal() as session:
#     # Priority1 = Priority(name="urgent", level=10)
#     # Priority2 = Priority(name="semi-urgent", level=5)
#     # Type1 = TaskType(name="type1")
#     # Type2 = TaskType(name="type2")
#     # Tasklist1 = TaskList(
#     #     name="tasklist1",
#     #     isCompleted=False,
#     #     description="tasklist1 desc",
#     #     priority=Priority1,
#     # )
#     User2 = User(
#         username="user2",
#         first_name="first2",
#         last_name="last2",
#         email="user2@user.com",
#         about="about user2",
#         hashed_password="user2 password",
#         profile_photo="aws3.privatebucket.com/user2_photo",
#         is_active=True,
#     )
#     User1 = User(
#         username="user1",
#         first_name="first1",
#         last_name="last1",
#         email="user1@user.com",
#         about="about user1",
#         hashed_password="user1 password",
#         profile_photo="aws3.privatebucket.com/user1_photo",
#         is_active=True,
#     )
#     Task1 = Task(
#         isCompleted=False,
#     )

#     Task2 = Task(
#         isCompleted=False,

#     )
#     Group1 = Group(name="group1", description="group1 description")
#     Group2 = Group(name="group2", description="group2 description")
#     User3 = User(
#         username="user3",
#         first_name="first3",
#         last_name="last3",
#         email="user3@user.com",
#         about="about user3",
#         hashed_password="user3 password",
#         profile_photo="aws3.privatebucket.com/user3_photo",
#         is_active=True,
#     )

#     tprops1 = TaskProperties(description = "desc1", quantity = 1)
#     tprops2 = TaskProperties(description = "desc2", quantity = 2)
#     # Type1.tasks = [Task1, Task2]
#     # Tasklist1.tasks = [Task1, Task2]
#     # Tasklist1.priority = Priority1
#     # Task1.priority = Priority1
#     Task1.properties_id = 1
#     Task2.properties_id = 2
#     # TaskList.tasks = [Task1, Task2]
#     Group1.owner_id = 1
#     Group2.owner_id = 2
#     Group1.users = [User1, User2]
#     Group2.users = [User2, User3]
#     User1.task_assignments = [Task1]
#     User2.task_assignments = [Task2]
#     User1.authored_tasks = [Task2]
#     User2.authored_tasks = [Task1]
#     session.add_all(
#         [
#             Group1,
#             Group2,
#             User1,
#             User2,
#             User3,
#             Task1,
#             Task2,
#             # Tasklist1,
#             tprops1,
#             tprops2,
#             # Priority1,
#             # Priority2,
#             # Type1,
#             # Type2,
#         ]
#     )
#     session.commit()

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
