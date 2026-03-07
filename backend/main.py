from fastapi import FastAPI, UploadFile, File
import shutil
import os

app = FastAPI()

UPLOAD_FOLDER = "../uploads"

# create uploads folder if not exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Exam Paper Predictor API running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"{file.filename} uploaded successfully"}