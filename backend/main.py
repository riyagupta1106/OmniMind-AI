from fastapi import FastAPI
from api.chat import router as chat_router
from api.health import router as health_router
from api.rag import router as rag_router

app = FastAPI(
    title="OmniMind AI",
    description="Enterprise Multi-Agent AI Platform",
    version="1.0"
)


app.include_router(chat_router)
app.include_router(health_router)
app.include_router(rag_router)

@app.get("/")
def home():
    return {
        "message": "🚀 OmniMind AI Backend Running"
    }