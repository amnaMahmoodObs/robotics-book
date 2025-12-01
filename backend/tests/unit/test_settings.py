import os
import pytest
from backend.src.config.settings import Settings


def test_settings_loading():
    settings = Settings()
    assert settings.OPENAI_API_KEY == "test_openai_key"
    assert settings.QDRANT_URL == "http://test-qdrant:6333"
    assert settings.QDRANT_API_KEY == "test_qdrant_key"
    assert settings.QDRANT_COLLECTION_NAME == "test_collection"
