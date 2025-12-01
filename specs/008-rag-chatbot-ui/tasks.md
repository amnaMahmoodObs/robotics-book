# Feature Tasks: Integrate FastAPI RAG Chatbot UI

**Branch**: `008-rag-chatbot-ui` | **Date**: 2025-12-01 | **Spec**: [specs/008-rag-chatbot-ui/spec.md](specs/008-rag-chatbot-ui/spec.md) | **Plan**: [specs/008-rag-chatbot-ui/plan.md](specs/008-rag-chatbot-ui/plan.md)

## Summary

This document outlines the detailed implementation tasks for integrating the FastAPI RAG backend into the Docusaurus website with an interactive chatbot UI, supporting both direct and text-selection based queries.

## Tasks

### Task 1: Create React Chat Component in Docusaurus

- **ID**: TSK-001
- **Description**: Develop the core React component for the chatbot UI within the Docusaurus theme override system (`src/theme/common/Chatbot/`). This component will encapsulate the chat interface, including message display and input area.
- **Acceptance Criteria**:
    - [ ] A new React component `src/theme/common/Chatbot/index.js` exists and can be rendered within Docusaurus.
    - [ ] The component displays a basic chat interface (e.g., a static header and a placeholder for messages and input).
    - [ ] The component does not introduce any build errors or warnings in the Docusaurus project.
- **Dependencies**: None
- **Time Estimate**: N/A
- **Effort Estimate**: N/A
- **Assigned**: N/A
- **Status**: Pending

---

### Task 2: Add UI Trigger to Open and Close Chat Interface

- **ID**: TSK-002
- **Description**: Implement a floating button or icon (e.g., a chat bubble) that appears consistently across Docusaurus pages. Clicking this trigger should toggle the visibility of the chatbot UI.
- **Acceptance Criteria**:
    - [ ] A clickable trigger element is visible on all Docusaurus pages.
    - [ ] Clicking the trigger opens the chatbot UI if it's closed, and closes it if it's open.
    - [ ] The chatbot UI's visibility state is managed correctly (e.g., using React state).
    - [ ] The trigger and chatbot UI are styled appropriately and do not break Docusaurus's existing layout.
- **Dependencies**: TSK-001 (core chat component)
- **Time Estimate**: N/A
- **Effort Estimate**: N/A
- **Assigned**: N/A
- **Status**: Pending

---

### Task 3: Implement Function to Call FastAPI RAG Query Endpoint

- **ID**: TSK-003
- **Description**: Create a JavaScript/TypeScript service or utility (`src/theme/common/Chatbot/ChatService.js`) responsible for making API calls to the FastAPI RAG backend's POST query endpoint. This function should accept a query string and optionally selected text as parameters.
- **Acceptance Criteria**:
    - [ ] A `ChatService.js` file exists within the chatbot directory.
    - [ ] The service contains a function (e.g., `queryRAGBackend`) that sends a POST request to the configured FastAPI endpoint.
    - [ ] The function correctly includes `query` and optionally `selected_text` in the request body.
    - [ ] The function handles API responses and potential errors (e.g., network issues, backend errors).
    - [ ] No sensitive information (API keys) are hardcoded in the frontend.
- **Dependencies**: None (can be developed in parallel with UI, but UI needs it to function)
- **Time Estimate**: N/A
- **Effort Estimate**: N/A
- **Assigned**: N/A
- **Status**: Pending

---

### Task 4: Implement Logic to Read Selected Text from Document

- **ID**: TSK-004
- **Description**: Develop JavaScript logic to detect and capture text highlighted by the user within the Docusaurus page content. This logic should be able to retrieve the exact selected string.
- **Acceptance Criteria**:
    - [ ] A utility function (e.g., `getSelectedText()`) exists that returns the currently highlighted text as a string.
    - [ ] The function correctly handles cases where no text is selected (returns an empty string or null).
    - [ ] The function is integrated into the Docusaurus page/layout where text selection is relevant.
- **Dependencies**: TSK-002 (requires a way to trigger the selection query, or at least the chat UI to be present to display the option)
- **Time Estimate**: N/A
- **Effort Estimate**: N/A
- **Assigned**: N/A
- **Status**: Pending

---

### Task 5: Allow User to Send Normal and Selection-Based Queries

- **ID**: TSK-005
- **Description**: Integrate the query sending functionality into the chatbot UI. This includes allowing users to type and submit questions (normal queries) and adding an option to send the currently selected text as a contextual query.
- **Acceptance Criteria**:
    - [ ] The chatbot input field allows users to type and submit questions.
    - [ ] Submitting a question triggers `TSK-003` to send the query to the backend.
    - [ ] An interface element (e.g., a button, context menu option) is available to initiate a query with selected text.
    - [ ] When the selection-based query is triggered, `TSK-004` is used to get the text, and `TSK-003` is called with both the user's question (if any) and the selected text.
- **Dependencies**: TSK-001 (chat component), TSK-003 (API service), TSK-004 (text selection logic)
- **Time Estimate**: N/A
- **Effort Estimate**: N/A
- **Assigned**: N/A
- **Status**: Pending

---

### Task 6: Render Backend Response within Chat Component UI

- **ID**: TSK-006
- **Description**: Update the chatbot UI to display responses received from the FastAPI RAG backend. This involves updating the message display area with the agent's answers, associating them with the user's questions.
- **Acceptance Criteria**:
    - [ ] Responses from the backend (via `TSK-003`) are parsed and displayed clearly within the chat window.
    - [ ] Each response is visually associated with the corresponding user query.
    - [ ] The chat window is scrollable if content exceeds its visible area.
    - [ ] Loading indicators are displayed while waiting for a backend response.
- **Dependencies**: TSK-001 (chat component), TSK-003 (API service), TSK-005 (query sending)
- **Time Estimate**: N/A
- **Effort Estimate**: N/A
- **Assigned**: N/A
- **Status**: Pending

---

### Task 7: Test Both Normal and Selection-Based Queries

- **ID**: TSK-007
- **Description**: Manually and/or automatically test the full integration to ensure both normal text queries and queries augmented with selected text function correctly with the FastAPI RAG backend.
- **Acceptance Criteria**:
    - [ ] A normal text query successfully sends to the backend and displays a relevant response.
    - [ ] Selecting text on a Docusaurus page and initiating a query successfully sends the selected text as context to the backend.
    - [ ] The backend responds with answers that are demonstrably contextual to the selected text.
    - [ ] Error handling (e.g., backend unreachable) is tested and displays appropriate messages.
    - [ ] All UI interactions (opening/closing chat, typing, submitting) are smooth and responsive.
- **Dependencies**: TSK-001, TSK-002, TSK-003, TSK-004, TSK-005, TSK-006 (all preceding tasks)
- **Time Estimate**: N/A
- **Effort Estimate**: N/A
- **Assigned**: N/A
- **Status**: Pending

