import pytest
from unittest.mock import MagicMock, patch
from backend.src.rag_modules.book_rag_agent import BookRAGAgent

@pytest.fixture
def mock_qdrant_client():
    with (
        patch('qdrant_client.QdrantClient') as MockQdrantClient,
    ):
        mock_client = MockQdrantClient()
        mock_client.query.return_value = [
            MagicMock(payload={"content": "This is a chunk about robotics."}),
            MagicMock(payload={"content": "Another chunk detailing AI applications."}),
        ]
        yield mock_client

def test_qdrant_retrieval_tool(mock_qdrant_client):
    agent = BookRAGAgent(model_name="test-model", qdrant_client=mock_qdrant_client, collection_name="test_collection")
    query_text = "What is robotics?"
    retrieved_chunks = agent.retrieve_content(query_text)

    assert len(retrieved_chunks) == 2
    assert "robotics" in retrieved_chunks[0].lower()
    assert "ai applications" in retrieved_chunks[1].lower()
    mock_qdrant_client.query.assert_called_once() # Verify QdrantClient.query was called
