# Website

This website is built using [Docusaurus](https://docusaurus.io/), a modern static website generator.

## Installation

```bash
yarn
```

## Local Development

```bash
yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## Build

```bash
yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## RAG Chat Widget

This website includes a floating RAG (Retrieval-Augmented Generation) chat widget that allows users to ask questions about the robotics book content. The widget is integrated on all pages automatically.

### Backend API Configuration

The chat widget requires a backend API to function. Update the API URL in `src/clientModules/rag-widget-init.js` to point to your deployed RAG API:

```javascript
backendUrl: 'https://your-deployed-rag-api.com'
```

### Local Development with Widget

To test the widget with a local API during development:

1. Ensure your RAG API server is running (typically on `http://localhost:8000`)
2. Update the `backendUrl` in `src/clientModules/rag-widget-init.js` to `'http://localhost:8000'`
3. Run the Docusaurus dev server: `yarn start`

## Deployment

Using SSH:

```bash
USE_SSH=true yarn deploy
```

Not using SSH:

```bash
GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

### GitHub Pages Deployment with RAG Widget

When deploying to GitHub Pages, note that:

1. The frontend will be hosted at `https://<username>.github.io/robotics-book/`
2. You must separately deploy the RAG API backend to a service that supports server-side processing
3. Ensure your backend API allows cross-origin requests from your GitHub Pages domain
4. Update the `backendUrl` in `src/clientModules/rag-widget-init.js` to point to your deployed API before building
