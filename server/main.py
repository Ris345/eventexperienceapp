from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import database
from routes import users, groups, tasks
from fastapi.middleware.cors import CORSMiddleware

# can import admin from .internal
from internal import admin

engine = database.engine

from routes import users, groups, tasks, token

# creates db tables based on defined models, bind=engine will use engine created earlier with presets
# models.Base.metadata.create_all(bind=engine)

# create fastapi server
server = FastAPI()
"""
Required at some point for deployment

allow_origins=[os.environ.get("CORS_HOST", "http://localhost:3000")],
"""
server.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],  # need to remove this in production
    allow_methods=["*"],
    allow_headers=["*"],
)
# include routers that are defined via routers, syntax is [domain].router -> refers to router = ApiRouter() in each router file
server.include_router(users.router)
server.include_router(groups.router)
server.include_router(tasks.router)
server.include_router(token.router)
