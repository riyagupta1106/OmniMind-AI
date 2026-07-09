from collections import deque

conversation_memory = deque(maxlen=20)


def add_message(role: str, content: str):
    conversation_memory.append(
        {
            "role": role,
            "content": content
        }
    )


def get_memory():
    return list(conversation_memory)


def clear_memory():
    conversation_memory.clear()