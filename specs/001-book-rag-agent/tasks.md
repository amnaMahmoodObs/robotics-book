# Tasks: BookRAGAgent

**Input**: Design documents from `/specs/001-book-rag-agent/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: The spec requests verification of agent responses, so testing is implicitly required.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `backend/tests/`

---

## Phase 3: User Story 1 - Ask a question about book content (Priority: P1) 🎯 MVP

**Goal**: Implement the core BookRAGAgent to answer user questions based on book content.

**Independent Test**: The agent provides correct and relevant answers, citing only information from the book content, when given book-related questions.

### Tests for User Story 1

- [x] T001 [US1] Write a unit test for agent initialization and model configuration in `backend/tests/unit/test_agent_initialization.py`
- [x] T002 [US1] Write an integration test for Qdrant retrieval in `backend/tests/integration/test_qdrant_retrieval.py`
- [x] T003 [US1] Write an integration test for agent's response generation (content limitation) in `backend/tests/integration/test_book_rag_agent.py`

### Implementation for User Story 1

- [x] T004 [US1] Create `backend/src/rag_modules/book_rag_agent.py` and define the agent class, initializing it with the `gpt-4.1-mini` model.
- [ ] T005 [US1] Implement a method within the agent class in `backend/src/rag_modules/book_rag_agent.py` to query Qdrant for relevant book chunks.
- [ ] T006 [US1] Configure the agent's internal instructions in `backend/src/rag_modules/book_rag_agent.py` to strictly use retrieved content for answers and explicitly state when an answer is not found in the book.
- [ ] T007 [US1] Integrate the agent into `backend/src/main.py` with an API endpoint for user queries.

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Refinements and validation after core implementation.

- [ ] T008 Adjust Qdrant retrieval parameters or agent instructions in `backend/src/rag_modules/book_rag_agent.py` if test queries reveal deviations from book content or suboptimal answers.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1 - existing)**: Completed by previous feature.
- **Foundational (Phase 2 - existing)**: Completed by previous feature.
- **User Stories (Phase 3+)**: All depend on Foundational phase completion.
  - User Story 1 can proceed after Foundational.
- **Polish (Final Phase)**: Depends on User Story 1 completion.

### Within Each User Story

- Tests MUST be written and FAIL before implementation of their corresponding functionality.
- Agent definition before retrieval tool implementation.
- Retrieval tool before agent instructions.
- Core agent implementation before API integration.

### Parallel Opportunities

- Unit and integration tests can be developed in parallel (T001, T002, T003).
