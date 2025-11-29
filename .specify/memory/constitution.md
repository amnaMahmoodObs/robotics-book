<!--
Sync Impact Report:
Version change: None -> 0.1.0 (MINOR: Initial creation of the constitution)
List of modified principles: All principles are new.
Added sections: Core Principles, Project Scope & Dependencies, Development Workflow & Deliverables, Governance.
Removed sections: None.
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending
- .specify/templates/spec-template.md: ⚠ pending
- .specify/templates/tasks-template.md: ⚠ pending
- .specify/templates/commands/sp.clarify.md: ⚠ pending
- .specify/templates/commands/sp.constitution.md: ⚠ pending
- .specify/templates/commands/sp.implement.md: ⚠ pending
- .specify/templates/commands/sp.phr.md: ⚠ pending
- .specify/templates/commands/sp.plan.md: ⚠ pending
- .specify/templates/commands/sp.specify.md: ⚠ pending
- .specify/templates/phr-template.prompt.md: ⚠ pending
- README.md: ⚠ pending
- docs/quickstart.md: ⚠ pending
Follow-up TODOs: RATIFICATION_DATE needs to be set.
-->
# Physical AI & Humanoid Robotics – AI-Driven Book Project Constitution

## Core Principles

### I. Chapter-Driven Content Generation
All book chapters MUST be generated one at a time using the designated "chapter-writer" Claude Code subagent. Chapters MUST be beginner-friendly, self-contained, numbered, sectioned, and include suggested images. Content MUST be in Markdown format compatible with Docusaurus. No direct scripting for chapter generation is allowed outside the subagent.

### II. Modular Architecture for RAG Chatbot
The embedded RAG chatbot MUST utilize a backend built with FastAPI, Qdrant, and Neon Serverless Postgres. The architecture MUST support future expansion and maintainability.

### III. Reusability and Subagent Leverage
The project MUST maximize the reuse of intelligence by leveraging Claude Code subagents for specific tasks. This promotes efficiency and consistency in content generation and other automated processes.

### IV. Deployment and Accessibility
The generated book content MUST be deployed using Docusaurus to GitHub Pages, ensuring public accessibility. Optional features like personalization and Urdu translation for logged-in users MUST be supported.

### V. Incremental Development
Chapters will be developed incrementally, one at a time, allowing for focused development and review of each module. This ensures quality and adherence to the beginner-friendly and self-contained requirements.

## Project Scope & Dependencies

### In Scope:
- Minimum 3 chapters:
    1. Introduction to Physical AI & Humanoid Robotics
    2. The Robotic Nervous System (ROS 2)
    3. The Digital Twin (Gazebo & Unity)
- Use FastAPI, Qdrant, and Neon Serverless Postgres for RAG backend.
- Allow reuse of intelligence via Claude Code subagents.

### Out of Scope:
- Explicitly excluded items will be defined as the project progresses.

### External Dependencies:
- Docusaurus for static site generation and deployment to GitHub Pages.
- FastAPI for RAG chatbot backend.
- Qdrant for vector database.
- Neon Serverless Postgres for data storage.
- Claude Code subagents for chapter generation and intelligence reuse.

## Development Workflow & Deliverables

### Constraints:
- All chapters must be generated **one at a time**.
- Chapters must be beginner-friendly and self-contained.
- Use markdown format compatible with Docusaurus.
- Image suggestions must be provided for each chapter.
- No direct scripting outside of the Claude subagent for chapter generation.

### Deliverables:
1. Fully written book chapters in `front-end/docs/`.
2. Embedded RAG chatbot.
3. GitHub Pages deployment of the book.
4. Optional personalization and translation features.
5. Subagent “chapter-writer” created in Claude Code.

## Governance

This constitution supersedes all other practices. Amendments require documentation, approval, and a migration plan. All PRs/reviews must verify compliance with these principles. Complexity must be justified.

**Version**: 0.1.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2025-11-28
