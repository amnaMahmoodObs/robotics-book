# Tasks for Feature: Document Ingestion and Preprocessing for RAG Agent

**Feature Branch**: `001-rag-doc-ingestion`
**Date**: 2025-11-29
**Spec**: /specs/001-rag-doc-ingestion/spec.md
**Plan**: /specs/001-rag-doc-ingestion/plan.md

## Summary

This document outlines the tasks required to implement the Python module for the RAG agent's document ingestion and preprocessing layer. Tasks are organized by user story and broken down into granular, independently executable steps.

## Implementation Strategy

The implementation will follow an iterative approach, prioritizing core ingestion and chunking functionality before moving to embedding generation. Each user story will be developed and tested independently to ensure modularity and correctness. A simple integration test script will be added to confirm successful end-to-end ingestion.

## Dependencies (User Story Completion Order)

- User Story 1 (Ingest GitHub Repository) MUST be completed before User Story 2 (Generate Embeddings).

## Parallel Execution Opportunities

- Within User Story 1, the implementation of `repo_loader.py` and `chunker.py` can be done in parallel after the initial setup.
- Unit tests for each module (`repo_loader`, `chunker`, `embeddings`) can be developed in parallel once the respective module stubs are in place.

---

## Phase 1: Setup

### Goal
Establish the basic project structure and install necessary development dependencies.

### Tasks

- [x] T001 Create the `rag_ingestion/` directory in the repository root.
- [x] T002 Create the `rag_ingestion/__init__.py` file.
- [x] T003 Create the `rag_ingestion/tests/` directory.
- [x] T004 Create the `rag_ingestion/tests/__init__.py` file.
- [x] T005 Install core Python dependencies: `GitPython`, `markdown-it-py`, `tiktoken` (or `LangChain`), `anthropic` (or `sentence-transformers`), `pytest`.

---

## Phase 2: Foundational Components (N/A for this feature - integrated into User Story phases)

---

## Phase 3: User Story 1 - Ingest GitHub Repository (Priority: P1)

### Goal
Enable the system to clone a GitHub repository, locate Markdown files, and split their content into configurable chunks.

### Independent Test
Provide a public GitHub repository URL, execute the `load_repo` and `load_markdown` functions, and then the `chunk_text` function. Verify that the repository is cloned, Markdown files are found, and content is correctly chunked into the specified token range.

### Tasks

- [x] T006 [P] [US1] Create `rag_ingestion/repo_loader.py`.
- [x] T007 [P] [US1] Implement `load_repo(repo_url: str, local_path: str) -> None` in `rag_ingestion/repo_loader.py` to clone a Git repository.
- [x] T008 [P] [US1] Implement `load_markdown(local_path: str) -> List[Tuple[str, str]]` in `rag_ingestion/repo_loader.py` to locate and read Markdown files, returning (file_path, content) tuples.
- [x] T009 [P] [US1] Create `rag_ingestion/chunker.py`.
- [x] T010 [P] [US1] Implement `chunk_text(text: str, min_tokens: int, max_tokens: int) -> List[str]` in `rag_ingestion/chunker.py` to split text into chunks (500-700 tokens).
- [x] T011 [P] [US1] Create `rag_ingestion/tests/test_repo_loader.py`.
- [x] T012 [P] [US1] Add unit tests for `load_repo` and `load_markdown` functionality in `rag_ingestion/tests/test_repo_loader.py`.
- [x] T013 [P] [US1] Create `rag_ingestion/tests/test_chunker.py`.
- [x] T014 [P] [US1] Add unit tests for `chunk_text` functionality (including edge cases like very short/long texts) in `rag_ingestion/tests/test_chunker.py`.

---

## Phase 4: User Story 2 - Generate Embeddings (Priority: P1)

### Goal
Generate vector embeddings for the processed document chunks using either Claude's embedding capabilities or another specified embedding model.

### Independent Test
Provide a list of text chunks, execute the `embed_chunks` function with a specified model, and verify that the output is a list of correctly formatted vector embeddings.

### Tasks

- [x] T015 [P] [US2] Create `rag_ingestion/embeddings.py`.
- [x] T016 [P] [US2] Implement `embed_chunks(chunks: List[str], model: str = "claude", api_key: Optional[str] = None) -> List[List[float]]` in `rag_ingestion/embeddings.py` to generate embeddings.
- [x] T017 [P] [US2] Create `rag_ingestion/tests/test_embeddings.py`.
- [x] T018 [P] [US2] Add unit tests for `embed_chunks` (including mock API responses and different model choices) in `rag_ingestion/tests/test_embeddings.py`.

---

## Phase 5: Polish & Cross-Cutting Concerns

### Goal
Ensure the module is ready for integration and confirm successful end-to-end ingestion.

### Tasks

- [x] T019 Create a simple local integration test script (e.g., `rag_ingestion/run_ingestion.py`) that uses `load_repo`, `load_markdown`, `chunk_text`, and `embed_chunks` on a test repository to confirm successful ingestion.
- [x] T020 Review and update `pyproject.toml` or `requirements.txt` in the repository root with all Python dependencies required by `rag_ingestion`.

---

## Suggested MVP Scope

The Minimum Viable Product for this feature includes completing all tasks under **Phase 1: Setup** and **Phase 3: User Story 1 - Ingest GitHub Repository**, along with the integration test `T019` to confirm successful basic ingestion and chunking without embeddings.