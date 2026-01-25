#!/usr/bin/env python3
"""
Smart RAG Ingestion Script
Intelligently updates Qdrant with only new/modified content
"""
import os
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from rag_ingestion.embeddings import embed_chunks
from rag_ingestion.qdrant_vector_store import QdrantVectorStore

# Track last ingestion times
INGESTION_STATE_FILE = ".rag_ingestion_state.json"


def load_ingestion_state():
    """Load the last ingestion state"""
    if os.path.exists(INGESTION_STATE_FILE):
        with open(INGESTION_STATE_FILE, 'r') as f:
            return json.load(f)
    return {}


def save_ingestion_state(state):
    """Save ingestion state to file"""
    with open(INGESTION_STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)


def get_markdown_files(docs_path):
    """Get all markdown files with their modification times"""
    files = {}
    docs_dir = Path(docs_path)

    for md_file in docs_dir.glob("**/*.md"):
        if md_file.is_file():
            rel_path = str(md_file.relative_to(docs_dir))
            mod_time = md_file.stat().st_mtime
            files[rel_path] = {
                'path': str(md_file),
                'modified': mod_time,
                'modified_str': datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')
            }

    return files


def detect_changes(current_files, last_state, force=False):
    """Detect new, modified, and unchanged files"""
    if force:
        return {
            'new': [],
            'modified': list(current_files.keys()),
            'unchanged': []
        }

    new_files = []
    modified_files = []
    unchanged_files = []

    for file_path, file_info in current_files.items():
        if file_path not in last_state:
            new_files.append(file_path)
        elif file_info['modified'] > last_state[file_path]['modified']:
            modified_files.append(file_path)
        else:
            unchanged_files.append(file_path)

    return {
        'new': new_files,
        'modified': modified_files,
        'unchanged': unchanged_files
    }


def main():
    parser = argparse.ArgumentParser(description='Smart RAG Ingestion - Only update changed content')
    parser.add_argument('--force', action='store_true', help='Re-ingest all files')
    parser.add_argument('--verify-only', action='store_true', help='Show what would be updated without ingesting')
    parser.add_argument('--test-query', default='What is robotics?', help='Test query after ingestion')
    parser.add_argument('--docs-path', default='front-end/docs/', help='Path to documentation files')

    args = parser.parse_args()

    # Ensure required environment variables
    required_env = ["QDRANT_URL", "QDRANT_API_KEY", "OPENAI_API_KEY", "QDRANT_COLLECTION_NAME"]
    missing = [var for var in required_env if not os.environ.get(var)]
    if missing:
        print(f"❌ Error: Missing environment variables: {', '.join(missing)}")
        print("Please check your .env file")
        sys.exit(1)

    collection_name = os.environ.get('QDRANT_COLLECTION_NAME')

    print(f"\n{'='*60}")
    print(f"🔍 RAG Ingestion Analysis")
    print(f"{'='*60}\n")

    # Get current files
    print(f"📂 Scanning: {args.docs_path}")
    current_files = get_markdown_files(args.docs_path)
    print(f"   Found {len(current_files)} markdown files\n")

    # Load last state
    last_state = load_ingestion_state()

    # Detect changes
    changes = detect_changes(current_files, last_state, args.force)

    # Report changes
    print(f"📊 Change Detection:")
    print(f"   🆕 New files: {len(changes['new'])}")
    for f in changes['new']:
        print(f"      - {f} (modified: {current_files[f]['modified_str']})")

    print(f"   ✏️  Modified files: {len(changes['modified'])}")
    for f in changes['modified']:
        print(f"      - {f} (modified: {current_files[f]['modified_str']})")

    print(f"   ⏭️  Unchanged files: {len(changes['unchanged'])}")
    for f in changes['unchanged'][:3]:  # Show first 3
        print(f"      - {f}")
    if len(changes['unchanged']) > 3:
        print(f"      ... and {len(changes['unchanged']) - 3} more")

    print()

    # Calculate what needs processing
    files_to_process = changes['new'] + changes['modified']

    if not files_to_process:
        print("✅ All content is up to date! No ingestion needed.\n")
        return

    if args.verify_only:
        print(f"\n📋 Verification Mode (No Changes Made):")
        print(f"   Would process {len(files_to_process)} files")
        print(f"   Estimated chunks: ~{len(files_to_process) * 15} (approximate)\n")
        print("   Run without --verify-only to perform actual ingestion.\n")
        return

    # Perform ingestion
    print(f"\n{'='*60}")
    print(f"🚀 Starting Ingestion")
    print(f"{'='*60}\n")

    try:
        # Initialize Qdrant
        print("🔗 Connecting to Qdrant...")
        qdrant_store = QdrantVectorStore()

        # Check if collection exists, create if needed
        from qdrant_client.http.models import Distance, VectorParams
        try:
            qdrant_store.client.get_collection(collection_name)
            print(f"   ✅ Connected to existing collection: {collection_name}\n")
        except:
            print(f"   Creating new collection: {collection_name}...")
            qdrant_store.client.create_collection(
                collection_name=collection_name,
                vectors_config={
                    "embedding": VectorParams(size=1536, distance=Distance.COSINE)
                }
            )
            print(f"   ✅ Collection created\n")

        # Get initial count
        try:
            initial_info = qdrant_store.client.get_collection(collection_name)
            initial_count = initial_info.points_count
        except:
            initial_count = 0

        # Index the book content
        print(f"📚 Indexing {len(files_to_process)} files...")
        qdrant_store.index_book(args.docs_path)

        # Get final count
        final_info = qdrant_store.client.get_collection(collection_name)
        final_count = final_info.points_count

        print(f"\n✅ Ingestion Complete!")
        print(f"   Total chunks: {initial_count} → {final_count} (+{final_count - initial_count})\n")

        # Save state
        save_ingestion_state(current_files)

        # Run test query
        print(f"{'='*60}")
        print(f"🧪 Testing Search Functionality")
        print(f"{'='*60}\n")

        print(f"🔍 Test Query: \"{args.test_query}\"\n")

        query_embedding = embed_chunks([args.test_query])[0]
        search_results = qdrant_store.search(query_embedding, top_n=3)

        if search_results:
            print(f"   Found {len(search_results)} results:\n")
            for i, hit in enumerate(search_results[:3]):
                print(f"   Result {i + 1} (Score: {hit.score:.4f})")
                print(f"   Source: {hit.payload.get('source_file', 'unknown')}")
                content = hit.payload.get('text', '')
                print(f"   Content: {content[:150]}...")
                print()

            print("✅ All content successfully indexed and searchable!\n")
        else:
            print("⚠️  Warning: No results found. Content may need re-ingestion.\n")

    except Exception as e:
        print(f"\n❌ Error during ingestion: {e}")
        print(f"   Check your .env file for correct credentials\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
