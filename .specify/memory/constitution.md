# Robotics Book RAG Chatbot Constitution

<!--
Sync Impact Report:
Version change: [unversioned] → 1.0.0
Modified principles: Initial creation
Added sections: Core Principles (6 principles), Technology Stack, Development Workflow, Governance
Removed sections: None
Templates requiring updates:
  ✅ Updated: All templates align with new constitution
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
Follow-up TODOs: None
-->

## Core Principles

### I. AI-Spec-Driven Development (MANDATORY)

All features MUST be developed using Spec-Kit Plus methodology:
- Every feature begins with a specification in `specs/<feature>/spec.md`
- Architecture decisions documented in `specs/<feature>/plan.md`
- Implementation tracked via testable tasks in `specs/<feature>/tasks.md`
- Use Claude Code as primary development tool for all work
- All user interactions and significant decisions recorded as Prompt History Records (PHRs)

**Rationale**: Structured development ensures traceability, maintainability, and alignment with hackathon requirements for spec-driven approach.

### II. Documentation-First Content Creation

Book content MUST prioritize educational value and accessibility:
- Docusaurus-based content with clear chapter structure
- Content written for learners with varying technical backgrounds
- All technical concepts explained with examples and visuals
- Deployable to GitHub Pages with automated CI/CD
- Content structured for optimal RAG retrieval (clear sections, semantic headings)

**Rationale**: The primary deliverable is an educational robotics book that serves real learning needs while enabling intelligent question-answering.

### III. RAG-Enabled Interactive Learning (CORE DELIVERABLE)

The embedded RAG chatbot is non-negotiable and MUST provide:
- Full book content retrieval using Qdrant vector database
- Context-aware responses using OpenAI Agents/ChatKit SDKs
- Text selection-based queries (user highlights text → chatbot answers about selection)
- FastAPI backend with Neon Serverless Postgres for persistence
- Qdrant Cloud Free Tier integration for vector embeddings
- Real-time streaming responses for better UX

**Rationale**: The chatbot transforms static documentation into an interactive learning experience, worth 100 base points.

### IV. Reusable Intelligence Through Agents (BONUS: +50 points)

Maximize value through custom Claude Code tooling:
- Create Claude Code Subagents for repetitive tasks (chapter generation, content validation, deployment)
- Build Agent Skills for domain-specific operations (RAG ingestion, content formatting, chatbot testing)
- Document all custom agents and skills in `docs/custom-agents/`
- Ensure agents are configurable and reusable across chapters/features

**Rationale**: Demonstrates advanced understanding of AI-assisted development and creates lasting productivity improvements.

### V. Personalized Learning Experience (BONUS: +150 points total)

Implement user-centric features to maximize bonus points:

**Authentication & Profiling (+50 points)**:
- Better-auth.com integration for signup/signin
- Capture user background (software/hardware experience) at registration
- Store profiles in Neon Postgres with privacy considerations
- Use profiles to personalize chatbot responses and content recommendations

**Content Personalization (+50 points)**:
- Chapter-level "Personalize" button adjusting complexity/examples based on user profile
- Dynamic content adaptation (beginner → more explanations; expert → advanced topics)
- Persist user preferences across sessions

**Multi-Language Support (+50 points)**:
- Chapter-level "Translate to Urdu" button
- High-quality translation using LLM with technical term preservation
- Toggle between English and Urdu without page reload

**Rationale**: These features demonstrate full-stack capability and create genuine user value beyond base requirements.

### VI. Test-Driven Quality Assurance

Testing MUST cover all critical paths:
- Backend: pytest for API endpoints, RAG retrieval accuracy, database operations
- Frontend: Component testing for chatbot, authentication flows, personalization features
- Integration: End-to-end tests for user journeys (signup → personalize → query chatbot)
- Performance: Load testing for RAG queries, response time benchmarks (< 2s for queries)
- Validate embeddings quality and retrieval relevance

**Rationale**: Hackathon projects often sacrifice testing; demonstrating robust QA differentiates this submission.

## Technology Stack

### Required Technologies (Base Deliverable)

**Frontend**:
- Docusaurus v3+ (content platform)
- React 18+ (chatbot UI components)
- GitHub Pages (hosting)

**Backend**:
- Python 3.9+
- FastAPI (API framework)
- OpenAI Agents SDK / ChatKit SDK (LLM integration)
- Qdrant Cloud Free Tier (vector database)
- Neon Serverless Postgres (relational data)

**Development Tools**:
- Claude Code (primary AI assistant)
- Spec-Kit Plus (development methodology)
- Git/GitHub (version control, deployment)

### Bonus Feature Technologies

**Authentication (+50 points)**:
- Better-auth.com (authentication service)
- Secure session management
- User profile database schema in Neon Postgres

**Personalization & Translation (+100 points)**:
- OpenAI GPT-4 (content adaptation and translation)
- Client-side state management (React Context or Zustand)
- Caching layer for translated content

**Custom Agents (+50 points)**:
- Claude Code Agent SDK
- Custom subagent configurations
- Reusable skill definitions

## Development Workflow

### Feature Development Process

1. **Specification Phase**:
   - Create feature spec using `/sp.specify` or manually in `specs/<feature>/spec.md`
   - Define user stories, acceptance criteria, and constraints
   - Get approval before proceeding

2. **Planning Phase**:
   - Run `/sp.plan` to generate architecture plan in `specs/<feature>/plan.md`
   - Document technology choices, API contracts, data models
   - Identify architectural decisions requiring ADRs (use `/sp.adr` for significant decisions)

3. **Task Breakdown**:
   - Execute `/sp.tasks` to generate actionable tasks in `specs/<feature>/tasks.md`
   - Ensure tasks include test cases and acceptance criteria
   - Prioritize tasks by dependency order

4. **Implementation Phase**:
   - Follow Red-Green-Refactor cycle where applicable
   - Write tests before implementation for critical paths
   - Create Prompt History Records (PHRs) for all significant work sessions
   - Update tasks.md as progress is made

5. **Quality Gates**:
   - All tests passing (pytest for backend, npm test for frontend)
   - Code reviewed (self-review checklist in `specs/<feature>/tasks.md`)
   - Documentation updated (README, API docs, user guides)
   - No hardcoded secrets (use .env, validate with git grep)

6. **Deployment**:
   - Backend deployed to compatible host (Render, Railway, etc.)
   - Frontend deployed to GitHub Pages via CI/CD
   - Environment variables configured in deployment platform
   - Health checks passing

### Architectural Decision Records (ADRs)

**When to create ADRs** (must meet ALL three criteria):
- **Impact**: Long-term consequences for architecture (framework choice, data model, API design, security model, platform)
- **Alternatives**: Multiple viable options with significant tradeoffs
- **Scope**: Cross-cutting concern influencing system design

**ADR process**:
1. During planning, identify decisions meeting criteria above
2. Suggest to user: "📋 Architectural decision detected: [brief]. Document reasoning and tradeoffs? Run `/sp.adr [decision-title]`"
3. Wait for consent; never auto-create
4. Document in `history/adr/ADR-NNNN-<slug>.md` using template

**Example ADR-worthy decisions**:
- Choosing Qdrant over Pinecone/Weaviate for vector storage
- Using Better-auth vs. NextAuth vs. custom JWT auth
- Structuring chatbot state management (Context vs. Redux vs. Zustand)
- LLM selection for RAG responses (GPT-4 vs. Claude vs. Llama)

### Prompt History Records (PHRs)

**Automatic PHR creation required** after:
- Implementation work (code changes, new features)
- Planning and architecture discussions
- Debugging sessions
- Spec/task/plan generation
- Multi-step workflows

**PHR routing** (all under `history/prompts/`):
- `constitution` stage → `history/prompts/constitution/`
- Feature stages (spec, plan, tasks, red, green, refactor, explainer, misc) → `history/prompts/<feature-name>/`
- `general` stage → `history/prompts/general/`

**Creation process**:
1. Determine stage and generate 3-7 word title
2. Run `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
3. Fill all placeholders in YAML frontmatter and body sections
4. Embed full verbatim user prompt and concise assistant response
5. Validate: no unresolved placeholders, correct routing, coherent metadata

## Governance

### Constitution Authority

This constitution supersedes all other development practices and guidelines. All code reviews, PRs, and architectural decisions MUST verify compliance with these principles.

### Amendment Process

1. **Proposal**: Document proposed change with rationale and impact analysis
2. **Version Bump Decision**:
   - MAJOR: Backward-incompatible governance changes, principle removals/redefinitions
   - MINOR: New principles added, material expansions to guidance
   - PATCH: Clarifications, wording improvements, non-semantic fixes
3. **Update**: Modify constitution with sync impact report (HTML comment at top)
4. **Propagation**: Update dependent templates (plan, spec, tasks, commands)
5. **Commit**: Use message format `docs: amend constitution to vX.Y.Z (<summary>)`

### Compliance Review

**Pre-commit checks**:
- No secrets committed (API keys, tokens, credentials)
- Test coverage maintained or improved
- Documentation updated for user-facing changes
- PHR created for significant work

**Feature completion criteria**:
- All tasks in tasks.md marked complete
- Acceptance criteria met and validated
- Deployment successful with health checks passing
- User-facing documentation complete

### Hackathon Scoring Checklist

**Base Functionality (100 points)**:
- [ ] Docusaurus book deployed to GitHub Pages
- [ ] RAG chatbot embedded and functional
- [ ] OpenAI Agents/ChatKit SDK integration working
- [ ] Qdrant vector database storing book embeddings
- [ ] Neon Postgres database operational
- [ ] Text selection-based query feature working

**Bonus: Custom Agents (+50 points)**:
- [ ] At least 2 custom Claude Code Subagents created
- [ ] At least 1 reusable Agent Skill defined
- [ ] Agents documented with usage examples

**Bonus: Authentication & Profiling (+50 points)**:
- [ ] Better-auth.com signup/signin functional
- [ ] User background questionnaire at signup
- [ ] Profile data stored in Neon Postgres
- [ ] Chatbot uses profile for context

**Bonus: Content Personalization (+50 points)**:
- [ ] Personalize button on each chapter
- [ ] Content adapts based on user profile
- [ ] Preferences persist across sessions

**Bonus: Multi-Language Support (+50 points)**:
- [ ] Translate to Urdu button on each chapter
- [ ] High-quality translation preserving technical terms
- [ ] Toggle between languages without reload

**Version**: 1.0.0 | **Ratified**: 2026-01-24 | **Last Amended**: 2026-01-24
