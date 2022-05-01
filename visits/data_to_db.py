from logging import exception
import psycopg2
from psycopg2 import IntegrityError
import pandas as pd
import io
import os

from requests import delete


def get_csv_from_file(file_path)->pd.DataFrame:

    with open(file_path) as file:
        raw_csv = file.read()
        new_csv = raw_csv.replace('\n\"', '\n').replace('\"\n', '\n').replace(', ', ',').replace('\"', '')
        sio = io.StringIO(new_csv)

    df = pd.read_csv(sio, sep=',')
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%dT%H:%M:%S.000000Z')

    # Select only the columns of interest
    df = df[['Start Time', 'Enters']]

    return df


def insert_data(file_path):
    # Connect to database
    conn = psycopg2.connect(f'host= localhost dbname= postgres user= {os.getenv("POSTGRES_USER")} password= {os.getenv("POSTGRES_PASSWORD")}')
    cur = conn.cursor()

    tablename = "visits"

    # Build SQL code to drop table if exists and create table
    # sqlQueryCreate = f'DROP TABLE IF EXISTS {tablename};\n CREATE TABLE {tablename} (Date DATE UNIQUE,\n Enters INTEGER);'
    # cur.execute(sqlQueryCreate)

    # Get the visits data
    df = get_csv_from_file(file_path)

    # Generate query to get the data that matches the date in the csv files. a.k.a data duplicates
    vals = '\', \''.join([str(d)[:-9] for d  in df['Start Time'].tolist()])
    sqlQueryGetDuplicates = f"SELECT * FROM {tablename} WHERE Date IN ('{vals}')"
    cur.execute(sqlQueryGetDuplicates)
    # Get the output from the query
    duplicated_data = [d[0] for d in cur.fetchall()]
    # Select dataframe values that DON'T match duplicates
    df = df[df['Start Time'].isin(duplicated_data) == False]

    for index, row in df.iterrows():

        sqlQueryInsert = f'INSERT INTO {tablename}( Date, Enters) VALUES( TO_TIMESTAMP(\'{row["Start Time"]}\',\'YYYY-MM-DD\'), {row["Enters"]})'
        try:
            cur = conn.cursor()
            cur.execute(sqlQueryInsert)
            conn.commit()
            cur.close()
        except Exception as temp:
            print(f'[INFO] Duplicate instance. {row}')
            print(temp)
            cur.close()
            # raise


if __name__ == "__main__":
    try:
        insert_data("/home/antoni/hackaton/data/data_1.csv")
    except IntegrityError as err:
        pass