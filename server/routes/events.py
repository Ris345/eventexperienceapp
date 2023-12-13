from schemas.events import EventPropertiesSchema, EventSchema
from queries.events import db_get_events, db_get_events2
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

@router.get("/events2", response_model = List[EventSchema])
def get_events(skip : int = 0, limit : int = 100, db: Session = Depends(get_db)):
    events = db_get_events2(db, skip, limit)
    return events
