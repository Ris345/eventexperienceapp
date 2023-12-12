from schemas.events import EventPropertiesSchema, EventSchema

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

@router.get("/events")
def get_events():
    return {"message":"events get"}
