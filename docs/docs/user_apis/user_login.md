# User Login  API

- [User_Registration API](#login-api)
  - [Create User](#create-login)
    - [Create User Request](#create-login-request)
    - [Create User Response](#create-login-response)


## Create Login

### Create Login Request

```js
POST api/login_user
```

```json
{
    "user_name": "Vegan",
    "password": "Sunshine",
}
```

### Create User Response

```js
201 Created
```


```json
{
    "id": "01",
    "user_name": "Vegan",
    "password": "Sunshine",
}
```
