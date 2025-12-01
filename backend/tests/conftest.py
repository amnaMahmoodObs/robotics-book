import pytest
import os
from unittest.mock import patch

@pytest.fixture(scope="session", autouse=True)
def set_test_environment_variables():
    # Use patch.dict to temporarily set environment variables for the entire test session
    # This ensures they are set before any module-level imports that might rely on them
    with patch.dict(os.environ, {
        "OPENAI_API_KEY": "test_openai_key",
        "QDRANT_URL": "http://test-qdrant:6333",
        "QDRANT_API_KEY": "test_qdrant_key",
        "QDRANT_COLLECTION_NAME": "test_collection",
    }):
        yield
