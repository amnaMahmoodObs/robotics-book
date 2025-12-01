# Implementation Plan: Document Ingestion and Preprocessing for RAG Agent

**Branch**: `001-rag-doc-ingestion` | **Date**: 2025-11-29 | **Spec**: /specs/001-rag-doc-ingestion/spec.md
**Input**: Feature specification from `/specs/001-rag-doc-ingestion/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implement a Python module for the RAG agent's document ingestion and preprocessing layer. This includes utilities for cloning GitHub repositories, locating and reading Markdown files, splitting their content into configurable chunks, and generating embeddings for these chunks using either Claude's capabilities or a specified embedding model. The module will be designed for reusability and modularity.

## Technical Context

**Language/Version**: Python 3.9+ (aligned with common development practices for AI/ML projects)
**Primary Dependencies**:
- Git (CLI tool) for repository cloning.
- `GitPython` or similar library for programmatic Git operations.
- `markdown-it-py` or similar for robust Markdown parsing.
- `tiktoken` or `LangChain` text splitters for efficient and configurable text chunking (500-700 tokens).
- `anthropic` client for Claude embedding generation, or other embedding model SDK (e.g., `sentence-transformers`).
**Storage**: Local filesystem for cloned repositories (temporary) and for saving processed chunks/embeddings during development/testing. Final embedding storage is external to this module's scope.
**Testing**: `pytest` for unit and integration tests.
**Target Platform**: Any environment supporting Python 3.9+ and Git (e.g., Linux, macOS, Windows via WSL).
**Project Type**: Python library/module.
**Performance Goals**:
- **SC-001**: The Python module can successfully clone a GitHub repository and process its Markdown files into chunks within 5 minutes for a repository of 100 Markdown files averaging 10KB each.
- **SC-002**: The embedding generation utility successfully processes 99% of document chunks into embeddings without error.
**Constraints**:
- Initial focus on public GitHub repositories.
- Adherence to standard Markdown syntax.
- Configurable chunk size between 500-700 tokens.
- Handling of rate limits for external API calls (e.g., Claude embeddings).
**Scale/Scope**: The module provides the core ingestion and preprocessing utilities; it does not cover the full RAG system (e.g., vector database integration, retrieval logic).

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **I. Chapter-Driven Content Generation**: N/A - This principle applies to book content generation, not the RAG agent's backend.
- **II. Modular Architecture for RAG Chatbot**: Passed - The plan emphasizes creating a modular Python module as a core component of the RAG backend, aligning with using FastAPI, Qdrant, and Neon for the broader RAG architecture.
- **III. Reusability and Subagent Leverage**: Passed - The module is designed to provide reusable utilities for document ingestion and preprocessing, which can be leveraged by various parts of the RAG agent or other subagents.
- **IV. Deployment and Accessibility**: N/A - This principle relates to the book's deployment, not the RAG agent's backend components.
- **V. Incremental Development**: Passed - The development of this module is an incremental step towards the larger RAG agent feature.

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-doc-ingestion/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command - not generated for this feature due to clear initial prompt)
├── data-model.md        # Phase 1 output (/sp.plan command - not generated, entities are defined in spec.md)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command - not generated, no external APIs defined by this module)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
rag_ingestion/
├── __init__.py
├── repo_loader.py         # Handles cloning and Markdown loading
├── chunker.py             # Handles text splitting (500-700 token chunks)
├── embeddings.py          # Handles embedding generation (Claude/other model wrapper)
└── tests/
    ├── __init__.py
    ├── test_repo_loader.py
    ├── test_chunker.py
    └── test_embeddings.py
```

**Structure Decision**: The selected structure creates a dedicated `rag_ingestion` Python package with distinct modules for each core utility: repository loading, text chunking, and embedding generation. A `tests` sub-directory provides a clear separation for unit and integration tests for each component.

## Complexity Tracking

> **Not applicable - no Constitution Check violations that require justification.**