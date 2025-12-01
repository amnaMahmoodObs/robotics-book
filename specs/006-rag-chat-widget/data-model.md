# Data Model: RAG Chat Widget

## Entities

### ChatMessage
- **Fields**:
  - id (string, required): Unique identifier for the message
  - content (string, required): The text content of the message
  - role (string, required): Either "user" or "assistant"
  - timestamp (datetime, required): When the message was created
  - sources (array[object], optional): Source information for assistant responses

- **Validation Rules**:
  - content must be 1-2000 characters
  - role must be either "user" or "assistant"
  - sources, if provided, must have valid file and relevance properties

### ChatSession
- **Fields**:
  - sessionId (string, required): Unique identifier for the session
  - messages (array[ChatMessage], required): Messages in the conversation
  - createdAt (datetime, required): When the session started
  - lastActiveAt (datetime, required): When the last message was sent

- **Validation Rules**:
  - messages must have 0-100 messages
  - createdAt must be before or equal to lastActiveAt
  - sessionId must be unique per user session

### UserQuery
- **Fields**:
  - question (string, required): The user's question
  - selectedText (string, optional): Text selected by the user when asking the question
  - context (string, optional): Additional context related to the question
  - pageUrl (string, optional): URL of the page where the question was asked

- **Validation Rules**:
  - question must be 1-1000 characters
  - selectedText, if provided, must be 1-500 characters
  - pageUrl, if provided, must be a valid URL

### WidgetConfig
- **Fields**:
  - position (string, required): Widget position on screen (e.g., "bottom-right", "bottom-left")
  - title (string, required): Title displayed in the widget header
  - initialMessage (string, optional): Message shown when widget opens
  - backendUrl (string, required): URL of the RAG backend API
  - welcomeMessage (string, optional): Welcome message for new sessions

- **Validation Rules**:
  - position must be a valid position value
  - title must be 1-100 characters
  - backendUrl must be a valid URL