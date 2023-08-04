# User Registration  API

- [User Registration API](#user-api)
  - [Create User](#create-user)
    - [Create User Request](#create-user-request)
    - [Create User Response](#create-user-response)


## Create User

### Create User Request

```js
POST api/register_user
```

```json
{
    "first_name": "Vegan",
     "last_name": "Sunshine",
    "email": "123Iamauser_eea@gmail.com",
    "password": "1234CoolApp",
    "date_created": "2023-04-08T11:00:00",
    "role": "Admin",
}
```

### Create User Response

```js
201 Created
```


```json
{
    "id": "01",
    "first_name": "Vegan",
    "last_name": "Sunshine",
    "email": "123Iamauser_eea@gmail.com",
    "password": "1234CoolApp",
    "date_created": "2022-04-08T11:00:00",
    "role": "role"
}
```
