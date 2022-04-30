import csv
import psycopg2
import os
import glob


conn = psycopg2.connect("host= localhost dbname= guest user= guest password= guest")
print("Connecting to Database")


directory = "/home/antoni/hackaton/data/"

for file in os.listdir(directory):

    file_path = f"{directory}{file}"

    # Create a table name
    tablename = "visits";  # file.replace(".csv", "")
    print(tablename)

    # Open file
    fileInput = open(file_path, "r")

    # Extract first line of file
    firstLine = fileInput.readline().strip()

    # Split columns into an array [...]
    columns = firstLine.split(",")

    # Build SQL code to drop table if exists and create table
    sqlQueryCreate = 'DROP TABLE IF EXISTS ' + tablename + ";\n"
    sqlQueryCreate += 'CREATE TABLE ' + tablename + "(Start_Time DATE,\n Enters INTEGER,\n"

    valid_columns = ['Start_Time', 'Enters']
    #some loop or function according to your requiremennt
    # Define columns for table
    # for column in columns:
    #     column = column.replace(" ", "_")
    #     if column in valid_columns:
    #         sqlQueryCreate += f"{column} VARCHAR(64),\n"

    sqlQueryCreate = sqlQueryCreate[:-2]
    sqlQueryCreate += ");"

    print(sqlQueryCreate)
    cur = conn.cursor()
    cur.execute(sqlQueryCreate)
    conn.commit()
    cur.close()

    import pandas as pd
    import io
    # Create a new .csv file which removes all the quotations around the rows and values
    with open(file_path) as file:
        raw_csv = file.read()
        new_csv = raw_csv.replace('\n\"', '\n').replace('\"\n', '\n').replace(', ', ',').replace('\"', '')
        sio = io.StringIO(new_csv)

    df = pd.read_csv(sio, sep=',')
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%dT%H:%M:%S.000000Z')

    df = df[['Start Time', 'Enters']]

    df.to_csv('clean_data.csv')

    for index, row in df.iterrows():

        sqlQueryInsert = f'INSERT INTO {tablename}('
        for column in columns:
            column = column.replace(" ", "_")
            if column in valid_columns:
                sqlQueryInsert = f'{sqlQueryInsert} {column},'

        sqlQueryInsert = sqlQueryInsert[:-1]
        sqlQueryInsert = f'{sqlQueryInsert}) VALUES('

        for idx, v in enumerate(row):
            v = str(v)
            v = v.replace(" ", "_")
            if idx == 0:

                v = f'TO_TIMESTAMP(\'{v[:-9]}\',\'YYYY-MM-DD\')'

            sqlQueryInsert = f'{sqlQueryInsert} {v},'

        sqlQueryInsert = sqlQueryInsert[:-1]
        sqlQueryInsert = f'{sqlQueryInsert})'

        print(sqlQueryInsert)

        cur = conn.cursor()
        cur.execute(sqlQueryInsert)
        conn.commit()
        cur.close()
