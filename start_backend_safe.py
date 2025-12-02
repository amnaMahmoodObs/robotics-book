#!/usr/bin/env python3
"""
Start script for the RAG API server
"""
import subprocess
import sys
import os


def start_server():
    """Start the RAG API server"""
    try:
        # Use absolute path to avoid issues with spaces in directory names
        backend_src_path = "/Users/jamalazfarkhan/AI Agents/robotics-book/backend/src"
        
        # Run uvicorn directly using python -m
        cmd = [
            sys.executable, 
            "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000"
        ]
        
        print("Starting RAG API server...")
        print(f"Working directory: {backend_src_path}")
        print(f"Command: {' '.join(cmd)}")
        
        # Change to the backend directory and run the command
        os.chdir(backend_src_path)
        result = subprocess.run(cmd)
        
        if result.returncode != 0:
            print(f"Server exited with code: {result.returncode}")
        else:
            print("Server stopped")
            
    except FileNotFoundError:
        print("Error: Could not find backend/src directory. Please ensure you're in the correct project directory.")
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")


if __name__ == "__main__":
    start_server()