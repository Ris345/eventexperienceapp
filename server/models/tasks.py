from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime, Integer, Text
from sqlalchemy.orm import relationship, joinedload
import database

Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal
from models.users import User, UserTasks, AuthoredTasks

"""
! subject to change !

fk = foreign key
pk = primary key

Task Model
class Task(Base):
    id - primaryKey, int
    name - str
    author - fk to users table
    description - text
    tasklist - fk to tasklist
    assigned_user - fk to users table
    type - fk to types table
    isCompleted - boolean, true/false
    priority - fk to priority table
    Multiple tasks to one user
    Cant have multiple users assigned to one task
        - thats what im assuming tasklist would alleviate (?)
    """


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    isCompleted = Column(Boolean, default=False)
    quantity = Column(Integer)
    # fk to tasklist
    tasklist_id = Column(Integer, ForeignKey("task_list.id"))
    # fk to type
    type_id = Column(Integer, ForeignKey("task_type.id"))
    # fk to priority
    priority_id = Column(Integer, ForeignKey("task_priority.id"))
    # Define relationships directly in the class definition
    task_list = relationship("TaskList", back_populates="tasks", lazy="joined")
    author = relationship("User", secondary="authored_tasks", back_populates="tasks")
    assignedUser = relationship("User", secondary="user_tasks", back_populates="tasks")
    task_type = relationship(
        "TaskType", back_populates="tasks", lazy="joined", foreign_keys=[type_id]
    )
    task_priority = relationship(
        "Priority", back_populates="tasks", lazy="joined", foreign_keys=[priority_id]
    )


"""
TaskList Model
    id - pk, int
    name - str
    owner - fk to user table
    isCompleted - boolean
    priority - fk to priority table
    assigned_group - fk to group table
    description - text
"""


class TaskList(Base):
    __tablename__ = "task_list"
    __table_args__ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner = Column(Integer, ForeignKey("users.id"))
    isCompleted = Column(Boolean, default=False)
    description = Column(Text)
    priority_id = Column(Integer, ForeignKey("task_priority.id"))
    task_priority = relationship("Priority", back_populates="task_list")
    assignedGroup_id = Column(Integer, ForeignKey("groups.id"))
    assignedGroup = relationship("Group", back_populates="task_list", lazy="joined")
    tasks = relationship("Task", back_populates="task_list", lazy="joined")


"""
TaskType Model
    id - pk, int
    name - name of type
"""


class TaskType(Base):
    __tablename__ = "task_type"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tasks = relationship("Task", back_populates="task_type", lazy="joined")


"""
Priority Model
    id - pk, int
    name - str ex: urgent
    level - int ex: out of x
"""


class Priority(Base):
    __tablename__ = "task_priority"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    level = Column(Integer)
    task_list = relationship("TaskList", back_populates="task_priority")
    tasks = relationship("Task", back_populates="task_priority")


# Test if models work
Base.metadata.create_all(engine)
# with SessionLocal() as session:
#     tasklist1 = TaskList(name="tasklist1")
#     tasklist2 = TaskList(name="tasklist2")
#     task1 = Task(name="task1", description="description1")
#     task2 = Task(name="task2", description="description2")
#     task3 = Task(name="task3", description="description3")
#     task1.tasklist_id = 1
#     task2.tasklist_id = 1
#     task3.tasklist_id = 2
#     task1.assigned_user_id = 1
#     tasklist1.tasks = [task1, task2]
#     tasklist2.tasks = [task3]
#     priority1 = Priority(name="high", level=10)
#     tasktype1 = TaskType(name="tasktype1")
#     task1.priority_id = 1
#     task2.priority_id = 1
#     task3.priority_id = 1
#     task1.type_id = 1
#     task2.type_id = 1
#     task3.type_id = 1

#     session.add_all([tasklist1, tasklist2, task1, task2, task3, priority1, tasktype1])
#     session.commit()
