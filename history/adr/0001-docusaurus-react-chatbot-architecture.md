# ADR-0001: Docusaurus React Chatbot Architecture

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-01
- **Feature:** 008-rag-chatbot-ui
- **Context:** The goal is to integrate a FastAPI RAG backend into a Docusaurus website by adding an interactive chatbot UI. The integration needs to be lightweight and simple, supporting both direct user queries and text-selection based contextual queries. This architectural decision focuses on the frontend integration strategy within the Docusaurus framework.

## Decision

The chatbot UI will be implemented as a custom React component within the Docusaurus theme override system, specifically under `src/theme/common/Chatbot/`. This will include components for the main chatbot, input field, chat window, and a service for API calls to the backend. The UI trigger (e.g., a floating button) will be integrated into the Docusaurus Layout component. The existing FastAPI RAG backend remains unchanged and will be consumed via its POST query endpoint.

## Consequences

### Positive

- **Lightweight Integration**: Leveraging Docusaurus's theme override system allows for minimal impact on the core Docusaurus build process and structure.
- **React Ecosystem**: Utilizes familiar React development patterns and tools for the UI, enabling efficient development and maintenance for React-proficient teams.
- **Modular Design**: Separating the chatbot into distinct React components (main, input, window, service) promotes reusability, testability, and maintainability.
- **Contextual Query Support**: Direct integration within the Docusaurus frontend enables seamless capture of highlighted text for contextual RAG queries.

### Negative

- **Docusaurus Specifics**: The implementation will be tightly coupled with Docusaurus's theme override mechanism, potentially requiring adjustments if Docusaurus undergoes significant architectural changes.
- **Frontend Complexity**: Adding an interactive chat UI increases the frontend bundle size and introduces new state management challenges for the chat history and active queries.
- **API Dependency**: The frontend UI is entirely dependent on the FastAPI RAG backend being operational and responsive.

## Alternatives Considered

-   **Iframe Integration**: Embedding the chatbot as an iframe from a separate application.
    -   **Why rejected**: Introduces cross-origin communication complexities, potential styling inconsistencies, and a less seamless user experience. Also, capturing highlighted text from the parent document for contextual queries would be significantly more complex or impossible.
-   **External Micro-frontend**: Developing the chatbot as a completely separate micro-frontend application.
    -   **Why rejected**: Adds overhead of managing a separate build process, deployment, and increased complexity for sharing state/context with the Docusaurus application. It would also increase the difficulty of achieving a lightweight integration.
-   **Docusaurus Plugin**: Attempting to implement the chatbot as a Docusaurus plugin.
    -   **Why rejected**: While potentially cleaner, developing a full-fledged Docusaurus plugin might be an overkill for a lightweight integration and could introduce a steeper learning curve or more rigid constraints than a custom React component. The `theme override` approach offers more direct control and flexibility for a custom UI.

## References

- Feature Spec: `specs/008-rag-chatbot-ui/spec.md`
- Implementation Plan: `specs/008-rag-chatbot-ui/plan.md`
- Related ADRs: N/A
- Evaluator Evidence: N/A
