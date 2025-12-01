import os
import shutil
from typing import List, Tuple
from git import Repo
from markdown_it import MarkdownIt

def load_repo(repo_url: str, local_path: str) -> None:
    """
    Clones a Git repository to a specified local path.
    If the directory already exists, it will be removed and re-cloned.
    """
    if os.path.exists(local_path):
        shutil.rmtree(local_path)
    Repo.clone_from(repo_url, local_path)

def load_markdown(local_path: str) -> List[Tuple[str, str]]:
    """
    Locates and reads all Markdown files within a local path,
    returning a list of (file_path, content) tuples.
    """
    markdown_files = []
    parser = MarkdownIt()
    for root, _, files in os.walk(local_path):
        for file in files:
            if file.endswith((".md", ".mdx")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    markdown_files.append((file_path, content))
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    return markdown_files
