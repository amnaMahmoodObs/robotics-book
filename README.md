# Robotics Book RAG Chatbot

This project implements a Retrieval-Augmented Generation (RAG) chatbot for a robotics book, allowing users to ask questions about robotics concepts and receive answers based on the book content.

## Architecture

The system consists of:

1. **RAG Ingestion Pipeline** (`/rag_ingestion/`): Processes book content, chunks text, generates embeddings, and stores them in a vector database
2. **Backend API** (`/backend/src/`): FastAPI-based service that handles queries, retrieves relevant content, and generates responses
3. **Frontend Interface** (`/front-end/src/theme/common/Chatbot/`): Interactive chatbot interface integrated into the Docusaurus documentation site

## How It Works

1. Book content is processed through the ingestion pipeline and stored in a Qdrant vector database
2. When a user asks a question, the system:
   - Embeds the question using OpenAI's embedding model
   - Searches the vector database for relevant content chunks
   - Constructs a prompt with the relevant content and the question
   - Uses an LLM (GPT-4.1-mini) to generate a contextual answer
3. The answer is returned to the user via the chatbot interface

## Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js 18+ (for the frontend)
- OpenAI API key
- Qdrant vector database (cloud or local instance)

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```bash
# OpenAI API Key for embeddings and language model
OPENAI_API_KEY=your_openai_api_key_here

# Qdrant Vector Database configuration
QDRANT_URL=your_qdrant_url_here
QDRANT_API_KEY=your_qdrant_api_key_here
QDRANT_COLLECTION_NAME=book_chunks

# Backend configuration
DEBUG_MODE=true

# Frontend API URL (for the RAG chat widget)
RAG_API_URL=http://localhost:8000
```

### Backend Setup

1. Install backend dependencies:

```bash
cd backend
pip install -r requirements.txt
```

2. Run the RAG ingestion to populate the vector database:

```bash
cd rag_ingestion
python run_ingestion.py
```

3. Start the backend API server:

```bash
cd backend/src
python main.py
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Install frontend dependencies:

```bash
cd front-end
npm install
```

2. Start the Docusaurus development server:

```bash
npm start
```

The website will be available at `http://localhost:3000`

## API Endpoints

- `GET /`: API information
- `POST /query`: Submit a query to the RAG system
- `GET /health`: Health check for the API
- `GET /docs`: Interactive API documentation (Swagger UI)

## Frontend Integration

The chatbot is integrated into the Docusaurus site via:

1. A React-based chatbot component that appears as a floating widget on all pages
2. A service layer for API communication
3. The component is automatically loaded via the Root.js wrapper

## Testing

Run the backend functionality test:

```bash
python3 test_rag_chatbot.py
```

Run the integration test:

```bash
python3 test_integration.py
```

## Deployment

### Backend (to Render.com)

1. Create a new web service on Render
2. Point to this repository
3. Set the environment variables in the Render dashboard
4. Use the build command: `pip install -r backend/requirements.txt`
5. Use the start command: `cd backend/src && uvicorn main:app --host 0.0.0.0 --port $PORT`

### Frontend (to Netlify/Vercel)

1. The Docusaurus site can be deployed to platforms like Netlify or Vercel
2. Set the `RAG_API_URL` environment variable to point to your deployed backend

## Troubleshooting

- If you get authentication errors, ensure your OpenAI and Qdrant API keys are correct
- If queries return no results, verify that the ingestion process completed successfully
- If the chatbot button doesn't appear, check that:
  - The Chatbot component is properly imported in Root.js
  - There are no JavaScript errors in the browser console
  - All dependencies are properly installed

## Technologies Used

- Python 3.8+
- FastAPI
- Qdrant Vector Database
- OpenAI API
- React
- Docusaurus
- Langchain