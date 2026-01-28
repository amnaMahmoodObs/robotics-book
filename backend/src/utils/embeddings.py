import os
from typing import List, Optional
from openai import OpenAI

DEFAULT_MODEL = "text-embedding-3-small"


def embed_chunks(
    chunks: List[str], model: str = DEFAULT_MODEL, api_key: Optional[str] = None
) -> List[List[float]]:
    """
    Generate embeddings for a list of text chunks using OpenAI embeddings.
    """

    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY must be provided or set as environment variable."
        )

    client = OpenAI(api_key=api_key)

    all_embeddings = []
    for chunk in chunks:
        response = client.embeddings.create(model=model, input=chunk)
        all_embeddings.append(response.data[0].embedding)

    return all_embeddings
