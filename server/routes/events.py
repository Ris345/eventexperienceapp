from schemas.events import EventPropertiesSchema, EventSchema
from queries.events import db_get_events, db_create_event
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
