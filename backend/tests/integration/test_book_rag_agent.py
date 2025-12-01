import pytest
from unittest.mock import MagicMock, patch
from backend.src.rag_modules.book_rag_agent import BookRAGAgent
from backend.src.config.settings import settings

@pytest.fixture
def mock_clients_for_response_test():
    with (
        patch('qdrant_client.QdrantClient') as MockQdrantClient,
        patch('langchain_openai.ChatOpenAI') as MockChatOpenAI,
    ):
        mock_qdrant = MockQdrantClient()
        mock_llm = MockChatOpenAI()
        yield mock_qdrant, mock_llm

def test_agent_response_content_limitation(mock_clients_for_response_test):
    mock_qdrant, mock_llm = mock_clients_for_response_test
    settings.QDRANT_COLLECTION_NAME = "test_collection"
    settings.OPENAI_API_KEY = "test_key"

    # Mock Qdrant to return specific content
    mock_qdrant.query.return_value = [
        MagicMock(payload={"content": "The capital of France is Paris, according to the travel guide."}),
    ]

    # Mock LLM to generate a response based on the provided context
    mock_llm.invoke.return_value = MagicMock(content="Based on the travel guide, the capital of France is Paris.")

    agent = BookRAGAgent(model_name="gpt-4.1-mini", qdrant_client=mock_qdrant, llm_client=mock_llm)
    response = agent.answer_question("What is the capital of France?")

    assert "Paris" in response
    assert "travel guide" in response # Ensure it references the source
    mock_qdrant.query.assert_called_once()
    mock_llm.invoke.assert_called_once()

def test_agent_response_no_content_found(mock_clients_for_response_test):
    mock_qdrant, mock_llm = mock_clients_for_response_test
    settings.QDRANT_COLLECTION_NAME = "test_collection"
    settings.OPENAI_API_KEY = "test_key"

    # Mock Qdrant to return no relevant content
    mock_qdrant.query.return_value = []

    # Mock LLM to state no answer found based on empty context
    mock_llm.invoke.return_value = MagicMock(content="I cannot find the answer to your question within the provided book content.")

    agent = BookRAGAgent(model_name="gpt-4.1-mini", qdrant_client=mock_qdrant, llm_client=mock_llm)
    response = agent.answer_question("What is the capital of France?")

    assert "cannot find the answer" in response
    mock_qdrant.query.assert_called_once()
