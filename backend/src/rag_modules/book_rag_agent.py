from typing import Union

import os
from qdrant_client import QdrantClient
from langchain_openai import ChatOpenAI
from src.utils.embeddings import embed_chunks
from src.config.settings import settings

class BookRAGAgent:
    def __init__(self, model_name: str, qdrant_client: QdrantClient = None, llm_client: ChatOpenAI = None, collection_name: str = None):
        self.model_name = model_name
        self.collection_name = collection_name if collection_name else settings.QDRANT_COLLECTION_NAME
        self.qdrant_client = qdrant_client if qdrant_client else QdrantClient(url=settings.QDRANT_URL, api_key=settings.QDRANT_API_KEY)
        self.llm_client = llm_client if llm_client else ChatOpenAI(model_name=self.model_name, openai_api_key=settings.OPENAI_API_KEY)

    def retrieve_content(self, query: str) -> list[str]:
        # Implement Qdrant retrieval logic
        search_result = self.qdrant_client.query_points(
            collection_name=self.collection_name,
            query=embed_chunks([query])[0],
            using="embedding",
            limit=3  # Retrieve top 3 relevant chunks
        )
        return [hit.payload["text"] for hit in search_result.points if "text" in hit.payload]

    def answer_question(self, query: str, debug: bool = False) -> Union[str, dict]:
        retrieved_content = self.retrieve_content(query)

        if not retrieved_content:
            return "I cannot find the answer to your question within the provided book content."

        context = "\n\n".join(retrieved_content)
        prompt = f'''You are an AI assistant. Your primary goal is to answer the user's question SOLELY based on the provided "Retrieved Book Content".

**Strict Instructions:**
1.  **ONLY** use information present in the "Retrieved Book Content" to formulate your answer.
2.  If the answer to the user's question **cannot be found** within the "Retrieved Book Content", explicitly state: "I cannot find the answer to your question within the provided book content."
3.  **DO NOT** use any outside knowledge or prior training data.
4.  Be concise and directly address the question.

Retrieved Book Content:
{context}

User Question: {query}

Your Answer:'''

        response = self.llm_client.invoke(prompt)
        answer = response.content

        if debug:
            return {"answer": answer, "retrieved_content": retrieved_content}
        return answer
