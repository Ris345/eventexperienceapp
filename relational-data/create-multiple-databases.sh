# .sh file
#!/bin/bash

set -e
set -u

function initialize_database() {
    local database_file=$1
    echo "  Initializing database: '$database_file'"
    # Run any database setup commands here
    # For example, if you're using an ORM like SQLAlchemy, you can use Alembic for migrations
    alembic -c alembic.ini upgrade head
}

if [ -n "$TASKS_DB" ]; then
    initialize_database "$TASKS_DB"
fi

if [ -n "$EVENTS_DB" ]; then
    initialize_database "$EVENTS_DB"
fi

if [ -n "$USERS_DB" ]; then
    initialize_database "$USERS_DB"
fi

echo "Initialization completed"
