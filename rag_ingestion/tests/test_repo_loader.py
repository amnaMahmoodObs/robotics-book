import os
import shutil
from unittest.mock import patch, MagicMock
import pytest
from rag_ingestion.repo_loader import load_repo, load_markdown

# Fixture for a temporary directory
@pytest.fixture
def temp_dir(tmp_path):
    yield tmp_path
    # Cleanup is handled by tmp_path fixture

# Test load_repo function
def test_load_repo_success(temp_dir):
    repo_url = "https://github.com/gregkinney/rag-test-repo.git"  # A small public test repo
    local_path = os.path.join(temp_dir, "test_repo")

    load_repo(repo_url, local_path)

    assert os.path.exists(local_path)
    assert os.path.isdir(local_path)
    assert os.path.exists(os.path.join(local_path, ".git"))

def test_load_repo_removes_existing_dir(temp_dir):
    repo_url = "https://github.com/gregkinney/rag-test-repo.git"
    local_path = os.path.join(temp_dir, "test_repo")
    os.makedirs(local_path)
    with open(os.path.join(local_path, "dummy.txt"), "w") as f:
        f.write("old content")

    load_repo(repo_url, local_path)

    assert os.path.exists(local_path)
    assert not os.path.exists(os.path.join(local_path, "dummy.txt")) # Old content should be removed
    assert os.path.exists(os.path.join(local_path, ".git"))

@patch('git.Repo.clone_from')
def test_load_repo_clone_failure(mock_clone_from, temp_dir):
    mock_clone_from.side_effect = Exception("Mock clone error")
    repo_url = "invalid_url"
    local_path = os.path.join(temp_dir, "test_repo")

    with pytest.raises(Exception, match="Mock clone error"):
        load_repo(repo_url, local_path)
    assert not os.path.exists(local_path)

# Test load_markdown function
def test_load_markdown_success(temp_dir):
    # Create dummy markdown files
    repo_path = os.path.join(temp_dir, "test_markdown_repo")
    os.makedirs(repo_path)
    with open(os.path.join(repo_path, "file1.md"), "w", encoding="utf-8") as f:
        f.write("# Hello\nThis is markdown content 1.")
    with open(os.path.join(repo_path, "file2.mdx"), "w", encoding="utf-8") as f:
        f.write("## World\nThis is mdx content 2.")
    with open(os.path.join(repo_path, "not_markdown.txt"), "w", encoding="utf-8") as f:
        f.write("plain text")

    markdown_files = load_markdown(repo_path)

    assert len(markdown_files) == 2
    file_paths = [mf[0] for mf in markdown_files]
    contents = [mf[1] for mf in markdown_files]

    assert os.path.join(repo_path, "file1.md") in file_paths
    assert os.path.join(repo_path, "file2.mdx") in file_paths
    assert "# Hello\nThis is markdown content 1." in contents
    assert "## World\nThis is mdx content 2." in contents
    assert "plain text" not in contents

def test_load_markdown_no_markdown_files(temp_dir):
    repo_path = os.path.join(temp_dir, "empty_markdown_repo")
    os.makedirs(repo_path)
    with open(os.path.join(repo_path, "not_markdown.txt"), "w", encoding="utf-8") as f:
        f.write("plain text")

    markdown_files = load_markdown(repo_path)
    assert len(markdown_files) == 0

def test_load_markdown_empty_directory(temp_dir):
    repo_path = os.path.join(temp_dir, "empty_dir")
    os.makedirs(repo_path)
    markdown_files = load_markdown(repo_path)
    assert len(markdown_files) == 0

@patch('builtins.open', new_callable=MagicMock)
def test_load_markdown_read_error(mock_open, temp_dir):
    mock_open.side_effect = IOError("Mock read error")
    repo_path = os.path.join(temp_dir, "error_repo")
    os.makedirs(repo_path)
    with open(os.path.join(repo_path, "file.md"), "w") as f:
        f.write("dummy") # This open call is for file creation, not the mocked one

    # Reset mock after file creation, for the load_markdown call
    mock_open.reset_mock()
    mock_open.side_effect = IOError("Mock read error")

    markdown_files = load_markdown(repo_path)
    assert len(markdown_files) == 0
