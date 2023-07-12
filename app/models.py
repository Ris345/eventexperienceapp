from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime, Integer, Text
from sqlalchemy.orm import relationship
from .database import Base

"""
for test db:
username | password | role
user1   | secret1 | admin
user2 | secret2 | organizer
user3 | secret3 | volunteer

"""


# Creating classes that inherit from Base
# User Model that contains the attributes of id, username, ..., profile_photo to be a url coming from an s3 storage bucket, many to man relationship with groups meaning that there can be many users to one project, many projects to one user


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    about = Column(Text)
    hashed_password = Column(String)
    profile_photo = Column(String)
    created_at = Column(DateTime, default=DateTime.utcnow())
    # M2M
    groups = relationship("Group", secondary="group_users", back_populates="user")
    is_active = Column(Boolean, default=True)


class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))
    # M2M
    users = relationship("User", secondary="group_users", back_populates="group")
    description = Column(Text)


# Facilitates Many to Many relationship
class GroupUser(Base):
    __table__name__ = "group_users"
    id = Column(Integer, primary_key=True)
    notes = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    group_id = Column(Integer, ForeignKey("group.id"))


class Event(Base):
    pass


class Task(Base):
    pass


class TaskList(Base):
    pass


class Location(Base):
    pass


class Favorites(Base):
    pass


class RSVPS(Base):
    pass
