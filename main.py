from fastapi import FastAPI, File, UploadFile
import csv, codecs

app = FastAPI()

@app.post("/uploadfile/")
def upload_visits_file(file: UploadFile = File(...)):
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