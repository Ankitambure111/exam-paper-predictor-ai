from question_processor import clean_questions
from question_extractor import extract_questions
from fastapi import FastAPI, UploadFile, File
import shutil
import os
from pdf_reader import extract_text

app = FastAPI()

UPLOAD_FOLDER = "../uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "Exam Paper Predictor API running"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    text = extract_text(file_path)

    # Extract questions
    questions = extract_questions(text)

    # Clean questions
    questions = clean_questions(questions)

    return {
        "message": f"{file.filename} uploaded successfully",
        "total_questions": len(questions),
        "questions": questions
    }