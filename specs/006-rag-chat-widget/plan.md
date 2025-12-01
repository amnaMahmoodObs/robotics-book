# Implementation Plan: Floating RAG Chat Widget

## Technical Context

- **Problem Domain**: Create a floating chat widget for the Docusaurus-based robotics book that allows users to ask questions and get answers powered by the RAG pipeline.
- **Current State**: The RAG pipeline with semantic search in Qdrant and response generation is already implemented and tested.
- **Target Architecture**: A lightweight JavaScript widget that embeds in Docusaurus pages and communicates with the existing FastAPI backend.
- **Known Dependencies**:
  - Existing RAG pipeline and FastAPI endpoint at `/ask`
  - Qdrant vector database with robotics book embeddings
  - OpenAI API for embeddings
  - Docusaurus website deployed on GitHub Pages

## Constitution Check

[NEEDS CLARIFICATION: What are the specific principles from constitution.md that apply to UI components and JavaScript implementation?]

## Gates

- [ ] Architecture: Does the design align with project principles in constitution.md?
- [ ] Performance: Will the widget load quickly and not impact page performance?
- [ ] Security: Are API keys and user data handled securely in the frontend?
- [ ] Accessibility: Does the widget meet accessibility standards?

## Phase 0: Research

### Completed Research

1. **Widget Implementation Research**: Researched best practices for lightweight JavaScript widgets. Decided on a self-contained JavaScript approach with all HTML, CSS, and JavaScript in a single file for easy embedding.

2. **Selected Text Integration**: Researched browser Selection API for capturing selected text. This provides reliable access to user-selected text to incorporate into queries.

3. **Docusaurus Integration**: Researched integration approaches. Will implement via script injection that can be added globally to all Docusaurus pages.

4. **Frontend Communication**: Researched communication methods. Will use browser's fetch API to communicate with the backend, requiring CORS configuration.

## Phase 1: Design

### Data Model
Completed - see [data-model.md](./data-model.md)

Key entities include:
- ChatMessage: Represents messages in the conversation
- ChatSession: Represents a user's conversation context
- UserQuery: Represents a query from the widget with additional context
- WidgetConfig: Configuration options for the widget

### API Contracts
Completed - see [contracts/widget-api.yaml](./contracts/widget-api.yaml)

The API extends the existing /ask endpoint to include additional context from the widget.

## Phase 2: Implementation Strategy

### Implementation Tasks

1. **Create Lightweight JS Widget**: Implement a self-contained JavaScript widget that can be added to any page.
   - Develop HTML structure for the chat interface
   - Implement CSS styling with a floating design
   - Add JavaScript functionality for messaging

2. **Add Selected Text Functionality**: Implement functionality to capture selected text and include it with user questions.
   - Use browser Selection API to get selected text
   - Add UI element to incorporate selected text into questions

3. **Create HTML Include**: Design a simple HTML include pattern for easy integration.
   - Create a container div that can be placed anywhere
   - Implement initialization function

4. **Integrate with Docusaurus**: Implement the integration of the widget into the Docusaurus theme.
   - Create Docusaurus plugin or script injection mechanism
   - Ensure proper loading on all pages

5. **Connect to Backend**: Configure the widget to communicate with the existing RAG API endpoint.
   - Implement API calls using fetch
   - Handle responses and display in chat interface

## Phase 3: Validation

[To be filled with validation strategies]

## Risks

- Performance: JavaScript widget could impact page load times
- Security: Need to ensure API endpoints are properly secured for frontend access
- Compatibility: Widget needs to work across different browsers and devices