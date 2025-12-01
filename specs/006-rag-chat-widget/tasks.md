# Implementation Tasks: Floating RAG Chat Widget

**Feature**: Floating RAG Chat Widget that loads inside the Docusaurus book website deployed on GitHub Pages

## Dependencies

- User Story 1 (Core functionality) must be completed before User Story 2 (Enhanced experience)
- Backend API must be accessible from GitHub Pages (CORS configured) before widget integration

## Implementation Strategy

1. **MVP**: Implement basic floating chat widget that connects to the RAG API
2. **Enhancement**: Add selected text integration and refined UI
3. **Integration**: Integrate with Docusaurus and deploy to GitHub Pages
4. **Testing**: Ensure functionality across different pages and scenarios

## Parallel Execution Examples

- UI development (T010-T030) can run in parallel with API modifications (T040-T050)
- Docusaurus integration (T070-T090) can run in parallel with widget styling (T025-T026)
- Testing (T100-T110) can run after both core functionality and Docusaurus integration are complete

---

## Phase 1: Setup

- [ ] T001 Set up project structure for widget development
- [ ] T002 Review existing RAG pipeline architecture and API endpoints
- [ ] T003 Prepare development environment with necessary dependencies

## Phase 2: Foundational

- [ ] T005 [P] Update FastAPI backend to accept additional context parameters in api.py
- [ ] T006 [P] Add CORS middleware to allow requests from GitHub Pages domain in api.py
- [ ] T007 [P] Update RAG pipeline to handle selected text and context parameters in rag_pipeline.py
- [ ] T008 [P] Create JavaScript widget skeleton with basic HTML structure in rag_chat_widget.js
- [ ] T009 [P] Add essential CSS styling for floating widget in rag_chat_widget.js

## Phase 3: [US1] Access Knowledge via Chat

- [ ] T010 [US1] Implement basic widget toggle functionality (open/close) in rag_chat_widget.js
- [ ] T011 [US1] Create message display area in widget UI in rag_chat_widget.js
- [ ] T012 [US1] Implement user message input field in widget UI in rag_chat_widget.js
- [ ] T013 [US1] Add send button functionality to submit queries in rag_chat_widget.js
- [ ] T014 [US1] Implement API communication to send queries to backend in rag_chat_widget.js
- [ ] T015 [US1] Display assistant responses in chat interface in rag_chat_widget.js
- [ ] T016 [US1] Implement auto-scrolling to latest message in rag_chat_widget.js
- [ ] T017 [US1] Add loading indicators during API requests in rag_chat_widget.js
- [ ] T018 [US1] Implement basic error handling for API failures in rag_chat_widget.js
- [ ] T019 [US1] Create independent test: User can open chat widget and submit a query
- [ ] T020 [US1] Create independent test: User receives response from RAG system in chat

## Phase 4: [US2] Non-Intrusive Chat Experience

- [ ] T025 [US2] Refine widget styling for better visual integration in rag_chat_widget.js
- [ ] T026 [US2] Implement responsive design for mobile compatibility in rag_chat_widget.js
- [ ] T027 [US2] Add keyboard navigation support for accessibility in rag_chat_widget.js
- [ ] T028 [US2] Implement smooth animations for widget opening/closing in rag_chat_widget.js
- [ ] T029 [US2] Add option to position widget (bottom-left, bottom-right) in rag_chat_widget.js
- [ ] T030 [US2] Implement minimize/maximize functionality in rag_chat_widget.js
- [ ] T031 [US2] Add text selection integration functionality in rag_chat_widget.js
- [ ] T032 [US2] Create "Ask about selected text" feature in rag_chat_widget.js
- [ ] T033 [US2] Implement auto-resizing textarea for long messages in rag_chat_widget.js
- [ ] T034 [US2] Create independent test: Widget does not interfere with reading experience
- [ ] T035 [US2] Create independent test: Widget works smoothly on both desktop and mobile

## Phase 5: [US3] Backend & API Enhancement

- [ ] T040 [US3] Update API endpoint to accept selected text parameter in api.py
- [ ] T041 [US3] Update API endpoint to accept page context information in api.py
- [ ] T042 [US3] Update RAG pipeline to incorporate selected text into queries in rag_pipeline.py
- [ ] T043 [US3] Enhance response formatting to include source information in rag_pipeline.py
- [ ] T044 [US3] Add API rate limiting to handle multiple widget requests in api.py
- [ ] T045 [US3] Implement proper error responses from backend in api.py
- [ ] T046 [US3] Add logging for widget interactions in api.py
- [ ] T047 [US3] Create independent test: API properly handles context parameters

## Phase 6: [US4] Docusaurus Integration

- [ ] T070 [US4] Create Docusaurus plugin for widget integration in docusaurus-rag-widget/src/index.js
- [ ] T071 [US4] Create React component for seamless Docusaurus integration in docusaurus-rag-widget/src/rag-widget-component.js
- [ ] T072 [US4] Implement script injection method for direct HTML integration in widget_integration_instructions.md
- [ ] T073 [US4] Add widget to Docusaurus configuration in docusaurus.config.js
- [ ] T074 [US4] Test widget functionality on various Docusaurus page layouts
- [ ] T075 [US4] Add widget to all documentation pages in Docusaurus
- [ ] T076 [US4] Ensure proper loading sequence for widget initialization
- [ ] T077 [US4] Create independent test: Widget appears on all Docusaurus book pages
- [ ] T078 [US4] Create independent test: Widget functions properly in Docusaurus context

## Phase 7: [US5] Source Attribution

- [ ] T080 [US5] Implement source display in chat responses in rag_chat_widget.js
- [ ] T081 [US5] Create links to source documents from chat responses in rag_chat_widget.js
- [ ] T082 [US5] Format source information attractively in chat interface in rag_chat_widget.js
- [ ] T083 [US5] Add source relevance scores to chat responses in rag_chat_widget.js
- [ ] T084 [US5] Implement collapsible sources section in rag_chat_widget.js
- [ ] T085 [US5] Ensure source links open in new tab appropriately in rag_chat_widget.js
- [ ] T086 [US5] Create independent test: Source attribution appears with responses
- [ ] T087 [US5] Create independent test: Source links navigate to correct documentation pages

## Phase 8: Polish & Cross-Cutting Concerns

- [ ] T100 Add comprehensive error handling throughout widget in rag_chat_widget.js
- [ ] T101 Implement proper input sanitization to prevent XSS in rag_chat_widget.js
- [ ] T102 Add analytics tracking for widget usage (optional) in rag_chat_widget.js
- [ ] T103 Optimize widget JavaScript bundle size in rag_chat_widget.js
- [ ] T104 Add proper accessibility attributes (ARIA) in rag_chat_widget.js
- [ ] T105 Test widget performance across different browsers
- [ ] T106 Document widget configuration options in widget_integration_instructions.md
- [ ] T107 Create troubleshooting guide for common integration issues
- [ ] T108 Update demo HTML to showcase full functionality in demo_widget.html
- [ ] T109 Test cross-origin requests and security implications
- [ ] T110 Final testing: End-to-end functionality including all user stories