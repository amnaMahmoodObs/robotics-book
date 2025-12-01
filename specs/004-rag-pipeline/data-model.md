# Data Model: RAG Pipeline Implementation

## Entities

### Query
- **Fields**:
  - query_text (string, required): The user's input question
  - query_embedding (array[float], required): The vector representation of the query
  - timestamp (datetime, required): When the query was submitted
  - user_id (string, optional): Identifier for the user (if implemented later)

- **Validation Rules**:
  - query_text must be 1-1000 characters
  - query_embedding must be exactly 1536 elements (for text-embedding-3-small model)

### DocumentChunk
- **Fields**:
  - id (string, required): Unique identifier for the chunk
  - text (string, required): The content of the document chunk
  - source_file (string, required): The original source document
  - embedding (array[float], required): The vector representation of the chunk
  - metadata (object, optional): Additional metadata about the chunk

- **Validation Rules**:
  - text must be 1-5000 characters
  - embedding must be exactly 1536 elements (for text-embedding-3-small model)
  - source_file must be a valid path

### RetrievedContext
- **Fields**:
  - query (string, required): The original user query
  - document_chunks (array[DocumentChunk], required): Retrieved relevant chunks
  - scores (array[float], required): Relevance scores for each chunk
  - packed_context (string, required): The final context string for the language model
  - total_tokens (integer, required): Estimated token count of packed context

- **Validation Rules**:
  - packed_context must not exceed model context limits (typically 8000 tokens)
  - document_chunks must contain 1-20 chunks
  - scores must match the length of document_chunks

### GeneratedResponse
- **Fields**:
  - query (string, required): The original user query
  - response_text (string, required): The generated response
  - source_chunks (array[string], required): IDs of the chunks used to generate the response
  - confidence_score (float, optional): Estimated confidence in the response
  - timestamp (datetime, required): When the response was generated

- **Validation Rules**:
  - response_text must be 1-20000 characters
  - confidence_score must be between 0 and 1 if provided