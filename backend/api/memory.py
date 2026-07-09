from fastapi import APIRouter

from memory.memory import (
    get_memory,
    clear_memory
)

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)


@router.get("/")
def memory():

    return get_memory()


@router.delete("/")
def clear():

    clear_memory()

    return {
        "message": "Memory Cleared"
    }