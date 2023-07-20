# Week of July 10th

# Considerations / Insight
- In regards to roles, there will be Admin, Organizer, Default User
    - Admin and Organizer
        * Tracks upcoming and present events
        * Track a list of volunteer tasks like distribute merchandise from Company X, Refill Coffee, etc.
    - Admin
        * Organizing events (management of tasks)
    - Organizer
        * Name appears on tasklist
    - Default User
        * Info on upcoming and present events via a notification/schedule
            * (?) For notifications, need to understand how that will operate via BE (notification system? pub/sub?)
            * (?) For schedule, most likely going to be a view of events from be of GET events_list

- As there are three roles does it require a table as there isn't just admin and superuser? Did some research on roles middleware for fastapi that would be helpful in implementation.

- Turns out there is ACL (Access Control Library) libraries/middleware able to be used for fastapi dbs
    * ![ACLs-Forum](../imgs/ACL_Implementation.png)
        ```
            Yes, of course. You just have to install them via pip (or any other tool you use) and then import and implement the access control logic in your path functions. Better yet, you can create helper functions or classes in external modules and just use them in your path functions.
        ```
        - [RBAC and ABAC auth using Casbin](https://github.com/tiangolo/fastapi/issues/5676)
        - [Fast API Casbin docs](https://github.com/pycasbin/fastapi-authz)

# 07/11/2023
- Going to do separate dbs for each ms using sqlite
    - wish me luck :3

# 07/17/2023
- Completed models, schemas on fastapi/sqlite branch
