from services.ollama_service import generate_response
from memory.memory import add_message

def chat(prompt: str):

    add_message("user", prompt)

    response = generate_response(prompt)

    add_message("assistant", response)

    return response