from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ./sql_app.db (opening a file in sqlite db), file located in same directory in file sql_app.db
SQLALCHEMY_DATABASE_URL = "sqlite:///./users_sql_app.db"

# using sync(def) functions, check_same_thread parameter allows >1 thread to interact with db for same request
"""
core interface to db and used to connect to db -
    connect_args - keyword arguments, check_same_thread allows for more than 1 thread to interact with db at same time for dev purposes req multiple connections
    echo - enavles sqla to log all sql satements for debugging
    future: enables 2.0 sqla behavior
"""
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True,
    future=True,
)

# each instance of sessionlocal class is a db session
"""
SessionLocal = factory for creating new Session objects
Session = transactional scope for db interaction
    - autocommit = false (req explicit calls to commit() to persist changes to db)
    - autoFlush = false (don't auto flush changes to db before querying)
    - bind = pass engine instance created earlier to bind 'Session' to db engine allowing session to use engine to communicate with db
"""
SessionLocal = sessionmaker(
    autocommit=False, expire_on_commit=False, autoflush=False, bind=engine
)

# Base is instance of declarative Base which is a factory function for creating base classes for declarative sqlalchemy models
Base = declarative_base()
