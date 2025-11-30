# RAG Chat Widget Configuration

The floating RAG chat widget is integrated into this Docusaurus site to provide an interactive way for users to ask questions about the robotics book content.

## Widget Features

- Floating chat interface accessible from any page
- Integration with selected text (users can select text and ask questions about it)
- Source attribution for all generated answers
- Responsive design for desktop and mobile
- Non-intrusive to the reading experience

## Configuration Options

The widget can be configured with the following options:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `backendUrl` | string | `https://robotics-book-rag-api.onrender.com` | URL of your RAG API backend |
| `title` | string | `Robotics Knowledge Assistant` | Title shown in the widget header |
| `initialMessage` | string | `Ask me anything about robotics!` | Message shown when widget opens |
| `position` | string | `bottom-right` | Position of the widget ('bottom-right', 'bottom-left') |
| `welcomeMessage` | string | `Hello! I'm your Robotics Knowledge Assistant...` | Welcome message for new sessions |

## Backend Deployment

The RAG chat widget requires a backend API to process queries. This backend needs to be deployed separately from the Docusaurus static site because:

1. The RAG pipeline requires server-side processing and access to the Qdrant vector database
2. The backend needs to make API calls to OpenAI or other LLM services
3. The backend handles the vector similarity search and response generation

### Backend Requirements

Your RAG API should provide the following:

1. A `/ask` endpoint that accepts POST requests with:
   - `query`: The user's question
   - `selectedText`: Text selected by the user when asking (optional)
   - `context`: Page context information (optional)
   - `page_url`: URL of the page where the question was asked (optional)
   - `top_k`: Number of results to retrieve (optional)

2. Response format that includes:
   - `query`: The original user query
   - `answer`: The generated answer
   - `sources`: Array of source documents with file paths and relevance scores
   - `context_length`: Length of the context used for generation

### CORS Configuration

Make sure your backend API allows cross-origin requests from your GitHub Pages domain. In FastAPI, this looks like:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://yourusername.github.io"],  # Your GitHub Pages URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Deployment Instructions

### For Local Development

1. Ensure your RAG API is running (typically on http://localhost:8000)
2. Update the `backendUrl` in `src/clientModules/rag-widget-init.js` to `'http://localhost:8000'`
3. Start the Docusaurus development server: `yarn start`

### For Production Deployment

1. Deploy your RAG API to a suitable hosting platform (e.g., Render, Heroku, AWS, Google Cloud)
2. Update the `backendUrl` in `src/clientModules/rag-widget-init.js` to your deployed API URL
3. Build the Docusaurus site: `yarn build`
4. Deploy the static files to GitHub Pages: `GIT_USER=<Your GitHub username> yarn deploy`

## Troubleshooting

### Widget Not Appearing

- Check browser console for JavaScript errors
- Verify that the script is being loaded by checking the Network tab
- Ensure the initialization function is being called

### API Connection Issues

- Check browser console for CORS errors
- Verify the `backendUrl` is correctly configured
- Test the API endpoint directly to ensure it's responding

### Build Errors

- Make sure the `src/clientModules` directory exists
- Verify all paths in the configuration are correct