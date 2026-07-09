from fastapi import APIRouter
from pydantic import BaseModel

from services.ollama_service import generate_response


router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"]
)


class ChatRequest(BaseModel):
    message:str



@router.post("/")
def chat(request:ChatRequest):

    answer = generate_response(
        request.message
    )


    return {
        "user": request.message,
        "assistant": answer
    }