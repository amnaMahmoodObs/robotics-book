---
id: 0001
title: Update project constitution for Physical AI Robotics book
stage: constitution
date: 2025-11-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: jamalazfarkhan
command: /sp.constitution
labels: ["governance", "project-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md (modified)
tests:

---

## Prompt

```text
Title: Physical AI & Humanoid Robotics – AI-Driven Book Project

Purpose:
- Create a beginner-friendly book on Physical AI and Humanoid Robotics.
- Each chapter will be generated one at a time using a Claude Code subagent called "chapter-writer".
- Chapters will be numbered, sectioned, and include suggested images.
- Content will be deployed using Docusaurus to GitHub Pages.
- Include an embedded RAG chatbot that answers questions based on the book content.
- Support optional personalization and Urdu translation per chapter for logged-in users.

Scope:
- Minimum 3 chapters:
    1. Introduction to Physical AI & Humanoid Robotics
    2. The Robotic Nervous System (ROS 2)
    3. The Digital Twin (Gazebo & Unity)
- Use FastAPI, Qdrant, and Neon Serverless Postgres for RAG backend.
- Allow reuse of intelligence via Claude Code subagents.

Constraints:
- All chapters must be generated **one at a time**.
- Chapters must be beginner-friendly and self-contained.
- Use markdown format compatible with Docusaurus.
- Image suggestions must be provided for each chapter.
- No direct scripting outside of the Claude subagent for chapter generation.

Deliverables:
1. Fully written book chapters in `front-end/docs/`.
2. Embedded RAG chatbot.
3. GitHub Pages deployment of the book.
4. Optional personalization and translation features.
5. Subagent “chapter-writer” created in Claude Code.
```

## Response snapshot

Created and updated the project constitution based on the provided details, outlining the project's purpose, scope, constraints, deliverables, core principles, and governance. Generated an initial version 0.1.0.

## Outcome

- ✅ Impact: Constitution established.
- 🧪 Tests: N/A
- 📁 Files: Modified .specify/memory/constitution.md
- 🔁 Next prompts: Next steps include updating other project templates and addressing the `RATIFICATION_DATE` TODO in the constitution.
- 🧠 Reflection: The initial constitution has been set up, providing a foundational document for the project. Further work is needed to propagate these changes to other templates.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Propagate constitution changes to other templates and fill `RATIFICATION_DATE`.
