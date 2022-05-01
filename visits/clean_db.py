from logging import exception
import psycopg2
from psycopg2 import IntegrityError
import pandas as pd
import io
import os

from requests import delete

if __name__ == "__main__":
    # Connect to database
    conn = psycopg2.connect(f'host= localhost dbname= postgres user= {os.getenv("POSTGRES_USER")} password= {os.getenv("POSTGRES_PASSWORD")}')
    cur = conn.cursor()

    tablename = "visits"

    # Build SQL code to drop table if exists and create table
    sqlQueryCreate = f'DROP TABLE IF EXISTS {tablename};\n CREATE TABLE {tablename} (Date DATE UNIQUE,\n Enters INTEGER);'
    cur.execute(sqlQueryCreate)

    conn.commit()
    cur.close()