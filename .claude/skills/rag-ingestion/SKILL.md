# RAG Ingestion Skill

**Purpose**: Intelligently update Qdrant vector database when book chapters are added or modified

**Use this skill when**:
- You've added new chapters to `front-end/docs/`
- You've modified existing chapter content
- Chatbot responses seem outdated or missing new content
- You want to verify what content is currently indexed

---

## What This Skill Does

This skill provides intelligent RAG (Retrieval-Augmented Generation) content management:

1. **Scans** `front-end/docs/` for all markdown files
2. **Detects changes** by comparing modification times with last ingestion
3. **Runs ingestion** only for new/modified content (or all if forced)
4. **Updates** Qdrant vector database with embeddings
5. **Verifies** the update was successful with test queries
6. **Reports** detailed summary of what was updated

---

## Task Instructions

When this skill is invoked, you should:

### Step 1: Assess Current State
- Check when Qdrant collection was last updated
- List all markdown files in `front-end/docs/`
- Identify which files are new or modified since last ingestion
- Report findings to user

### Step 2: Determine Ingestion Strategy
Ask the user (or decide based on context):
- **Incremental**: Only ingest new/modified files (recommended, faster)
- **Full**: Re-ingest everything (use if embeddings might be corrupted)
- **Verify Only**: Just report what would be updated without actually doing it

### Step 3: Run Ingestion
Execute the ingestion script:
```bash
python3 -m rag_ingestion.smart_ingest [--force] [--verify-only] [--test-query "your query"]
```

### Step 4: Verify Success
- Check that new files appear in Qdrant
- Run test queries to verify content is searchable
- Report number of chunks added/updated
- Show sample search results

### Step 5: Report Results
Provide a summary including:
- Files processed (new, modified, unchanged)
- Total chunks in database
- Test query results
- Any errors or warnings

---

## Parameters

- `--force`: Re-ingest all files regardless of modification time
- `--verify-only`: Check what would be updated without actually ingesting
- `--test-query <query>`: Run a specific test search after ingestion (default: "What is robotics?")

---

## Expected Outputs

**Success Case**:
```
✅ RAG Ingestion Complete!

Summary:
- New files: 2 (chapter-4.md, chapter-5.md)
- Modified files: 1 (chapter-1-introduction.md)
- Unchanged files: 2
- Total chunks ingested: 47 → 73 (+26)
- Collection: robotics-book

Test Query: "What is robotics?"
Top Result (score: 0.85): chapter-1-introduction.md
"Robotics is the interdisciplinary field..."

✅ All content successfully indexed and searchable!
```

**Verify-Only Case**:
```
📋 Ingestion Preview (No Changes Made):

Would process:
- NEW: chapter-4-sensors.md (modified: 2026-01-24 14:30)
- MODIFIED: chapter-1-introduction.md (modified: 2026-01-24 12:15)

Would skip:
- chapter-2-ros2.md (unchanged since last ingestion)
- chapter-3-digital-twin.md (unchanged since last ingestion)

Estimated: ~24 new chunks would be added

Run without --verify-only to perform actual ingestion.
```

---

## Error Handling

If ingestion fails:
1. Check Qdrant connection (verify API key and URL in `.env`)
2. Check OpenAI API key is valid
3. Verify markdown files are properly formatted
4. Check for network connectivity issues
5. Report specific error to user with suggested fix

---

## Integration Points

This skill integrates with:
- **Qdrant Cloud**: Vector database storing embeddings
- **OpenAI API**: For generating embeddings
- **Book Content**: Markdown files in `front-end/docs/`
- **Backend**: RAG agent uses the updated embeddings

---

## Acceptance Criteria

- ✅ Correctly detects all new `.md` files in `front-end/docs/`
- ✅ Detects modified `.md` files by comparing timestamps
- ✅ Successfully ingests content to Qdrant
- ✅ Verifies embeddings are searchable with test queries
- ✅ Reports clear, actionable summary of changes
- ✅ Handles errors gracefully with helpful messages
- ✅ Supports both incremental and full re-ingestion

---

## Example Usage Scenarios

### Scenario 1: Added New Chapters
**User**: "I just added Chapter 4 and Chapter 5. Can you update the RAG database?"

**Agent**:
1. Invokes rag-ingestion skill
2. Scans docs/ and finds 2 new files
3. Runs ingestion for those files only
4. Reports success with chunk count
5. Runs test query to verify

### Scenario 2: Modified Existing Content
**User**: "I updated the introduction chapter with better examples."

**Agent**:
1. Invokes skill
2. Detects chapter-1-introduction.md has newer timestamp
3. Re-ingests just that file
4. Confirms chatbot now has updated content

### Scenario 3: Verify Before Ingesting
**User**: "What content needs to be re-indexed?"

**Agent**:
1. Invokes skill with --verify-only
2. Reports list of changed files
3. Asks if user wants to proceed with ingestion

---

## Notes for Hackathon Judges

This skill demonstrates:
- **Reusable Intelligence**: Can be invoked anytime, not hardcoded for specific files
- **Smart Automation**: Only processes what's needed (incremental updates)
- **Error Handling**: Gracefully handles connection issues, bad files, etc.
- **Integration**: Works seamlessly with existing RAG pipeline
- **User Experience**: Clear reporting and verification steps
- **Bonus Points**: Custom Claude Code Skill (+50 points)
