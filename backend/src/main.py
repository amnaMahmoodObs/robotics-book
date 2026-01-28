from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Dict, Any
import logging

from src.config.settings import settings
from src.rag_modules.book_rag_agent import BookRAGAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Robotics Book RAG API", version="1.0.0")

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://amnaMahmoodObs.github.io",
        "https://amnamahmoodobs.github.io",
        "https://robotics-book-mu.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the RAG agent
try:
    agent = BookRAGAgent(model_name="gpt-4.1-mini")
    logger.info("BookRAG Agent initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize BookRAG Agent: {e}")
    raise

# Pydantic models for request/response
class QueryRequest(BaseModel):
    query: str
    selected_text: Optional[str] = None
    debug: Optional[bool] = False

class QueryResponse(BaseModel):
    answer: str
    retrieved_content: Optional[list] = None

class HealthResponse(BaseModel):
    status: str
    openai_api_key_loaded: bool
    qdrant_url_loaded: bool

@app.post("/query", response_model=QueryResponse)
async def query_agent(request: QueryRequest):
    """
    Process a user query against the robotics book content using RAG.

    Args:
        request (QueryRequest): The query request containing the user's question
                               and optional selected text for context

    Returns:
        QueryResponse: The answer and optionally retrieved content if in debug mode
    """
    try:
        # If selected text is provided, prepend it to the query to give more context
        search_query = request.query
        if request.selected_text:
            search_query = f"Context: {request.selected_text}\n\nQuestion: {request.query}"

        response = agent.answer_question(search_query, debug=request.debug)

        # Format response based on debug mode
        if request.debug and isinstance(response, dict):
            return QueryResponse(
                answer=response.get("answer", ""),
                retrieved_content=response.get("retrieved_content", [])
            )
        else:
            # If response is a dict but not in debug mode, extract just the answer
            if isinstance(response, dict):
                answer = response.get("answer", str(response))
            else:
                answer = response
            return QueryResponse(answer=answer, retrieved_content=None)

    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Health check endpoint to verify the API and its dependencies are working.

    Returns:
        HealthResponse: Status of the API and its key dependencies
    """
    return HealthResponse(
        status="ok",
        openai_api_key_loaded=bool(settings.OPENAI_API_KEY),
        qdrant_url_loaded=bool(settings.QDRANT_URL)
    )

@app.get("/")
async def root():
    """
    Root endpoint providing API information.
    """
    return {
        "message": "Welcome to the Robotics Book RAG API",
        "endpoints": {
            "POST /query": "Submit a query to the RAG system",
            "GET /health": "Health check for the API",
            "GET /docs": "Interactive API documentation"
        }
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting RAG API server...")
    uvicorn.run(app, host="0.0.0.0", port=8000)