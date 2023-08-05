import models
from fastapi import FastAPI
import database

engine = database.engine

from routes import users, groups

# creates db tables based on defined models, bind=engine will use engine created earlier with presets
models.Base.metadata.create_all(bind=engine)

# create fastapi app
app = FastAPI()

# include routers that are defined via routers, syntax is [domain].router -> referes to router = ApiRouter() in each router file
app.include_router(users.router)
app.include_router(groups.router)
