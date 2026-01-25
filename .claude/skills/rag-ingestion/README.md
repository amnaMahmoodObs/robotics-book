# RAG Ingestion Skill

## Quick Start

This skill helps you keep your RAG chatbot up-to-date when you add or modify book chapters.

### How to Use

Simply say to Claude Code:
- "Update the RAG database"
- "I added new chapters, can you ingest them?"
- "The chatbot is outdated, please refresh the content"

Claude will invoke this skill automatically and handle the ingestion for you!

### Manual Usage

You can also run the script directly:

**Check what needs updating (doesn't change anything)**:
```bash
python3 -m rag_ingestion.smart_ingest --verify-only
```

**Update only changed files** (recommended):
```bash
python3 -m rag_ingestion.smart_ingest
```

**Force re-ingest everything**:
```bash
python3 -m rag_ingestion.smart_ingest --force
```

**Run with custom test query**:
```bash
python3 -m rag_ingestion.smart_ingest --test-query "What are sensors?"
```

## What It Does

1. **Scans** your `front-end/docs/` directory for markdown files
2. **Detects** which files are new or have been modified
3. **Ingests** only the changed content (saves time and API costs!)
4. **Updates** Qdrant vector database with new embeddings
5. **Verifies** the update worked with a test search
6. **Reports** exactly what was updated

## Smart Features

### Change Detection
The skill tracks when files were last ingested in `.rag_ingestion_state.json`. This means:
- Only new files are processed
- Only modified files are re-indexed
- Unchanged files are skipped (faster, cheaper!)

### State Tracking
After each successful ingestion, the script saves a state file that includes:
- Which files were ingested
- When they were modified
- Next run will use this to detect changes

### Verification Mode
Use `--verify-only` to see what would be updated without actually doing it:
```bash
python3 -m rag_ingestion.smart_ingest --verify-only
```

This is useful for:
- Checking if you need to update
- Understanding what changed
- Planning before expensive API calls

## Example Output

### Verify Mode
```
============================================================
🔍 RAG Ingestion Analysis
============================================================

📂 Scanning: front-end/docs/
   Found 5 markdown files

📊 Change Detection:
   🆕 New files: 2
      - chapter-4-sensors.md (modified: 2026-01-24 14:30:00)
      - chapter-5-actuators.md (modified: 2026-01-24 15:00:00)
   ✏️  Modified files: 1
      - chapter-1-introduction.md (modified: 2026-01-24 12:15:00)
   ⏭️  Unchanged files: 2
      - chapter-2-ros2.md
      - chapter-3-digital-twin.md

📋 Verification Mode (No Changes Made):
   Would process 3 files
   Estimated chunks: ~45 (approximate)

   Run without --verify-only to perform actual ingestion.
```

### Actual Ingestion
```
============================================================
🔍 RAG Ingestion Analysis
============================================================

📂 Scanning: front-end/docs/
   Found 5 markdown files

📊 Change Detection:
   🆕 New files: 2
   ✏️  Modified files: 1
   ⏭️  Unchanged files: 2

============================================================
🚀 Starting Ingestion
============================================================

🔗 Connecting to Qdrant...
   ✅ Connected to existing collection: robotics-book

📚 Indexing 3 files...
Indexed 47 chunks from 'front-end/docs/' into Qdrant.

✅ Ingestion Complete!
   Total chunks: 47 → 73 (+26)

============================================================
🧪 Testing Search Functionality
============================================================

🔍 Test Query: "What is robotics?"

   Found 3 results:

   Result 1 (Score: 0.8532)
   Source: chapter-1-introduction.md
   Content: Robotics is the interdisciplinary field combining
   mechanical engineering, electrical engineering, and computer
   science...

✅ All content successfully indexed and searchable!
```

## Troubleshooting

### Error: Missing environment variables
**Fix**: Check your `.env` file has:
- `QDRANT_URL`
- `QDRANT_API_KEY`
- `OPENAI_API_KEY`
- `QDRANT_COLLECTION_NAME`

### Error: Connection to Qdrant failed
**Fix**:
1. Verify Qdrant URL is correct
2. Check API key is valid
3. Ensure Qdrant cluster is running
4. Test connection in browser

### Error: No files found
**Fix**:
- Check `front-end/docs/` directory exists
- Ensure it contains `.md` files
- Verify file permissions

## For Hackathon Judges

This skill demonstrates:

✅ **Reusable Intelligence**: Works for any number of chapters, any time
✅ **Smart Automation**: Only processes what's needed
✅ **Cost Optimization**: Avoids re-embedding unchanged content
✅ **Error Handling**: Clear messages for common issues
✅ **User Experience**: Beautiful formatted output
✅ **Integration**: Seamlessly works with existing RAG pipeline

**Bonus Points**: Custom Claude Code Skill (+50 points)
