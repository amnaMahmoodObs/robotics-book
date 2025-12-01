import os
from unittest.mock import patch, MagicMock
import pytest
from rag_ingestion.embeddings import embed_chunks

# Mocking anthropic client for Claude embedding calls
@pytest.fixture
def mock_anthropic_client():
    with patch('anthropic.Anthropic') as mock_client_class:
        mock_client = MagicMock()
        # Configure the mock to return a predictable mock embedding
        # for our internal _get_mock_embedding logic, as the actual Claude API
        # doesn't have a direct embedding endpoint in the current SDK.
        # Our `embed_chunks` will call _get_mock_embedding, so we don't need to mock
        # a chat completion response here directly.
        yield mock_client

# Helper for generating a mock embedding, matching the internal logic in embeddings.py
def _generate_expected_mock_embedding(text: str) -> List[float]:
    return [float(ord(c)) for c in text[:16]] + [0.0] * (1536 - len(text[:16]))

def test_embed_chunks_claude_success(mock_anthropic_client):
    chunks = ["hello world", "test chunk"]
    # We are mocking the Anthropic client itself, but our `embed_chunks` function
    # currently calls an internal mock embedding function for 'claude' model.
    # So, we test against that internal mock's expected output.
    embeddings = embed_chunks(chunks, model="claude", api_key="dummy_key")

    assert len(embeddings) == len(chunks)
    assert all(isinstance(e, list) and len(e) == 1536 for e in embeddings) # Assuming 1536 dim for mock
    assert embeddings[0] == _generate_expected_mock_embedding("hello world")
    assert embeddings[1] == _generate_expected_mock_embedding("test chunk")

def test_embed_chunks_claude_no_api_key_raises_error():
    chunks = ["test"]
    with pytest.raises(ValueError, match="ANTHROPIC_API_KEY must be provided or set as environment variable for Claude embeddings."):
        embed_chunks(chunks, model="claude", api_key=None) # Explicitly pass None

@patch.dict(os.environ, {"ANTHROPIC_API_KEY": "env_key"})
def test_embed_chunks_claude_api_key_from_env(mock_anthropic_client):
    chunks = ["env test"]
    embeddings = embed_chunks(chunks, model="claude") # api_key is None, should pick from env
    assert len(embeddings) == len(chunks)
    assert embeddings[0] == _generate_expected_mock_embedding("env test")

def test_embed_chunks_mock_model():
    chunks = ["mocking works", "another mock"]
    embeddings = embed_chunks(chunks, model="mock")

    assert len(embeddings) == len(chunks)
    assert all(isinstance(e, list) and len(e) == 1536 for e in embeddings)
    assert embeddings[0] == _generate_expected_mock_embedding("mocking works")
    assert embeddings[1] == _generate_expected_mock_embedding("another mock")

def test_embed_chunks_unsupported_model():
    chunks = ["unsupported"]
    with pytest.raises(ValueError, match="Unsupported embedding model: unknown_model"):
        embed_chunks(chunks, model="unknown_model")
