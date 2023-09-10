- Completed
    - [ ] Establish the ability to CRUD users (FA docs)
        [x] Create Account (soon) -> Login
            - POST /USERS (soon) -> GET /TOKEN
        [] Update Account
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

- Rest of Agenda
