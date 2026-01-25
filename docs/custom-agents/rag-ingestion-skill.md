# RAG Ingestion Skill Documentation

## Overview

The **RAG Ingestion Skill** is a custom Claude Code skill that intelligently updates the Qdrant vector database when you add or modify book chapters. This ensures your chatbot always has access to the latest content without manual intervention.

## Location

```
.claude/skills/rag-ingestion/
├── SKILL.md          # Skill definition for Claude Code
├── README.md         # User documentation
```

## How It Works

### Architecture

```
User adds/modifies chapter
        ↓
Claude Code invokes skill
        ↓
smart_ingest.py analyzes changes
        ↓
Only changed files ingested
        ↓
Qdrant updated with new embeddings
        ↓
Verification test runs
        ↓
User gets success report
```

### Smart Features

1. **Change Detection**
   - Tracks last modification time of each file
   - Only processes new or modified files
   - Saves ingestion state in `.rag_ingestion_state.json`

2. **Incremental Updates**
   - Default mode: Only ingest changed files
   - Force mode: Re-ingest everything (use if database corrupted)
   - Verify mode: Preview changes without ingesting

3. **Automatic Verification**
   - Runs test query after ingestion
   - Confirms embeddings are searchable
   - Reports success/failure clearly

## Usage

### Invoke via Claude Code

Simply tell Claude:
```
"I added a new chapter about sensors, please update the RAG database"
```

Claude will automatically invoke the skill and handle everything!

### Manual Command Line

**Check what needs updating**:
```bash
cd /Volumes/Important/AI Agents/robotics-book
python3 -m rag_ingestion.smart_ingest --verify-only
```

**Perform incremental update**:
```bash
python3 -m rag_ingestion.smart_ingest
```

**Force full re-ingestion**:
```bash
python3 -m rag_ingestion.smart_ingest --force
```

**Custom test query**:
```bash
python3 -m rag_ingestion.smart_ingest --test-query "What are actuators?"
```

## Implementation Details

### File Structure

**Skill Definition** (`.claude/skills/rag-ingestion/SKILL.md`):
- Defines skill purpose and behavior
- Provides step-by-step instructions for Claude
- Includes example scenarios
- Documents acceptance criteria

**Ingestion Script** (`rag_ingestion/smart_ingest.py`):
- Scans `front-end/docs/` for markdown files
- Compares with last ingestion state
- Processes only changed files
- Updates Qdrant collection
- Runs verification tests
- Saves new state

**State File** (`.rag_ingestion_state.json`):
```json
{
  "chapter-1-introduction.md": {
    "path": "front-end/docs/chapter-1-introduction.md",
    "modified": 1706121454.0,
    "modified_str": "2026-01-24 12:15:54"
  },
  ...
}
```

### Key Functions

**`load_ingestion_state()`**
- Loads previous ingestion state from JSON
- Returns empty dict if first run

**`get_markdown_files(docs_path)`**
- Scans directory for `.md` files
- Gets modification timestamps
- Returns dict of file info

**`detect_changes(current, last_state, force)`**
- Compares current files with last state
- Returns lists of: new, modified, unchanged files
- If `force=True`, marks all as modified

**`main()`**
- Parses command line arguments
- Runs change detection
- Performs ingestion if needed
- Verifies with test query
- Saves new state

## Benefits for Hackathon

### Reusable Intelligence (+50 points)

This skill demonstrates:
- ✅ **Automation**: Eliminates manual RAG updates
- ✅ **Intelligence**: Smart change detection
- ✅ **Reusability**: Works for any number of chapters
- ✅ **Integration**: Seamless with existing pipeline
- ✅ **Cost Optimization**: Only processes what's needed

### User Experience

**Before (Manual)**:
1. User adds chapter
2. User forgets to update RAG
3. Chatbot gives outdated answers
4. User confused why new content not working

**After (With Skill)**:
1. User adds chapter
2. User tells Claude "update RAG"
3. Skill automatically detects changes
4. Only new content processed
5. Chatbot immediately knows new content

### Cost Savings

**Without Smart Ingestion**:
- Re-embed all 50 chapters = 50 × embedding cost
- Every update = full re-ingestion
- Expensive and slow

**With Smart Ingestion**:
- Add 1 chapter = 1 × embedding cost
- Modify 2 chapters = 2 × embedding cost
- 96% cost reduction on typical updates!

## Testing

Test the skill with these scenarios:

### Scenario 1: Add New Chapter
```bash
# Create a new chapter
echo "# Chapter 4: Sensors" > front-end/docs/chapter-4-sensors.md

# Tell Claude to update RAG
# Or run manually:
python3 -m rag_ingestion.smart_ingest

# Expected: Only chapter-4 is ingested
```

### Scenario 2: Modify Existing Chapter
```bash
# Edit a chapter
echo "Updated content" >> front-end/docs/chapter-1-introduction.md

# Update RAG
python3 -m rag_ingestion.smart_ingest

# Expected: Only chapter-1 is re-ingested
```

### Scenario 3: Verify Before Updating
```bash
# Check what would be updated
python3 -m rag_ingestion.smart_ingest --verify-only

# Expected: Shows list without making changes
```

## Troubleshooting

### State File Issues

**Problem**: Skill re-ingests everything each time

**Solution**: Delete `.rag_ingestion_state.json` and run once with `--force` to rebuild state

### Permission Errors

**Problem**: Can't write state file

**Solution**: Check write permissions in project root directory

### Connection Errors

**Problem**: Can't connect to Qdrant

**Solution**:
1. Verify `.env` has correct `QDRANT_URL` and `QDRANT_API_KEY`
2. Check Qdrant cluster is running
3. Test connection in browser: `https://your-cluster-url:6333/collections`

## Future Enhancements

Potential improvements:
- [ ] Email notifications when ingestion completes
- [ ] Slack integration for team updates
- [ ] Automatic scheduling (cron job)
- [ ] Multi-language support detection
- [ ] Content quality validation before ingesting
- [ ] Rollback capability if ingestion fails

## Conclusion

The RAG Ingestion Skill is a powerful demonstration of reusable intelligence that:
- Saves time and money
- Prevents user errors
- Ensures chatbot stays current
- Works seamlessly with Claude Code

**Hackathon Impact**: This skill alone could earn you the full +50 bonus points for custom agents!
