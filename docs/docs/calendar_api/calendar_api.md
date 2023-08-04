# Calendar  API

- [Calendar API](#calendar-api)
  - [Create Calendar](#create-calendar)
    - [Create Calendar Request](#create-breakfast-request)
    - [Create Calednar Response](#create-calendar-response)
  - [Get Calendar](#get-calendar)
    - [Get Calendar Request](#get-calendar-request)
    - [Get Calendar Response](#get-calendar-response)
  - [Update Calendar](#update-calendar)
    - [Update Calendar Request](#update-calendar-request)
    - [Update Calendar Response](#update-calendar-response)
  - [Delete Calendar](#delete-calendar)
    - [Delete Calendar Request](#delete-calendar-request)
    - [Delete Calendar Response](#delete-breakfast-response)

## Create Calendar 

### Create Calendar Request

```js
POST api/calendar
```

```json

   {
  "event": {
    "title": "Dance Party",
    "date": "2023-08-15",
    "time": "15:00",
    "rsvp": true,
    "created_date": "2023-08-04T10:30:00Z"
  }
}

```

### Create Calendar Response

```js
201 Created
```


```json

    {
  "event": {
    "id": "01",
    "title": "Dance Party",
    "date": "2023-08-15",
    "time": "15:00",
    "rsvp": true,
    "created_date": "2023-08-04T10:30:00Z"
  }
}

```

## Get Calendar

### Get Calendar Request

```js
GET api/calendar/{{id}}
```

### Get Breakfast Response

```js
200 Ok
```

```json

     "event": {
    "id": "01",
    "title": "Dance Party",
    "date": "2023-08-15",
    "time": "15:00",
    "rsvp": true,
    "created_date": "2023-08-04T10:30:00Z"
  }
```

## Update Breakfast

### Update Breakfast Request

```js
PUT /breakfasts/{{id}}
```

```json
{
  "event": {
    "title": "Rave",
    "date": "2023-08-20",
    "time": "18:30",
    "rsvp": false,
    "modified_date": "2023-08-04T15:45:00Z"
  }
}
```

### Update Calendar Response

```js
204 No Content
```

or

```js
201 Created
```


## Delete Breakfast

### Delete Breakfast Request

```js
DELETE api/calendar/{{id}}
```

### Delete Breakfast Response

```js
204 No Content
```