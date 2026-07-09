import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "qwen2.5:3b"


def generate_response(prompt):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }


    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload
        )


        if response.status_code == 200:
            return response.json()["response"]

        return "Model Error"


    except Exception as e:
        return f"Ollama connection failed: {e}"