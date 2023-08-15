from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime, Integer, Text
from sqlalchemy.orm import relationship, joinedload
import database

Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

"""
Task Model

TaskList Model

TaskType Model
"""


class Task(Base):
    pass


class TaskList(Base):
    pass


class TaskType(Base):
    pass
