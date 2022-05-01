import os
from fastapi import Depends, FastAPI, File, UploadFile, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import csv, codecs

app = FastAPI()
security = HTTPBasic()

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, 'test')
    correct_password = secrets.compare_digest(credentials.password, 'test')
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

    return {"filename": file.filename}

@app.get('/')
def index():
    return { 'message': 'Workz!' }