---
id: 0002
title: Recreate hackathon project constitution
stage: constitution
date: 2026-01-24
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: developer
command: /sp.constitution
labels: ["constitution", "hackathon", "initialization", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - None
---

## Prompt

You are required to complete a unified book project using Claude Code and Spec-Kit Plus. The core deliverables are:

1. AI/Spec-Driven Book Creation: Write a book using Docusaurus and deploy it to GitHub Pages. You will use Spec-Kit Plus ( https://github.com/panaversity/spec-kit-plus/ ) and Claude Code ( https://www.claude.com/product/claude-code ) to write the book.

2. Integrated RAG Chatbot Development: Build and embed a Retrieval-Augmented Generation (RAG) chatbot within the published book. This chatbot, utilizing the OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres database, and Qdrant Cloud Free Tier, must be able to answer user questions about the book's content, including answering questions based only on text selected by the user.

3. Participants will receive points out of 100, for base functionality defined above.

4. Participants can earn up to 50 extra bonus points by creating and using reusable intelligence via Claude Code Subagents and Agent Skills in the book project.

5. Participants can receive up to 50 extra bonus points if they also implement Signup and Signin using https://www.better-auth.com/ At signup you will ask questions from the user about their software and hardware background. Knowing the background of the user we will be able to personalize the content.

6.  Participants can receive up to 50 extra bonus points if the logged user can personalise the content in the chapters by pressing a button at the start of each chapter.

7. Participants can receive up to 50 extra bonus points if the logged user can translate the content in Urdu in the chapters by pressing a button at the start of each chapter.
 this is a hackathon project. i had mmade constitution earlier but somehow it was woverwritten soo writing it again.

## Response snapshot

Created comprehensive project constitution v1.0.0 for robotics book RAG chatbot hackathon project. Constitution includes:

- 6 core principles: AI-Spec-Driven Development, Documentation-First Content Creation, RAG-Enabled Interactive Learning, Reusable Intelligence Through Agents, Personalized Learning Experience, Test-Driven Quality Assurance
- Technology stack specifications for base deliverable and bonus features
- Detailed development workflow with feature development process, ADR guidelines, and PHR creation process
- Governance section with amendment process, compliance review, and hackathon scoring checklist (100 base points + up to 200 bonus points)
- Sync impact report documenting version change from unversioned to 1.0.0

All placeholder tokens replaced with concrete values. Constitution ratified 2026-01-24.

## Outcome

- ✅ Impact: Established foundational governance document defining all project principles, workflows, and success criteria for hackathon submission
- 🧪 Tests: None (documentation artifact)
- 📁 Files: Created/updated .specify/memory/constitution.md
- 🔁 Next prompts: Begin feature development using /sp.specify for new features, ensure PHR creation for all subsequent work
- 🧠 Reflection: Constitution comprehensively captures hackathon requirements including base functionality (100 pts) and all bonus opportunities (custom agents +50, auth +50, personalization +50, translation +50). Clear scoring checklist enables tracking progress toward maximum 300 points.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A (initial constitution creation)
- Prompt variant (if applicable): Standard constitution creation workflow
- Next experiment (smallest change to try): Begin implementing base RAG chatbot functionality or bonus features per hackathon scoring priorities
