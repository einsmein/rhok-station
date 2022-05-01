# RHoK Station

## Start the stack
1. Copy `.env.example` to `.env` and set the variables.
2. Running the following commands.
```
./scripts/setup.sh
./scripts/deploy.sh
```
`scripts/setup.sh` scripts should contain all necessary setup.

## Setup metabase
To integrate with postgres, specify host as `postgres`.

## Services

### Postgres

Volumes:
- docker-entrypoint-initdb.d - folder that contains init sql scripts for postgres

### Adminer

After your enviroment spins up you can go to localhost:8765 and there you can inspect your database. Steps:

- Switch the System to PostgreSQL
- Use the name postgres in the Server input
- Use the username and password from the compose file (probably guest)
