# Quickstart Guide: RAG Chat Widget

## Overview

The RAG Chat Widget is a lightweight JavaScript component that allows users to ask questions about your robotics book content directly from the Docusaurus website. The widget integrates with your existing RAG pipeline to provide contextual answers.

## Setup

### 1. Backend API
Ensure your RAG API is running and accessible from your GitHub Pages site (CORS configured).

### 2. Widget Integration
Add the widget to your Docusaurus site by including the JavaScript file and a container div:

```html
<!-- Add this to your Docusaurus pages -->
<div id="rag-chat-widget-container"></div>
<script src="path/to/rag-chat-widget.js"></script>
<script>
  // Initialize the widget
  initRagChatWidget({
    backendUrl: 'https://your-api-url.com',
    title: 'Robotics Knowledge Assistant',
    initialMessage: 'Ask me anything about robotics!'
  });
</script>
```

### 3. Docusaurus Plugin (Alternative)
You can also integrate via a Docusaurus plugin by adding it to your `docusaurus.config.js`:

```js
module.exports = {
  // ... your config
  plugins: [
    // ... other plugins
    [
      'path/to/rag-chat-plugin',
      {
        backendUrl: 'https://your-api-url.com',
        title: 'Robotics Knowledge Assistant'
      }
    ]
  ]
};
```

## Features

1. **Floating Interface**: Widget appears as a floating icon that expands to a chat interface
2. **Selected Text Integration**: Users can select text on a page and ask questions about it
3. **Context Awareness**: Widget can pass page context to improve answer relevance
4. **Responsive Design**: Works on both desktop and mobile devices