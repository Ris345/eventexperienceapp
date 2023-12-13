from models.events import Event
from models.eventsUserJoinTable import EventParticipants, EventProperties
from schemas.events import EventPropertiesSchema, EventSchema
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

def db_create_event(db : Session, event_name, event_date, start_time, end_time, event_location ):


  new_event = Event(rsvp = False)
  new_event_property = EventProperties(
event_name= event_name, event_date=event_date, start_time=start_time, end_time=end_time, event_location=event_location
  )
  # new_event.properties = new_event_property
  print(new_event_property)
  db.add(new_event)
  db.add(new_event_property)
  db.commit()
  db.refresh(new_event)
  new_event.properties_id = new_event_property.id
  db.commit()
  db.refresh(new_event_property)



  return new_event
  # return {
  #   "message" : "created"
  # }
