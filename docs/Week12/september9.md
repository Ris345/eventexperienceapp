- Completed
    - Establish the ability to CRUD users (FA docs)
        [x] Create Account (soon) -> Login
            - POST /USERS (soon) -> GET /TOKEN

    - [ ] TOKEN BE
        - [x] GET /TOKEN
        - [x] Logged in user can view account details
        - [x] Logged in
    - [x] Establish users are able to log out in mockup
        - DELETE TOKEN (or this might be a process of deleting token on fe?)

- Rest of Agenda
    - REST OF CRUD
        - [ ] Update Account
            - PUT/USER
        - [ ] Delete Account
            - DELETE/USER
        - [ ] Search for other accounts
            - ACCOUNT_USERNAME [x]
            - NAME (first and last name, first or last name) [ ]
            - EMAIL [ ]

    - [ ] TOKEN BE
        - [ ] (Sign Up) Ensure that the password is hashed and that said password is not able to be accessed on FE ( req password security )
        - [ ] Logged in user can update account details
        - [ ] Establish errors are present with invalid account creation, login in mockup

    - [ ] Implement Roles with Casbin/FastAPI middleware
    - [ ] Implementation of ACL Middleware/System for roles
