import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from rag_ingestion.embeddings import embed_chunks
from rag_ingestion.qdrant_vector_store import QdrantVectorStore

if __name__ == "__main__":
    # --- Ensure required environment variables ---
    required_env = ["QDRANT_HOST", "QDRANT_API_KEY", "OPENAI_API_KEY"]
    missing = [var for var in required_env if not os.environ.get(var)]
    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        exit(1)

    # --- Initialize Qdrant ---
    qdrant_store = QdrantVectorStore()
    qdrant_store.create_collection()

    # --- Index book content ---
    docs_path = "front-end/docs/"
    print(f"Indexing book content from '{docs_path}'...")
    qdrant_store.index_book(docs_path)

    # --- Search validation ---
    search_query = "What is robotics?"
    print(f"\nSearching for: '{search_query}'")

    query_embedding = embed_chunks([search_query])[0]
    search_results = qdrant_store.search(query_embedding, top_n=3)

    print("\nSearch Results:")
    for i, hit in enumerate(search_results):
        print(f"Result {i + 1} (Score: {hit.score:.4f})")
        print(f"Source: {hit.payload['source_file']}")
        print(f"Content: {hit.payload['text'][:200]}...")
