# Notes
- DB Migration = script defining changes to db schema: creating/updating tables, indices, or constraints
    - Use to manage db schema evolution as app evolves+changes

- Changes made to data model req changes to schema and migration tools allow for management of changes in controlled, consistent manner
    - Alembic allows for defining of db scripts (upgrade, downgrade)
    - Scripts can be versioned, applied in sequence to move db schema from diff vers

- Overview
    1. Define db models, tables w/ SQLAlchemy in py code
    2. Need to make change to db schema -> create new migration script w/ Alembic (script captures changes req to make to schema)
    3. each script version is stored in dir called 'versions' with unique id
    4. Alembic maintains a table in db to keep track of current version `alembic_version`
    5. run app/migration command triggers alembic to check current version of db against latest migration script version
    6. alembic executes migration scripts in correct order to apply changes
