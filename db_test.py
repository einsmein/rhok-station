import psycopg2
import pandas as pd
import io

from requests import delete


def get_csv_from_file(file_path: str)->pd.DataFrame:

    with open(file_path) as file:
        raw_csv = file.read()
        new_csv = raw_csv.replace('\n\"', '\n').replace('\"\n', '\n').replace(', ', ',').replace('\"', '')
        sio = io.StringIO(new_csv)

    df = pd.read_csv(sio, sep=',')
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%dT%H:%M:%S.000000Z')

    # Select only the columns of interest
    df = df[['Start Time', 'Enters']]

    return df


def get_csv_data()->pd.DataFrame:

    return get_csv_from_file("/home/antoni/hackaton/data/data_3.csv")


def main():
    # Connect to database
    conn = psycopg2.connect("host= localhost dbname= guest user= guest password= guest")
    cur = conn.cursor()

    tablename = "visits"

    # # Build SQL code to drop table if exists and create table
    # sqlQueryCreate = f'DROP TABLE IF EXISTS {tablename};\n CREATE TABLE {tablename} (Date DATE UNIQUE,\n Enters INTEGER);'
    # cur.execute(sqlQueryCreate)

    # Get the visits data
    df = get_csv_data()

    for index, row in df.iterrows():
        sqlQueryInsert = f'INSERT INTO {tablename}( Date, Enters) VALUES( TO_TIMESTAMP(\'{row["Start Time"]}\',\'YYYY-MM-DD\'), {row["Enters"]})'
        try:
            cur.execute(sqlQueryInsert)
        except:
            print('[INFO] Duplicate instance.')

    # Save changes and close connection
    conn.commit()
    cur.close()


if __name__ == "__main__":
    main()