from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ./sql_app.db (opening a file in sqlite db), file located in same directory in file sql_app.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# using sync(def) functions, check_same_thread parameter allows >1 thread to interact with db for same request
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True,
    future=True,
)

# each instance of sessionlocal class is a db session,
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative_base() returns a class
Base = declarative_base()
