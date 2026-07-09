from fastapi import APIRouter

from memory.memory import get_memory

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/")
def history():
    return {
        "messages": get_memory()
    }