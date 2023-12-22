from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    String,
    DateTime,
    Integer,
    Text,
    func,
    Table
)
from sqlalchemy.orm import relationship, joinedload
import database
Base = database.Base
engine = database.engine
SessionLocal = database.SessionLocal


class Calendar(Base):
    __tablename__ = "real_calendar"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime, default=func.now())
    
    


    
    