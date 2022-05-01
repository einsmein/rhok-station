CREATE DATABASE station;
GRANT ALL PRIVILEGES ON DATABASE station TO postgres;

\connect postgres

CREATE TABLE visits (
    Date DATE UNIQUE,
    Enters INTEGER
);
