from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import shutil
import os
from pydantic import BaseModel
from services.rag_service import upload_document, ask_document


class Question(BaseModel):
    question: str


@router.post("/query")
def query_pdf(data: Question):

    answer = ask_document(
        data.question
    )

    return {
        "answer": answer
    }
from services.rag_service import (
    upload_document,
    ask_document
)

router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)

UPLOAD_FOLDER = "uploads"


class Question(BaseModel):
    question: str


@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    message = upload_document(file_path)

    return {
        "message": message
    }


@router.post("/chat")
def chat(question: Question):

    answer = ask_document(question.question)

    return {
        "answer": answer
    }