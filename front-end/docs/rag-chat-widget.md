# RAG Chatbot Integration

The RAG (Retrieval-Augmented Generation) chatbot is integrated into this Docusaurus site to provide an interactive way for users to ask questions about the robotics book content.

## Chatbot Features

- Floating chat interface accessible from any page
- Integration with selected text (users can select text and ask questions about it)
- Source attribution for all generated answers
- Responsive design for desktop and mobile
- Non-intrusive to the reading experience
- Real-time conversation interface

## How It Works

The chatbot uses RAG technology to provide accurate answers based on the robotics book content:

1. User asks a question in the chat interface
2. Question is sent to the backend API
3. Backend retrieves relevant content from the vector database
4. The LLM generates a contextual response based on retrieved content
5. Response is displayed in the chat interface

## Backend API

The RAG chatbot requires a backend API to process queries. This backend needs to be deployed separately from the Docusaurus static site because:

1. The RAG pipeline requires server-side processing and access to the Qdrant vector database
2. The backend needs to make API calls to OpenAI or other LLM services
3. The backend handles the vector similarity search and response generation

### Backend Endpoints

Your RAG API should provide the following:

1. `POST /query` endpoint that accepts requests with:
   - `query`: The user's question
   - `selected_text`: Text selected by the user when asking (optional)
   - `debug`: Boolean to return additional information (optional)

2. `GET /health` endpoint for health checks

3. `GET /` root endpoint with API information

### Response Format

The API returns responses in the following format:
- `answer`: The generated answer to the user's query
- `retrieved_content`: Array of relevant content chunks (when debug=true)

## Frontend Integration

The chatbot is integrated using React components and is automatically available on all pages through the Root component.

## Deployment Instructions

### For Local Development

1. Ensure your RAG API is running (typically on http://localhost:8000)
2. Start the Docusaurus development server: `npm start`
3. The chatbot will automatically connect to the backend at the configured URL

### For Production Deployment

1. Deploy your RAG API to a suitable hosting platform (e.g., Render, Heroku, AWS, Google Cloud)
2. Build the Docusaurus site: `npm run build`
3. Deploy the static files to your hosting platform
4. Set the `RAG_API_URL` environment variable to your deployed API URL

## Troubleshooting

### Chatbot Not Appearing

- Check browser console for JavaScript errors
- Verify that the Root.js component is loading the Chatbot component
- Ensure the project dependencies are properly installed

### API Connection Issues

- Check browser console for CORS errors
- Verify the backend API is running and accessible
- Test the API endpoint directly to ensure it's responding
- Make sure your backend has CORS configured to accept requests from your frontend domain

### Build Errors

- Ensure all dependencies are installed: `npm install`
- Verify the Chatbot component is properly imported and used in Root.js