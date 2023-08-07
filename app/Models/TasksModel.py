from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, String, DateTime, Integer, Text
from sqlalchemy.orm import relationship, joinedload
import database

Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal

class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    quantity = Column(Integer)
    date_created = Column(DateTime, default=datetime.utcnow())
    lastModifiedDateTime = Column(DateTime)

Base.metadata.create_all(engine)
with SessionLocal() as session:
    Task1 = Task(
        task="task1",
        quantity=2,
    )
    Task2 = Task(
        task="task2",
        quantity=420
    )
    session.add_all([Task1, Task2])
    session.commit()
