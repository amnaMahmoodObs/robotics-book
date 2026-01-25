"""
Vercel serverless function entry point for FastAPI app
"""
from src.main import app

# Vercel will use this as the handler
handler = app
