import React, { useState, useEffect } from 'react';
import './Chatbot.css'; // Import the CSS file for styling
import { queryRAGBackend } from './ChatService';

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [backendUrl, setBackendUrl] = useState('http://localhost:8000'); // Default or fallback URL


  // Function to get selected text from the document
  const getSelectedText = () => {
    const selection = window.getSelection();
    return selection.toString().trim();
  };

  useEffect(() => {
    if (typeof window !== 'undefined' && window.initRagChatWidget && window.initRagChatWidget.config && window.initRagChatWidget.config.backendUrl) {
      setBackendUrl(window.initRagChatWidget.config.backendUrl);
    }
  }, []);

  // Function to send a query to the backend
  const sendQueryToBackend = async (query, selectedText = null) => {
    try {
      setIsLoading(true);
      const response = await queryRAGBackend(query, backendUrl, selectedText);
      const answer = response.answer || response;

      setMessages(prevMessages => [
        ...prevMessages,
        {
          type: 'bot',
          text: answer,
          timestamp: new Date().toLocaleTimeString()
        }
      ]);
    } catch (error) {
      setMessages(prevMessages => [
        ...prevMessages,
        {
          type: 'bot',
          text: `Error: ${error.message || 'Failed to get response from RAG backend'}`,
          isError: true
        }
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleSendMessage = async () => {
    if (input.trim()) {
      // Add user message to the chat
      const userMessage = {
        type: 'user',
        text: input,
        timestamp: new Date().toLocaleTimeString()
      };

      setMessages(prevMessages => [...prevMessages, userMessage]);
      const currentInput = input;
      setInput(''); // Clear input immediately after sending

      // Send query to backend
      await sendQueryToBackend(currentInput);
    }
  };

  const handleSendSelectedText = async () => {
    const selectedText = getSelectedText();

    if (!selectedText) {
      setMessages(prevMessages => [
        ...prevMessages,
        {
          type: 'bot',
          text: 'Please select some text on the page first.',
          isError: true
        }
      ]);
      return;
    }

    // Add user message indicating selected text query
    const userMessage = {
      type: 'user',
      text: `Query with selected text: "${selectedText.substring(0, 50)}${selectedText.length > 50 ? '...' : ''}"`,
      timestamp: new Date().toLocaleTimeString()
    };

    setMessages(prevMessages => [...prevMessages, userMessage]);

    // Send selected text as query to backend
    await sendQueryToBackend(selectedText);
  };

  // Add keyboard shortcut for sending selected text (Ctrl/Cmd + Enter)
  useEffect(() => {
    const handleKeyDown = (e) => {
      // Check if Ctrl/Cmd+Enter is pressed
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter' && isOpen && getSelectedText()) {
        handleSendSelectedText();
      }
    };

    if (isOpen) {
      window.addEventListener('keydown', handleKeyDown);
    }

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [isOpen]);

  return (
    <div className="chatbot-container">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="chatbot-toggle-button"
        aria-label={isOpen ? 'Close Chatbot' : 'Open Chatbot'}
      >
        {isOpen ? '×' : '💬'}
      </button>

      {isOpen && (
        <div className="chatbot-window">
          <div className="chat-header">
            <h3>Book Assistant</h3>
          </div>
          <div className="chat-messages">
            {messages.map((msg, index) => (
              <div key={index} className={`chat-message ${msg.type} ${msg.isError ? 'error' : ''}`}>
                <span className={`message-bubble ${msg.type}-bubble ${msg.isError ? 'error-bubble' : ''}`}>
                  {msg.text}
                </span>
                {msg.timestamp && (
                  <span className="timestamp">{msg.timestamp}</span>
                )}
              </div>
            ))}
            {isLoading && (
              <div className="chat-message bot">
                <span className="message-bubble bot-bubble">
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </span>
              </div>
            )}
          </div>
          <div className="chat-input-area">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
              placeholder="Ask a question about robotics..."
              className="chat-input"
            />
            <button
              onClick={handleSendMessage}
              className="send-button"
              disabled={!input.trim() || isLoading}
            >
              Send
            </button>
          </div>
          <div className="chat-controls">
            <button
              onClick={handleSendSelectedText}
              className="selected-text-button"
              disabled={!getSelectedText() || isLoading}
              title="Send selected text as query (Ctrl/Cmd + Enter)"
            >
              Query with selected text
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chatbot;
