from Models import TasksModel
import models
from fastapi import FastAPI
import database

engine = database.engine

from routes import users, groups

models.Base.metadata.create_all(bind=engine)
TasksModel.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(users.router)
app.include_router(groups.router)

