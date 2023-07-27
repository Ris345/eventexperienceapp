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

if [ -n "$SQLITE_DATABASES" ]; then
    echo "Multiple database initialization requested: $SQLITE_DATABASES"
    for db_file in $(echo $SQLITE_DATABASES | tr ',' ' '); do
        initialize_database $db_file
    done
    echo "Multiple databases initialized"
fi

# alembic.ini
[alembic]
script_location = alembic

# Point to your SQLite database file
sqlalchemy.url = sqlite:///path/to/database.sqlite3
