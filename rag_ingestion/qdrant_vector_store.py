import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables

from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, PointStruct, VectorParams

from rag_ingestion.chunker import chunk_text
from rag_ingestion.embeddings import embed_chunks
from rag_ingestion.repo_loader import load_markdown


class QdrantVectorStore:
    def __init__(self):
        import urllib.parse
        qdrant_host = os.environ.get("QDRANT_HOST")
        qdrant_api_key = os.environ.get("QDRANT_API_KEY")
        
        # Parse the URL to extract host and port for cloud instances
        if qdrant_host and qdrant_host.startswith("https://"):
            parsed_url = urllib.parse.urlparse(qdrant_host)
            # Extract host and port for cloud
            host = parsed_url.hostname
            port = parsed_url.port or 443  # Use 443 for HTTPS if no explicit port
            
            self.client = QdrantClient(
                host=host,
                port=port,
                https=True,  # Enable HTTPS for cloud
                api_key=qdrant_api_key,
                timeout=60,
            )
        else:
            # Use host for local instances
            self.client = QdrantClient(
                host=qdrant_host,
                api_key=qdrant_api_key,
                timeout=60,
            )
        self.collection_name = "book_chunks"

    def create_collection(self):
        """Recreate the collection with named vector 'embedding'."""
        from qdrant_client.http.models import VectorParams
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config={
                "embedding": VectorParams(size=1536, distance=Distance.COSINE)
            },
        )
        print(f"Qdrant collection '{self.collection_name}' created/recreated.")

    def index_book(self, docs_path: str):
        """Load markdown files, chunk text, embed, and upsert into Qdrant."""
        markdown_files = load_markdown(docs_path)
        all_points = []
        point_id = 0

        for file_path, content in markdown_files:
            chunks = chunk_text(content)
            embeddings = embed_chunks(
                chunks,
                model="text-embedding-3-small",
                api_key=os.environ.get("OPENAI_API_KEY"),
            )

            for chunk, embedding in zip(chunks, embeddings):
                all_points.append(
                    PointStruct(
                        id=point_id,
                        vector={"embedding": embedding},  # named vector
                        payload={"text": chunk, "source_file": file_path},
                    )
                )
                point_id += 1

        self.client.upsert(
            collection_name=self.collection_name, points=all_points, wait=True
        )
        print(f"Indexed {point_id} chunks from '{docs_path}' into Qdrant.")

    def search(self, query_vector, top_n=3):
        """
        Search the collection using the query embedding.
        Works with qdrant-client v1.16.1 using query_points method.
        """
        # For qdrant-client v1.16.1, use the query_points method with the proper format
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_vector,  # Pass the vector directly
            using="embedding",  # Specify which vector to use
            limit=top_n,
            with_payload=True,
            with_vectors=False,
        )
        return results.points
