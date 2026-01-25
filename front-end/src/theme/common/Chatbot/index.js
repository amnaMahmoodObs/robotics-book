import React, { useState, useEffect } from 'react';
import './Chatbot.css'; // Import the CSS file for styling
import { queryRAGBackend } from './ChatService';

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [backendUrl, setBackendUrl] = useState('http://localhost:8000'); // Default or fallback URL
  const [selectedText, setSelectedText] = useState(''); // Track selected text


  // Function to get selected text from the document
  const getSelectedText = () => {
    const selection = window.getSelection();
    return selection.toString().trim();
  };

  // Update selected text whenever user makes a selection
  useEffect(() => {
    const handleSelectionChange = () => {
      const text = getSelectedText();
      // Only update if there's new text selected, don't clear on deselection
      if (text && text.length > 0) {
        setSelectedText(text);
      }
    };

    // Listen for selection changes globally, not just when open
    document.addEventListener('selectionchange', handleSelectionChange);

    // Check immediately when chatbot opens
    if (isOpen) {
      handleSelectionChange();
    }

    return () => {
      document.removeEventListener('selectionchange', handleSelectionChange);
    };
  }, [isOpen]);

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
      const currentInput = input;
      const currentSelectedText = selectedText;

      // Add user message to the chat
      let displayText = currentInput;
      if (currentSelectedText) {
        displayText = `${currentInput}\n[Context: "${currentSelectedText.substring(0, 100)}${currentSelectedText.length > 100 ? '...' : ''}"]`;
      }

      const userMessage = {
        type: 'user',
        text: displayText,
        timestamp: new Date().toLocaleTimeString()
      };

      setMessages(prevMessages => [...prevMessages, userMessage]);
      setInput(''); // Clear input immediately after sending

      // Send query to backend with selected text as context
      await sendQueryToBackend(currentInput, currentSelectedText || null);

      // Clear selected text after sending
      setSelectedText('');
    }
  };


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
          {selectedText && (
            <div className="selected-text-indicator">
              <div className="selected-text-header">
                <span className="selected-text-label">📄 Selected Text (will be used as context):</span>
                <button
                  className="clear-selection-button"
                  onClick={() => setSelectedText('')}
                  title="Clear selected text"
                >
                  ✕
                </button>
              </div>
              <div className="selected-text-preview">
                "{selectedText.substring(0, 150)}{selectedText.length > 150 ? '...' : ''}"
              </div>
            </div>
          )}
          <div className="chat-input-area">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && !e.shiftKey && handleSendMessage()}
              placeholder={selectedText ? "Ask a question about the selected text..." : "Ask a question about robotics..."}
              className="chat-input"
            />
            <button
              onClick={handleSendMessage}
              className="send-button"
              disabled={!input.trim() || isLoading}
              title={selectedText ? "Send question with selected text as context" : "Send question"}
            >
              {selectedText ? '📤 Send with Context' : 'Send'}
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chatbot;
