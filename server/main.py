import models
from fastapi import FastAPI
import database
from routes import users, groups, tasks

engine = database.engine
Base = database.Base
# creates db tables based on defined models, bind=engine will use engine created earlier with presets
Base.metadata.create_all(bind=engine)

# create fastapi app
server = FastAPI()

# include routers that are defined via routers, syntax is [domain].router -> refers to router = ApiRouter() in each router file
server.include_router(users.router)
server.include_router(groups.router)
server.include_router(tasks.router)
