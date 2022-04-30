# RHoK Station

## Start the stack
Running the following commands.

```
./setup.sh
docker compose up
```

`setup.sh` scripts should contain all necessary setup.


## Services

### Postgres

Volumes:
- docker-entrypoint-initdb.d - folder that contains init sql scripts for postgres

### Adminer

After your enviroment spins up you can go to localhost:8765 and there you can inspect your database. Steps:

- Switch the System to PostgreSQL
- Use the name postgres in the Server input
- Use the username and password from the compose file (probably guest)