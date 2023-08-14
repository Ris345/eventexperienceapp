# Tasks API

- [Tasks API](#tasks-api)
  - [Create Tasks](#create-tasks)
    - [Create Tasks Request](#create-tasks-request)
    - [Create Tasks Response](#create-tasks-response)
  - [Get Tasks](#get-tasks)
    - [Get Tasks Request](#get-tasks-request)
    - [Get Tasks Response](#get-tasks-response)
  - [Update Tasks](#update-tasks)
    - [Update Tasks Request](#update-tasks-request)
    - [Update Tasks Response](#update-tasks-response)
  - [Delete Tasks](#delete-tasks)
    - [Delete Tasks Request](#delete-tasks-request)
    - [Delete Tasks Response](#delete-tasks-response)

## Create Tasks

### Create Task Request

```js
POST api/tasks
```

```json
{
    "properties": {
        "description": "Buy Groceries",
        "quantity": 10,           
        "assigned_user": "volunteer",
    },
    "complete": false,
    "date_created": "2023-08-03T12:00:00Z",
    "lastModifiedDateTime": "2022-04-06T12:00:00Z"
}
```

### Create Task Response

```js
201 Created
```


```json
{
    "id": "01",
    "properties": {
        "description": "Buy Groceries",
        "quantity": 10,           
        "assigned_user": "volunteer",
    },
    "complete": false,
    "date_created": "2023-08-03T12:00:00Z",
    "lastModifiedDateTime": "2022-04-06T12:00:00Z"
}
```

## Get Tasks

### Get Tasks Request



### Get Tasks Response

```js
200 Ok
```

```json
{
    "id": "01",
    "properties": {
        "description": "Buy Groceries",
        "quantity": 10,           
        "assigned_user": "volunteer",
    },
    "complete": false,
    "date_created": "2023-08-03T12:00:00Z",
    "lastModifiedDateTime": "2022-04-06T12:00:00Z"
}
```

## Update Tasks

### Update Tasks Request

```js
PUT /tasks/{{id}}
```

```json
{
    "id": "01",
    "properties": {
        "description": "Buy Groceries",
        "quantity": 10,           
        "assigned_user": "volunteer",
    },
    "complete": false,
    "date_created": "2023-08-03T12:00:00Z",
    "lastModifiedDateTime": "2022-04-06T12:00:00Z"
}
```

### Update Task Response

```js
204 No Content
```

or

```js
201 Created
```


## Delete Task

### Delete Task Request

```js
DELETE /tasks/{{id}}
```

### Delete Task Response

```js
204 No Content
```