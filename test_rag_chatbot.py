#!/usr/bin/env python3
"""
Test script to validate the RAG chatbot functionality
"""
import os
import sys
import asyncio
import json
from pathlib import Path

# Add the backend source to path
sys.path.insert(0, str(Path(__file__).parent / "backend/src"))

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check if required environment variables are set
required_vars = ["OPENAI_API_KEY", "QDRANT_URL", "QDRANT_API_KEY"]
missing_vars = [var for var in required_vars if not os.environ.get(var)]

if missing_vars:
    print(f"Warning: Missing environment variables: {', '.join(missing_vars)}")
    print("Please set these variables in a .env file for full functionality.")
else:
    print("All required environment variables are set.")

# Test if the backend can be imported without errors
try:
    from backend.src.rag_modules.book_rag_agent import BookRAGAgent
    from backend.src.config.settings import settings
    print("✓ Backend modules imported successfully")
except ImportError as e:
    print(f"✗ Failed to import backend modules: {e}")
    sys.exit(1)
except Exception as e:
    print(f"✗ Error with settings or configuration: {e}")
    sys.exit(1)

# Test the BookRAGAgent initialization
try:
    agent = BookRAGAgent(model_name="gpt-4.1-mini")
    print("✓ BookRAGAgent initialized successfully")
except Exception as e:
    print(f"✗ Failed to initialize BookRAGAgent: {e}")
    sys.exit(1)

# Test a sample query if environment is configured
if not missing_vars:
    try:
        sample_query = "What is robotics?"
        print(f"Testing sample query: '{sample_query}'")
        response = agent.answer_question(sample_query, debug=True)
        print(f"✓ Sample query processed successfully")
        print(f"Response: {response.get('answer', response)[:100]}...")
        print(f"Retrieved content count: {len(response.get('retrieved_content', []))}")
    except Exception as e:
        print(f"✗ Error processing sample query: {e}")
else:
    print("Skipping sample query test due to missing environment variables")

print("\nRAG chatbot backend functionality test completed.")