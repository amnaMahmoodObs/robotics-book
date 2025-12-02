"""
Integration test for the RAG chatbot system
This test ensures that the frontend and backend work together properly.
"""
import subprocess
import time
import requests


def test_backend_api():
    """Test the backend API endpoints"""
    try:
        # Check health endpoint
        response = requests.get("http://localhost:8000/health", timeout=10)
        assert response.status_code == 200
        health_data = response.json()
        print("✓ Health check passed:", health_data)

        # Check root endpoint
        response = requests.get("http://localhost:8000/", timeout=10)
        assert response.status_code == 200
        root_data = response.json()
        print("✓ Root endpoint working:", root_data["message"])

        # Test query endpoint
        payload = {
            "query": "What is robotics?",
            "debug": True
        }
        response = requests.post("http://localhost:8000/query", json=payload, timeout=30)
        assert response.status_code == 200
        query_result = response.json()
        print("✓ Query endpoint working, answer length:", len(query_result["answer"]))

        # Check if retrieved content is returned in debug mode
        assert "retrieved_content" in query_result
        print("✓ Retrieved content returned in debug mode:", len(query_result["retrieved_content"]))

        return True
    except Exception as e:
        print(f"✗ Backend API test failed: {e}")
        return False


def test_frontend_integration():
    """Test frontend components"""
    try:
        # Check if frontend files exist and are properly structured
        import os

        frontend_files = [
            "front-end/src/theme/common/Chatbot/index.js",
            "front-end/src/theme/common/Chatbot/ChatService.js",
            "front-end/src/theme/common/Chatbot/Chatbot.css",
            "front-end/src/Root.js"
        ]

        for file in frontend_files:
            file_path = os.path.join("/Users/jamalazfarkhan/AI Agents/robotics-book", file)
            assert os.path.exists(file_path), f"File does not exist: {file}"
            print(f"✓ Frontend file exists: {file}")

        return True
    except Exception as e:
        print(f"✗ Frontend integration test failed: {e}")
        return False


if __name__ == "__main__":
    print("Starting RAG Chatbot Integration Tests...")

    backend_ok = test_backend_api()
    frontend_ok = test_frontend_integration()

    if backend_ok and frontend_ok:
        print("\n✓ All integration tests passed!")
    else:
        print("\n✗ Some integration tests failed!")
        exit(1)