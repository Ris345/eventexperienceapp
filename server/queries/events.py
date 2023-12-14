from models.events import Event
from models.eventsUserJoinTable import EventParticipants, EventProperties
from schemas.events import EventPropertiesSchema, EventSchema
from queries.users import db_get_user_by_id
from sqlalchemy.orm import Session, joinedload

def db_get_events(db : Session, skip : int = 0, limit : int = 100):
  events = (
    db.query(Event)
    .options(joinedload(Event.properties)
             .options(joinedload(EventProperties.event_participants)
                      .options(joinedload(EventParticipants.participants)))
             )
    .all()
  )
  event_schema = [EventSchema.from_orm(event) for event in events]
  return event_schema

def db_get_event_by_id(db : Session, event_id):
  event = (
    db.query(Event)
    .where(Event.id == event_id)
    .options(joinedload(Event.properties)
             .options(joinedload(EventProperties.event_participants)
                      .options(joinedload(EventParticipants.participants)))
             )
    .first()
  )
  # event_schema = [EventSchema.from_orm(event) for event in events]
  return event

def db_create_event(db : Session, event_name, event_date, start_time, end_time, event_location ):


  new_event = Event(rsvp = False)

  new_participants = EventParticipants()

  db.refresh(new_event)
  new_event.properties_id = new_event_property.id
  new_participants.event_properties_id = new_event_property.id
  db.commit()
  db.refresh(new_event_property)
  db.refresh(new_participants)
  return new_event
  # return {
  #   "message" : "created"
  # }

def db_add_participants(db : Session, user_id):
  user = db_get_user_by_id(db=db, user_id = user_id)

