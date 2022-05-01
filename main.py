import os
from fastapi import Depends, FastAPI, File, UploadFile, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import csv
import codecs
from data_to_db import insert_data

app = FastAPI()
security = HTTPBasic()


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, os.getenv("API_USER"))
    correct_password = secrets.compare_digest(credentials.password, os.getenv("API_PASS"))
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email/username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.post("/uploadfile/")
def upload_visits_file(file: UploadFile = File(...), username: str = Depends(authenticate)):
    data = file.file

    csv_reader = csv.reader(codecs.iterdecode(data, 'utf-8'), delimiter=',')

    with open('visits_data/' + file.filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in csv_reader:
            writer.writerow(row)

    try:
        insert_data('visits_data/' + file.filename)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Inserting duplicate data"
        )

    return {"filename": file.filename}


@app.get('/')
def index():
    return { 'message': 'Workz!' }