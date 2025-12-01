from fastapi import FastAPI
from backend.src.config.settings import settings
from backend.src.rag_modules.book_rag_agent import BookRAGAgent

app = FastAPI()

agent = BookRAGAgent(model_name="gpt-4.1-mini")

@app.post("/query")
async def query_agent(user_query: dict):
    response = agent.answer_question(user_query["query"], debug=settings.DEBUG_MODE)
    if settings.DEBUG_MODE and isinstance(response, dict):
        return response
    return {"answer": response}

@app.get("/health")
async def health_check():
    return {"status": "ok", "openai_api_key_loaded": bool(settings.OPENAI_API_KEY), "qdrant_url_loaded": bool(settings.QDRANT_URL)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)