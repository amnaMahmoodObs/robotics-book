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
        # Change to the backend src directory
        backend_src_path = "/Users/jamalazfarkhan/AI Agents/robotics-book/backend/src"
        os.chdir(backend_src_path)
        
        # Run uvicorn with specific file exclusion to avoid the build directory issue
        cmd = [
            sys.executable, "-m", "uvicorn", 
            "main:app", 
            "--host", "0.0.0.0", 
            "--port", "8000",
            "--reload",
            "--reload-exclude", "*/front-end/build/*"
        ]
        
        print("Starting RAG API server...")
        print(f"Command: {' '.join(cmd)}")
        
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")


if __name__ == "__main__":
    start_server()