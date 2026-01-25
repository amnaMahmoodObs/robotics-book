/* Floating RAG Chat Widget */
class RagChatWidget {
  constructor(config = {}) {
    this.config = {
      position: config.position || 'bottom-right',
      title: config.title || 'Robotics Knowledge Assistant',
      initialMessage: config.initialMessage || 'Ask me anything about robotics!',
      backendUrl: config.backendUrl || 'http://localhost:8000',
      welcomeMessage: config.welcomeMessage || 'Hello! Ask me anything about robotics concepts.',
      ...config
    };
    
    this.isOpen = false;
    this.sessionId = null;
    this.initializeWidget();
  }

  initializeWidget() {
    // Create the widget HTML structure
    this.createWidgetHTML();
    
    // Bind event listeners
    this.bindEvents();
    
    // Add to the page
    document.body.appendChild(this.widgetContainer);
  }

  createWidgetHTML() {
    // Create the main container
    this.widgetContainer = document.createElement('div');
    this.widgetContainer.id = 'rag-chat-widget';
    this.widgetContainer.className = `rag-chat-widget ${this.config.position}`;
    
    // Create toggle button
    this.toggleButton = document.createElement('div');
    this.toggleButton.id = 'rag-chat-toggle';
    this.toggleButton.className = 'rag-chat-toggle';
    this.toggleButton.innerHTML = '🤖';
    this.toggleButton.title = 'Ask about robotics';
    
    // Create chat window
    this.chatWindow = document.createElement('div');
    this.chatWindow.className = 'rag-chat-window';
    this.chatWindow.style.display = 'none';
    
    // Create header
    const header = document.createElement('div');
    header.className = 'rag-chat-header';
    header.innerHTML = `
      <div class="rag-chat-title">${this.config.title}</div>
      <button id="rag-chat-close" class="rag-chat-close">&times;</button>
    `;
    
    // Create messages container
    this.messagesContainer = document.createElement('div');
    this.messagesContainer.className = 'rag-chat-messages';
    
    // Add welcome message
    const welcomeMessage = document.createElement('div');
    welcomeMessage.className = 'rag-chat-message assistant-message';
    welcomeMessage.textContent = this.config.welcomeMessage;
    this.messagesContainer.appendChild(welcomeMessage);
    
    // Create input area
    const inputArea = document.createElement('div');
    inputArea.className = 'rag-chat-input-area';
    inputArea.innerHTML = `
      <textarea id="rag-chat-input" class="rag-chat-input" placeholder="Ask about robotics concepts..." rows="1"></textarea>
      <button id="rag-chat-send" class="rag-chat-send">Send</button>
    `;
    
    // Assemble the chat window
    this.chatWindow.appendChild(header);
    this.chatWindow.appendChild(this.messagesContainer);
    this.chatWindow.appendChild(inputArea);
    
    // Add all elements to the container
    this.widgetContainer.appendChild(this.toggleButton);
    this.widgetContainer.appendChild(this.chatWindow);
  }

  bindEvents() {
    // Toggle chat window
    this.toggleButton.addEventListener('click', () => this.toggleChat());
    
    // Close button
    document.getElementById('rag-chat-close').addEventListener('click', () => this.closeChat());
    
    // Send message
    document.getElementById('rag-chat-send').addEventListener('click', () => this.sendMessage());
    
    // Input handling
    const input = document.getElementById('rag-chat-input');
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        this.sendMessage();
      }
    });
    
    // Auto-resize textarea
    input.addEventListener('input', this.autoResizeTextarea);
    
    // Context menu for selected text
    document.addEventListener('mouseup', () => this.handleTextSelection());
  }

  autoResizeTextarea() {
    const input = document.getElementById('rag-chat-input');
    input.style.height = 'auto';
    input.style.height = (input.scrollHeight > 150 ? 150 : input.scrollHeight) + 'px';
  }

  toggleChat() {
    if (this.isOpen) {
      this.closeChat();
    } else {
      this.openChat();
    }
  }

  openChat() {
    this.chatWindow.style.display = 'flex';
    this.isOpen = true;
    document.getElementById('rag-chat-input').focus();
  }

  closeChat() {
    this.chatWindow.style.display = 'none';
    this.isOpen = false;
  }

  async sendMessage() {
    const input = document.getElementById('rag-chat-input');
    const message = input.value.trim();
    
    if (!message) return;
    
    // Add user message to UI
    this.addMessageToUI(message, 'user');
    input.value = '';
    input.style.height = 'auto';
    
    // Get selected text if any
    const selectedText = this.getSelectedText();
    
    try {
      // Call the backend API
      const response = await this.callBackend(message, selectedText);
      
      // Add assistant response to UI
      this.addMessageToUI(response.answer, 'assistant', response.sources);
    } catch (error) {
      console.error('Error sending message:', error);
      this.addMessageToUI('Sorry, I encountered an error processing your request.', 'assistant');
    }
  }

  async callBackend(query, selectedText = '') {
    const requestBody = {
      query: query,
      selected_text: selectedText,
      context: window.location.href,
      top_k: 5
    };

    const response = await fetch(`${this.config.backendUrl}/query`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    });
    
    if (!response.ok) {
      throw new Error(`API request failed with status ${response.status}`);
    }
    
    return await response.json();
  }

  addMessageToUI(content, role, sources = null) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `rag-chat-message ${role}-message`;
    
    if (role === 'assistant' && sources) {
      // Format the assistant response with sources
      messageDiv.innerHTML = `
        <div class="message-content">${this.escapeHtml(content)}</div>
        ${sources.length > 0 ? `
        <details class="sources-details">
          <summary>Sources (${sources.length})</summary>
          <ul class="sources-list">
            ${sources.map(source => 
              `<li><a href="${this.getSourceUrl(source.file)}" target="_blank" rel="noopener">${this.formatSourceName(source.file)}</a> (Score: ${(source.relevance * 100).toFixed(1)})</li>`
            ).join('')}
          </ul>
        </details>` : ''}
      `;
    } else {
      messageDiv.textContent = content;
    }
    
    this.messagesContainer.appendChild(messageDiv);
    
    // Scroll to bottom
    this.messagesContainer.scrollTop = this.messagesContainer.scrollHeight;
  }

  escapeHtml(unsafe) {
    return unsafe
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  getSourceUrl(sourceFile) {
    // Convert source file path to documentation URL
    // This assumes a standard Docusaurus structure
    const fileName = sourceFile.split('/').pop().replace('.md', '');
    return `/docs/${fileName}`;
  }

  formatSourceName(sourceFile) {
    // Extract meaningful name from file path
    const fileName = sourceFile.split('/').pop().replace('.md', '');
    return fileName.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
  }

  getSelectedText() {
    const selection = window.getSelection();
    return selection.toString().trim();
  }

  handleTextSelection() {
    const selectedText = this.getSelectedText();
    if (selectedText.length > 0 && selectedText.length < 500) { // Only activate for reasonably sized selections
      // Optionally show a hint or button to ask about the selected text
      // For now, we'll just store it to be used with the next query
      this.lastSelectedText = selectedText;
    }
  }

  // Add styles to the page
  static addDefaultStyles() {
    if (document.getElementById('rag-chat-widget-styles')) return;
    
    const styles = document.createElement('style');
    styles.id = 'rag-chat-widget-styles';
    styles.textContent = `
      #rag-chat-widget {
        position: fixed;
        z-index: 10000;
      }
      
      .rag-chat-widget.bottom-right {
        bottom: 20px;
        right: 20px;
      }
      
      .rag-chat-widget.bottom-left {
        bottom: 20px;
        left: 20px;
      }
      
      .rag-chat-toggle {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-color: #4f46e5;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
      }
      
      .rag-chat-toggle:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
      }
      
      .rag-chat-window {
        position: absolute;
        bottom: 80px;
        width: 350px;
        max-width: calc(100vw - 40px);
        max-height: 60vh;
        display: flex;
        flex-direction: column;
        background: white;
        border-radius: 12px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        overflow: hidden;
        opacity: 0;
        transform: translateY(20px);
        animation: chatWindowAppear 0.3s forwards;
      }
      
      @keyframes chatWindowAppear {
        to {
          opacity: 1;
          transform: translateY(0);
        }
      }
      
      .rag-chat-header {
        background-color: #4f46e5;
        color: white;
        padding: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      
      .rag-chat-title {
        font-weight: 600;
        font-size: 16px;
      }
      
      .rag-chat-close {
        background: none;
        border: none;
        color: white;
        font-size: 24px;
        cursor: pointer;
        padding: 0;
        width: 30px;
        height: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
      }
      
      .rag-chat-messages {
        flex: 1;
        padding: 15px;
        overflow-y: auto;
        max-height: 300px;
        display: flex;
        flex-direction: column;
        gap: 10px;
      }
      
      .rag-chat-message {
        padding: 10px 14px;
        border-radius: 18px;
        max-width: 85%;
        word-wrap: break-word;
        line-height: 1.4;
      }
      
      .user-message {
        background-color: #e0e7ff;
        align-self: flex-end;
        border-bottom-right-radius: 4px;
      }
      
      .assistant-message {
        background-color: #f3f4f6;
        align-self: flex-start;
        border-bottom-left-radius: 4px;
      }
      
      .message-content {
        margin-bottom: 8px;
      }
      
      .sources-details {
        font-size: 0.8em;
        color: #6b7280;
      }
      
      .sources-details summary {
        cursor: pointer;
        color: #4f46e5;
      }
      
      .sources-list {
        padding-left: 20px;
        margin-top: 8px;
      }
      
      .sources-list li {
        margin-bottom: 5px;
      }
      
      .sources-list a {
        color: #4f46e5;
        text-decoration: none;
      }
      
      .sources-list a:hover {
        text-decoration: underline;
      }
      
      .rag-chat-input-area {
        display: flex;
        padding: 10px;
        border-top: 1px solid #e5e7eb;
        background: white;
      }
      
      .rag-chat-input {
        flex: 1;
        padding: 10px 14px;
        border: 1px solid #d1d5db;
        border-radius: 20px;
        resize: none;
        overflow: hidden;
        max-height: 150px;
        font-family: inherit;
        font-size: 14px;
        outline: none;
      }
      
      .rag-chat-input:focus {
        border-color: #4f46e5;
        box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.1);
      }
      
      .rag-chat-send {
        background-color: #4f46e5;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 0 20px;
        margin-left: 10px;
        cursor: pointer;
        font-weight: 500;
      }
      
      .rag-chat-send:hover {
        background-color: #4338ca;
      }
      
      /* Mobile responsiveness */
      @media (max-width: 768px) {
        .rag-chat-window {
          width: calc(100vw - 40px);
          max-height: 50vh;
        }
        
        .rag-chat-message {
          max-width: 90%;
        }
      }
    `;
    
    document.head.appendChild(styles);
  }
}

// Initialize the widget when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  RagChatWidget.addDefaultStyles();
});

// Helper function for easy initialization
function initRagChatWidget(config) {
  document.addEventListener('DOMContentLoaded', () => {
    new RagChatWidget(config);
  });
}