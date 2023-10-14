# August 31
## Security
### First Steps
1. Imported OAuth2PasswordBearer and then created instance of passwordBearer using tokenUrl being a string 'token'
2. installed python-multipart
    - `pip install python-multipart`
3. Password Flow
    - Password flow is a type of flow defined to handle security, auth
    - Oauth2 designed in order for BE, API to be independent from server authenticating user
    * User, pass submitted -> send both inputs to url in api declared with scheme -> api check username and password and respond with token
        - token is set to expire after a set period of time
    * fe stores token temporarily -> user clicks in fe to go to another section in fe -> fe req to fetch more data from API
        * in order to authenticate with api, send header auth with value of Bearer + token
        * if token contains `arbitrary_string`, Authorization header is `Bearer arbitrary_string`

4. What IT Does
    - find and look in request for Auth header and check if value is Bearer + token, return token as str
    - If missing auth header / no Bearer token, respond with 401 status code i.e. unauthorized
    - already in docs, trying to access an endpoint without token, responds with `not authenticated`
