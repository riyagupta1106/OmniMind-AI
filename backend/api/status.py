from fastapi import APIRouter

from services.ollama_service import is_ollama_running

router = APIRouter(
    prefix="/status",
    tags=["Status"]
)


@router.get("/")
def status():

    return {
        "backend": "Running",
        "ollama": is_ollama_running()
    }