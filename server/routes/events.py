from schemas.events import EventPropertiesSchema, EventSchema
from queries.events import db_get_events, db_create_event, db_get_event_by_id, db_add_participants
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    FastAPI,
    Form
)
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List
from datetime import datetime
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    tags=["events"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}},
)

# @router.get("/events", response_model = List[EventSchema])
@router.get("/events")
def get_events(skip : int = 0, limit : int = 100, db: Session = Depends(get_db)):
    events = db_get_events(db, skip, limit)
    print(type(events[0].properties.event_participants.participants))
    return events
@router.get("/event/{id}")
def get_event(id : int ,db: Session = Depends(get_db)):
    event = db_get_event_by_id(db=db, event_id=id)
    return event

@router.post("/events/create")
def post_event(
    db: Session = Depends(get_db),
    event_name : str = Form(...),
    event_date : datetime = Form(...),
    start_time : datetime = Form(...),
    end_time : datetime = Form(...),
    event_location : str = Form(...),
    ):
#
    return db_create_event(db,event_name= event_name, event_date=event_date, start_time=start_time, end_time=end_time, event_location=event_location)

@router.put("/events/add_participants")
def add_participants(
    db : Session = Depends(get_db),
    user_id : int = Form(...),
    event_id : int = Form(...)
):
    db_add_participants(db=db, user_id=user_id, event_id=event_id)
    return {"message" : "added participants"}
