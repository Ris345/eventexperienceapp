from queries import users
import schemas
from queries.users import db_get_user, db_get_users
from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
    FastAPI,
)
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get("/users", response_model=List[schemas.UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db_get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=schemas.UserSchema)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db_get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=400, detail="user not found")
    return user

"""
router.get('/users/{user_id}/rsvps/)
- Get notifications for user via id

- will  have to query the rsvps of a user via the rsvp table that has foreign keys tied to user and event
- the rsvp object should look like this
    - rsvp:
        id: 1
        event: event 1
        user: user 1
        attending: True

user1 | id:1
    rsvps:
        [
        event1 : {
            attending: True
        }
        event2: {
            attending: False
        }
        event3:{
            attending: True
        }
        ]

(pub sub) - each user is subbed to notifications
type (current_day = current.utc_now, event.start_time) are datetime
type (current_day-event.start_time) are timedelta
push_notifications = []

[ if we want notifications to be pushed to a user dashboard an interval before event]

notification_interval = 1 day
for user in users:
    for event in user.events:
        if event[attending]==True and (current_day-event.start_time==notification_interval):
            push_notifications.push(event)
return push_notifications

[ if we want notifications to be pushed to a user db on the day of the event ]

for user in users:
    for event in events:
        if event[attending]==True and (current_day==event.start_time):
            push_notifications.push(event)
return push_notifications
"""
