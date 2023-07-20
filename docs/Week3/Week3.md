# 07/19/23
- changed schemas slightly
- removes uncommitted changes
    - revert back to progress of previous commit
        - `git reset --hard HEAD`
    - go back to a particular commit in current branch history
        - `git reset --hard HEAD@{n}`
- don't want to remove unstaged changes
    - `--soft` flag as opposed to `--hard`
- view commit history and what n is attached to which commit
    - `git reflog`
    - `git log --oneline --graph` (for visual representation)
        - to exit, press q

- Need to figure out migrations
- Need to figure out how to get Users connected to Groups via relationship to access User information
    - ie how do i get the username of a group's owner to show up when i do GET/groups, GET/group/{group_id}

# 07/18/23
- Used Peter's suggestions to modularize queries and routers of users and groups, users in users ms, groups in users ms
- Need to figure out migrations via Aembic


# GENERAL AGENDA
- Demo/Sample of BE -> FE functionality
    - User MS
        - To run user MS currently, (1) `uvicorn main:app --reload` -> (2) [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
        - First Draft
            - Local
                - [x] Establish DB setup for users first
                - [x] Ensure that user table can be setup with chosen db
                - [x] (fastapi) Setup queries, routers for users service and ensure there is proper operation with chosen db
                - [x] CRUD ( GET )
                    - [x] Able to get user(id), get users
                        - [x] GET /USER{ID} allows for viewing of user details
                        - [x] GET /USERS allows for viewing all users
                    - [x] Able to get group(id), get groups
                        - [x] GET /GROUP{ID} allows for viewing of group details
                        - [x] GET /GROUPS allows for viewing of all groups
- Rest of Agenda
            - [ ] Establish the ability to CRUD users (FA docs)
                - Create Account (soon) -> Login
                    - POST /USERS (soon) -> GET /TOKEN
                - Update Account
                    - PUT/USER_ID
                - Search for other accounts
                    - ACCOUNT_USERNAME, NAME, EMAIL
            - [ ] TOKEN BE
                - [ ] GET /TOKEN
                - [ ] (Sign Up) Ensure that the password is hashed and that said password is deleted on the FrontEnd ( req password security )
                - [ ] Logged in user can view account details
                - [ ] Logged in user can update account details
                - [ ] Logged in
            - [ ] Establish users are able to log out in mockup
                - DELETE TOKEN (or this might be a process of deleting token on fe?)
            - [ ] Establish users are able to login
                - GET TOKEN
            - [ ] Establish errors are present with invalid account creation, login in mockup
        - [ ] Implement Roles with Casbin/FastAPI middleware
            - [ ] Implementation of ACL Middleware/System for roles

- __SKELETON__
- Users:
    - The first step will be the entire user flow
        - 2 paths being: Create Account, Log In
            - Logged out (page that has printed on it 'ur logged out') -> (a) (button 'sign up') Create account -> button directs to a (form page) or (b) (button 'login') Login to prev created account
                - Successful Attempts (status code 500)
                    - (a) user inputs info on form page [ check to make sure there are no duplicate accounts, password is ok, username is okay, email is valid] [POST REQUEST] (500)-> clear form, successful login [GET TOKEN] -> direct to new page (page that has 'ur logged in' with user data on it except password) (cookie/token obtained after logging in) -> (button 'log out') Sign out [DELETE TOKEN] -> Back to start (page that has 'ur logged out' on it)
                        - Login form allows one to input username, email, first name, last name, password, profile photo, about me section {`user.description`}, profile photo (upload profile photo), select interests (drawn from a db that has all potential interests to match to a recommended event/events)
                    - (b) user inputs username and password -> press login button with correct info -> [LOGIN BE to check for correct account info]+[ GET TOKEN ] (500)-> site ('ur logged in' with 'sign out' button) has user data present without password
                        - Means I'm able to pass in user data from be to fe [ token, user data with hashed password, session (cookies) ]
                - Unsuccessful Attempts (status code 400?)
                    - (a) bad create account attempts -> tells user that 'x' is wrong
                        - user inputs data that is present with another user
                            - data that would present errors: same username
                            - tell user that there is an account with same username
                                - different accounts can have same email, first, last name etc. but not same username
                                - searching for accounts (?)
                        - invalid username, invalid first or last, invalid email
                    - (b) bad login attempt -> tell user there is no user with 'x' username, 'y' password
                        - 'user with {x} username not found'
                        - 'password and username combo does not match'
        - View account and details
            - View account role, access privileges
        - View account favorite events and rsvps
        - Update account
            - Update username, email, first name, last name, password, profile photo, about me section , profile photo (upload profile photo), interests

- Notes/Extraneous resources
    - Spatial/Location Info
        - [Using Open Street Map](https://wiki.openstreetmap.org/wiki/Using_OpenStreetMap#Web_applications)
        - [Spatial Data Apis](https://www.reddit.com/r/gis/comments/tb5rcq/what_are_some_of_your_favorite_apis_that_expose/)

- Google Calendar
    - [Python Quick Start](https://developers.google.com/calendar/api/quickstart/python)

    - [Api Key Setup](https://stackoverflow.com/questions/50881005/google-sheet-api-message-the-request-is-missing-a-valid-api-key)

        - Python Example
            - [Google Python Api Gateway](https://github.com/googleapis/python-api-gateway)
                - There is a quick start guide on that page, alot of instruction on implementing it locally !
