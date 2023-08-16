from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime, Integer, Text
from sqlalchemy.orm import relationship, joinedload
import database

Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

"""
! subject to change !

fk = foreign key
pk = primary key

Task Model
class Task(Base):
    id - primaryKey, int
    name - str
    owner - fk to users table
    description - text
    tasklist - fk to tasklist
    assigned_user - fk to users table
    type - fk to types table
    isCompleted - boolean, true/false
    priority - fk to priority table

Multiple tasks to one user
Cant have multiple users assigned to one task
    - thats what im assuming tasklist would alleviate (?)

TaskList Model
    id - pk, int
    name - str
    owner - fk to user table
    isCompleted - boolean
    priority - fk to priority table
    assigned_group - fk to group table
    description - text

TaskType Model
    id - pk, int
    name - name of type

Priority Model
    id - pk, int
    name - str ex: urgent
    level - int ex: out of x
"""


class Task(Base):
    pass


class TaskList(Base):
    pass


class TaskType(Base):
    pass
