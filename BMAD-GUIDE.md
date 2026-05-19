# BMAD Integration Guide (Continue, Junie & Claude Code)

Welcome to the **Business Modular Agentic Development (BMAD)** framework, version 6.0.0-Beta.4, now fully integrated into your **Continue** IDE plugin, **Junie** autonomous agent, and **Claude Code** CLI.

This guide explains how to orchestrate a complete project lifecycle—from initial discovery to production-ready implementation—using specialized AI agents and structured workflows.

---

## Using BMAD with Claude Code (New!)

Claude Code integrates with BMAD natively via the `.claude/` directory, which contains agent shards and rules adapted for Claude Code's capabilities.

### How Claude Code works with BMAD:
- **Agent Shards**: Each BMAD persona is available as an agent shard in `.claude/agents/`. These lightweight files reference the full agent definitions in `_bmad/bmm/agents/` or `_bmad/core/agents/`.
- **Step-File Discipline**: The rule in `.claude/rules/step-file-architecture.md` enforces sequential step execution. Claude Code will read a workflow file, execute only the current step, and ask for permission before moving to the next.
- **Context-Aware Navigation**: Ask Claude Code to load a specific workflow (e.g., "Start the PRD workflow") and it will find the files in `_bmad/`.
- **CLAUDE.md**: The `CLAUDE.md` file at the project root provides persistent context about the framework structure, agents, and conventions.

### Example prompts for Claude Code:
- "Adopte le persona de Mary (analyst) et démarre une découverte de projet en suivant `_bmad/bmm/workflows/1-analysis/create-product-brief/workflow.md`."
- "En tant que John (PM), crée un PRD en suivant le workflow dans `_bmad/bmm/workflows/2-plan-workflows/create-prd/workflow.md`."
- "En tant que Winston (architect), conçois l'architecture à partir du PRD dans `_bmad-output/planning-artifacts/`."
- "En tant que Barry (quick-flow), implémente rapidement cette fonctionnalité."

### Claude Code Specifics:
- Claude Code has access to the full filesystem and can read workflow steps, templates, and config files directly.
- No need to manually provide context files — Claude Code can explore `_bmad/` autonomously.
- The `.claude/rules/` directory enforces BMAD rules automatically when relevant files are loaded.
- Output artifacts are written to `_bmad-output/` as configured in `_bmad/bmm/config.yaml`.

---

## Using BMAD with Junie

Junie is an autonomous agent that follows the BMAD framework natively via the `.junie/` directory.

### How Junie works with BMAD:
- **Automatic Persona Adoption**: Junie detects your intent (e.g., "Analyze this feature") and automatically adopts the relevant BMAD persona (Mary, Winston, etc.) by reading `.junie/agents/`.
- **Step-File Discipline**: Junie follows the "Step-File Architecture" defined in `.junie/bmad-framework.md`. It will read a workflow file, execute only the current step, and ask for your permission before moving to the next.
- **Context-Aware Navigation**: You don't need to specify context providers. Just ask Junie to "Start the PRD workflow in _bmad", and she will find the files.

### Example prompts for Junie:
- "Junie, démarre une découverte de projet (Phase 1) en utilisant le dossier _bmad/bmm/workflows/1-analysis."
- "À partir du brief produit dans _bmad-output, crée un PRD en suivant le workflow de solutioning."
- "Implémente la story #5 en respectant l'architecture définie."

---

## Executing the Full BMAD Lifecycle

The BMAD method follows a disciplined, phase-based approach. Each phase is handled by a specific agent with its own persona and principles.

### Phase 1: Strategic Analysis (Mary)
*   **Continue**: `/analyst`
*   **Claude Code**: "Adopte le persona de Mary et démarre l'analyse."
*   **Workflow**: `_bmad/bmm/workflows/1-analysis/`
*   **Goal**: Define the problem space, perform market research, and create a **Product Brief**.
*   **How to start (Continue)**:
    > `/analyst Start a new project discovery. Use @Project-Context as a template and @BMAD-Workflows-Analysis for discovery workflows.`

### Phase 2: Product Strategy & Planning (John)
*   **Continue**: `/pm` or `/prd`
*   **Claude Code**: "Adopte le persona de John et crée un PRD."
*   **Workflow**: `_bmad/bmm/workflows/2-plan-workflows/create-prd/`
*   **Goal**: Translate the Brief into a comprehensive **Product Requirements Document (PRD)**.
*   **How to start (Continue)**:
    > `/pm Create a PRD based on the project brief in _bmad-output/planning-artifacts/. Use @BMAD-Workflows-Planning to find the create-prd workflow.`

### Phase 3: Technical Architecture (Winston)
*   **Continue**: `/architect` or `/arch`
*   **Claude Code**: "Adopte le persona de Winston et conçois l'architecture."
*   **Workflow**: `_bmad/bmm/workflows/3-solutioning/create-architecture/`
*   **Goal**: Define the technical stack, data flows, and system components.
*   **How to start (Continue)**:
    > `/architect Design the architecture for the PRD at [path/to/PRD.md]. Load the create-architecture workflow from @BMAD-Workflows-Solutioning.`

### Phase 4: Implementation (Bob & Amelia)
*   **Continue**: `/sprint` (for Bob/Scrum Master) then `/dev` (for Amelia/Dev)
*   **Claude Code**: "Adopte le persona de Bob et planifie le sprint." then "Adopte le persona d'Amelia et implémente la story."
*   **Workflow**: `_bmad/bmm/workflows/4-implementation/`
*   **Goal**: Break the PRD into stories and implement them with 100% test coverage.
*   **How to start (Continue)**:
    > `/sprint Plan the first sprint based on the PRD and Architecture. Use @BMAD-Workflows-Implementation for the sprint-planning workflow.`
    > `/dev Implement story [ID] from the sprint plan. Use @BMAD-Workflows-Implementation for the dev-story workflow.`

### Quick Flow (Barry)
*   **Continue**: `/quick-dev`
*   **Claude Code**: "Adopte le persona de Barry et implémente rapidement."
*   **Workflow**: `_bmad/bmm/workflows/bmad-quick-flow/`
*   **Goal**: Fast one-off development tasks with minimal ceremony.

---

## Tips and Tricks

*   **Granular Context (@)**: Avoid using `@BMAD-Core` which loads the entire framework (400+ files). Use targeted providers like `@BMAD-Workflows-Analysis`, `@BMAD-Workflows-Planning`, etc.
*   **Just-In-Time (JIT) Loading**: Always provide the specific step file (e.g., `@step-01-init.md`) as context. The agents are instructed to wait for your input after each step.
*   **The Tri-Modal Pattern**: Most BMAD workflows support **Create**, **Validate**, and **Edit** modes. Use `/prd -v` to validate an existing PRD or `/arch -e` to refine your design.
*   **Party Mode**: For complex architectural or product decisions, use `/brainstorm` or manually mention multiple agents to trigger a multi-perspective discussion.
*   **Excalidraw Integration**: Need a diagram? Use Sally (UX) or Winston (Architect) and ask for an Excalidraw output to visualize your data flows.

---

## Caveats

*   **Manual Step Advancement (Continue)**: Continue does not automatically load the "next" file in a sequence. You must manually add the next step file to the context (using `@file`) when prompted by the agent.
*   **Claude Code Step Advancement**: Claude Code can read files autonomously but will still halt between steps per the step-file architecture rules. Simply confirm to proceed.
*   **Context Window Limits**: Mistral (7b) has a limited context window. Avoid loading `@BMAD-Core` in favor of targeted contexts (e.g., `@BMAD-Workflows-Analysis`). Claude Code has a much larger context window but should still load files just-in-time.
*   **Validation is Key**: BMAD relies on the "Validate" phase. Never skip it — it's designed to catch hallucinations and missing requirements before you write a single line of code.
*   **Language Consistency**: The framework is configured for **Français** by default in `config.yaml`. If you want to switch to English, update the `communication_language` in `_bmad/bmm/config.yaml`.

---

## Maintenance and Extension

### Adding New Agents
1.  Add the agent details to `_bmad/_config/agent-manifest.csv`.
2.  Create a markdown shard in `.claude/agents/`, `.continue/agents/`, and `.junie/agents/` for quick loading.
3.  (Optional) Add a custom slash command in `.continue/config.yaml`.

### Customizing Workflows
All workflows are stored in `_bmad/bmm/workflows/`. You can edit the markdown step files directly to adjust the instructions to your team's specific standards (e.g., specific linting rules or testing frameworks).

### Output Management
All generated artifacts go to `_bmad-output/`. This folder is excluded from most scans to keep your source tree clean while providing a clear audit trail of your development process.
