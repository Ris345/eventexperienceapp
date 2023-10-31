from fastapi import Depends, HTTPException, APIRouter, Form, status, Request
from sqlalchemy.orm import Session
from typing import List, Annotated
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

@router.get("/events/test")
async def events_test():
    return "event test endpoint"
