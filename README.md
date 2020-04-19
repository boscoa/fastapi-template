# Introduction 
FastAPI project template with custom shell script
Supports relational and NoSQL.
Uses alembic for relational database migrations.

# Planned
- Docker file
- HTTP Patch example

# Getting Started
1.	Install pipenv
2.	Install dependencies with ``sh ./script.sh install``
3.	Serve with ``sh ./script.sh serve``

# Build and Test
To test with coverage, use ``sh ./script.sh test``

# Script commands
- ``sh ./script.sh current`` Give the current alembic migration applied to the database
- ``sh ./script.sh downgrade $migration_name`` Downgrade the relational database to the specified migration name. Default: base
- ``sh ./script.sh install $env`` Install dependencies for a specified env. Default: dev
- ``sh ./script.sh migrate $migration_name`` Generate a new alembic migration with the given name 
- ``sh ./script.sh run`` Run the api
- ``sh ./script.sh serve`` Serve the api with reloading enable 
- ``sh ./script.sh test`` Test with coverage using pytest
- ``sh ./script.sh upgrade $migration_name`` Upgrade the relational database to the specified migration_name. Default: head


# Contribute
