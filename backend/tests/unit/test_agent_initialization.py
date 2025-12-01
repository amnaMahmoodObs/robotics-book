import pytest
from unittest.mock import MagicMock, patch
from backend.src.rag_modules.book_rag_agent import BookRAGAgent

def test_agent_initialization():
    # Test agent initialization with a specific model
    agent = BookRAGAgent(model_name="gpt-4.1-mini")
    assert agent.model_name == "gpt-4.1-mini"
    assert agent.qdrant_client is not None # Clients are initialized by default
    assert agent.llm_client is not None # Clients are initialized by default

@patch('backend.src.rag_modules.book_rag_agent.QdrantClient')
@patch('backend.src.rag_modules.book_rag_agent.ChatOpenAI')
def test_agent_initialization_with_clients(MockChatOpenAI, MockQdrantClient):
    # Test agent initialization when clients are provided
    mock_qdrant_client = MockQdrantClient()
    mock_llm_client = MockChatOpenAI()
    agent = BookRAGAgent(model_name="gpt-4.1-mini", qdrant_client=mock_qdrant_client, llm_client=mock_llm_client)
    assert agent.model_name == "gpt-4.1-mini"
    assert agent.qdrant_client == mock_qdrant_client
    assert agent.llm_client == mock_llm_client
