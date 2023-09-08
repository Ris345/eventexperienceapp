import models
from fastapi import FastAPI

import database

engine = database.engine

from routes import users, groups, tasks, token

# creates db tables based on defined models, bind=engine will use engine created earlier with presets
# models.Base.metadata.create_all(bind=engine)

# create fastapi server
server = FastAPI()

# include routers that are defined via routers, syntax is [domain].router -> referes to router = ApiRouter() in each router file
server.include_router(users.router)
server.include_router(groups.router)
server.include_router(tasks.router)
server.include_router(token.router)
