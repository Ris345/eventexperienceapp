from queries.users import (
    db_get_users,
    db_get_user_by_id,
    db_get_user_by_username,
    db_get_user_by_email,
    UserSchema,
    UserCreate,
    db_create_user,
    db_check_email_and_username,
)
from fastapi import (
    Depends,
    HTTPException,
    APIRouter,
    Form,
    status,
    Request,
    Query,
    Path,
)
from fastapi.encoders import jsonable_encoder
from ..dependencies import get_token_header
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not Found"}},
)


@router.get("/users", response_model=List[UserSchema])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db_get_users(db, skip=skip, limit=limit)
    return users


@router.get("/users_by_user_id/{user_id}", response_model=UserSchema)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db_get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=400, detail="user not found")
    return user


@router.get("/users_by_user_username/{username}", response_model=UserSchema)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    username = db_get_user_by_username(db, username)
    if username is None:
        raise HTTPException(status_code=400, detail="user not found")
    return username


@router.get(
    "/search/user={username}+email={email}",
    response_model=UserSchema,
)
def get_user_by_username_and_email(
    username: str = Path(..., description="user username"),
    email: str = Path(..., description="user email"),
    db: Session = Depends(get_db),
):
    try:
        userFound = db_check_email_and_username(db, username, email)
        if userFound is None:
            raise HTTPException(status_code=400, detail="user not found")
        return userFound
    except HTTPException:
        raise


@router.post("/users", response_model=UserSchema)
def create_user(
    username: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(...),
    profile_photo: str = Form(...),
    about: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        db_get_userby_username = db_get_user_by_username(db, username=username)
        if db_get_userby_username is not None:
            raise HTTPException(
                status_code=400, detail="Username is already registered to a user"
            )

        db_get_userby_email = db_get_user_by_email(db, email=email)
        if db_get_userby_email is not None:
            raise HTTPException(
                status_code=400, detail="Email is already registered to a user"
            )

        user = UserCreate(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hash(password),
            about=about,
            profile_photo=profile_photo,
        )

        return db_create_user(db=db, user=user)
    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Can not create an account with those credentials",
        ) from e


# @router.put
# @router.delete
"""
# Admin Router
- As a start we can perform a get request for a singular user and get their rsvps, favorites, and tasks, tasklists

router.get('/users/{user_id}/rsvps)
router.get('/users/{user_id}/favorites')
* router.get('/users/.../tasks')
* router.get('/users/.../tasklists')
    * basically want to get the tasks, tasklists that a user has subscribed with


- Eventually we want to do it for the signed in user using account data via the token/user session

# Via GetAccount Data
router.get('/get_account/rsvps')
router.get('/get_account/favorites')
router.get('/get_account/tasks')
router.get('/get_account/tasklists')


- Get notifications for user via id
router.get('/get_account/notifications')
    * with this we want to have notifications about events, changes made to events, tasks, changes made to tasks/tasklists


! AMATEUR NOVICE IMPLEMENTATION !

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
notification = "your event is soon"
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
