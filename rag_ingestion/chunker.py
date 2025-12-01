from typing import List
import tiktoken

def chunk_text(text: str, min_tokens: int = 200, max_tokens: int = 300) -> List[str]:
    """
    Splits text into chunks based on token count using tiktoken.
    Attempts to keep chunks between min_tokens and max_tokens.
    """
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    chunks = []
    current_chunk_tokens = []

    for token in tokens:
        current_chunk_tokens.append(token)
        if len(current_chunk_tokens) >= min_tokens:
            chunks.append(enc.decode(current_chunk_tokens))
            current_chunk_tokens = []
        elif len(current_chunk_tokens) > max_tokens:
            # If a chunk exceeds max_tokens, force-split it
            chunks.append(enc.decode(current_chunk_tokens[:max_tokens]))
            current_chunk_tokens = current_chunk_tokens[max_tokens:]

    if current_chunk_tokens:
        chunks.append(enc.decode(current_chunk_tokens))

    return chunks
