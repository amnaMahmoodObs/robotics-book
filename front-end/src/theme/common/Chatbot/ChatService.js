/**
 * Service for handling communication with the FastAPI RAG backend
 */

/**
 * Queries the RAG backend with a user question and optional selected text
 * @param {string} query - The user's question
 * @param {string} [selectedText] - Optional selected text to provide as context
 * @returns {Promise<Object>} The response from the backend
 */
export const queryRAGBackend = async (query, backendUrl, selectedText = null) => {
  const API_BASE_URL = backendUrl || 'https://robotics-book-mu.vercel.app';
  try {
    // Construct the payload
    const payload = {
      query: query,
      ...(selectedText && { selected_text: selectedText })
    };

    const response = await fetch(`${API_BASE_URL}/query`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      throw new Error(`Backend error: ${response.status} ${response.statusText}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error querying RAG backend:', error);
    throw error;
  }
};

/**
 * Health check for the backend
 * @returns {Promise<Object>} The health check response
 */
export const checkHealth = async (backendUrl) => {
  const API_BASE_URL = backendUrl || 'https://robotics-book-mu.vercel.app';
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    
    if (!response.ok) {
      throw new Error(`Health check failed: ${response.status} ${response.statusText}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Health check error:', error);
    throw error;
  }
};