# Events API

## Create Event

**Create Event Request**

```js

POST api/events


201 Created

{
    "id": "01",
    "properties": {
        "eventName": "Birthday Party",
        "eventDate": "2023-08-03T18:00:00Z",
        "startTime": "1:00 PM",
        "endTime": "5:00 PM",
        "eventLocation": "Party Hall",
        "participants": ["John", "Jane", "Alice"],
        "organizer": "Event Planner"
    },
    "rsvp": true,
    "date_created": "2023-04-06T12:00:00Z",
    "lastModifiedDateTime": "2023-04-06T12:00:00Z"
}

Get Events


GET api/events


Get Events Response


200 Ok

{
    "id": "01",
    "properties": {
        "eventName": "Birthday Party",
        "eventDate": "2023-08-03T18:00:00Z",
        "startTime": "1:00 PM",
        "endTime": "5:00 PM",
        "eventLocation": "Party Hall",
        "participants": ["John", "Jane", "Alice"],
        "organizer": "Event Planner"
    },
    "rsvp": true,
    "date_created": "2023-04-06T12:00:00Z",
    "lastModifiedDateTime": "2023-04-06T12:00:00Z"
}
Update Event
Update Event Request


PUT /events/{{id}}

{
    "id": "01",
    "properties": {
        "eventName": "Birthday Party",
        "eventDate": "2023-08-03T18:00:00Z",
        "startTime": "1:00 PM",
        "endTime": "5:00 PM",
        "eventLocation": "Party Hall",
        "participants": ["John", "Jane", "Alice"],
        "organizer": "Event Planner"
    },
    "rsvp": true,
    "date_created": "2023-04-06T12:00:00Z",
    "lastModifiedDateTime": "2023-04-06T12:00:00Z"
}

Update Event Response


204 No Content
or


201 Created
Delete Event
Delete Event Request


DELETE /events/{{id}}


204 No Content
