from models.events import Event
from models.eventsUserJoinTable import EventParticipants, EventProperties
from schemas.events import EventPropertiesSchema, EventSchema
from sqlalchemy.orm import Session, joinedload
def db_get_events(db : Session, skip : int = 0, limit : int =100):
  events = (
    db.query(Event)
    .options(joinedload(Event.properties)
             .options(joinedload(EventProperties.event_participants)
                      .options(joinedload(EventParticipants.participants)))

             )

    .first()
  )
  # event_schema = [EventSchema.from_orm(event) for event in events]

  return events
