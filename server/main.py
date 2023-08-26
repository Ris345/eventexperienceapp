from fastapi import FastAPI
import database
from routes import users, groups, tasks
from fastapi.middleware.cors import CORSMiddleware

# can import admin from .internal
from internal import admin

engine = database.engine
Base = database.Base
# creates db tables based on defined models, bind=engine will use engine created earlier with presets
Base.metadata.create_all(bind=engine)

# create fastapi app
server = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
]

server.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers that are defined via routers, syntax is [domain].router -> refers to router = ApiRouter() in each router file
server.include_router(users.router)
server.include_router(groups.router)
server.include_router(tasks.router)
server.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    # dependencies = [Depends(get_token_header)]
    responses={418: {"description": "admin ops"}},
)
