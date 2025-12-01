import pytest
from rag_ingestion.chunker import chunk_text

def test_chunk_text_basic_chunking():
    text = "This is a sample sentence for chunking. " * 50  # ~300 tokens
    chunks = chunk_text(text, min_tokens=50, max_tokens=100)
    # We expect multiple chunks, each roughly within 50-100 tokens
    assert len(chunks) > 1
    for chunk in chunks:
        enc = tiktoken.encoding_for_model("cl100k_base")
        num_tokens = len(enc.encode(chunk))
        assert 50 <= num_tokens <= 100 or len(chunks) == 1 # A single chunk might be smaller than min_tokens if the entire text is small

def test_chunk_text_small_text_one_chunk():
    text = "Short text." # ~2 tokens
    chunks = chunk_text(text, min_tokens=50, max_tokens=100)
    assert len(chunks) == 1
    assert chunks[0] == text

def test_chunk_text_empty_text():
    text = ""
    chunks = chunk_text(text)
    assert len(chunks) == 1  # tiktoken encodes empty string as one token
    assert chunks[0] == ""

def test_chunk_text_exact_max_tokens():
    # This test might be tricky to get exact due to tiktoken's internal logic,
    # but we can aim for a chunk that's very close to max_tokens.
    text = "word " * 600  # ~600 tokens
    chunks = chunk_text(text, min_tokens=500, max_tokens=600)
    assert len(chunks) >= 1
    enc = tiktoken.encoding_for_model("cl100k_base")
    num_tokens = len(enc.encode(chunks[0]))
    assert num_tokens <= 600

def test_chunk_text_force_split_over_max_tokens():
    # Create a very long single word or a sequence that tiktoken doesn't split easily
    # For simplicity, let's create a text that would result in a chunk > max_tokens if not split
    long_word = "a" * 1000  # A very long word
    text = long_word * 2 # two such long words to test splitting
    chunks = chunk_text(text, min_tokens=100, max_tokens=200)

    # Expect multiple chunks, none exceeding max_tokens significantly
    assert len(chunks) > 1
    enc = tiktoken.encoding_for_model("cl100k_base")
    for chunk in chunks:
        num_tokens = len(enc.encode(chunk))
        assert num_tokens <= 200 or len(chunks) == 1 # If the whole text is one chunk it can be larger

def test_chunk_text_with_different_min_max():
    text = "The quick brown fox jumps over the lazy dog. " * 100
    chunks = chunk_text(text, min_tokens=100, max_tokens=150)
    assert len(chunks) > 1
    enc = tiktoken.encoding_for_model("cl100k_base")
    for chunk in chunks:
        num_tokens = len(enc.encode(chunk))
        assert 100 <= num_tokens <= 150 or len(chunks) == 1
