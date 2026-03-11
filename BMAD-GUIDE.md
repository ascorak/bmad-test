# 🧙 BMAD Integration Guide (Continue & Junie)

Welcome to the **Business Modular Agentic Development (BMAD)** framework, version 6.0.0-Beta.4, now fully integrated into your **Continue** IDE plugin and **Junie** autonomous agent.

This guide explains how to orchestrate a complete project lifecycle—from initial discovery to production-ready implementation—using specialized AI agents and structured workflows.

---

## 🤖 Using BMAD with Junie (New!)

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

## 🚀 Executing the Full BMAD Lifecycle (Continue)

The BMAD method follows a disciplined, phase-based approach. Each phase is handled by a specific agent with its own persona and principles.

### Phase 1: Strategic Analysis (Mary)
*   **Command**: `/analyst`
*   **Workflow**: Use `@BMAD-Workflows-Analysis` to find `_bmad/bmm/workflows/1-analysis/`
*   **Goal**: Define the problem space, perform market research, and create a **Product Brief**.
*   **How to start**: 
    > `/analyst Start a new project discovery. Use @Project-Context as a template and @BMAD-Workflows-Analysis for discovery workflows.`

### Phase 2: Product Strategy & Planning (John)
*   **Command**: `/pm` or `/prd`
*   **Workflow**: Use `@BMAD-Workflows-Planning` to find `_bmad/bmm/workflows/2-plan-workflows/create-prd/`
*   **Goal**: Translate the Brief into a comprehensive **Product Requirements Document (PRD)**.
*   **How to start**:
    > `/pm Create a PRD based on the project brief in _bmad-output/planning-artifacts/. Use @BMAD-Workflows-Planning to find the create-prd workflow.`

### Phase 3: Technical Architecture (Winston)
*   **Command**: `/architect` or `/arch`
*   **Workflow**: Use `@BMAD-Workflows-Solutioning` to find `_bmad/bmm/workflows/3-solutioning/create-architecture/`
*   **Goal**: Define the technical stack, data flows, and system components.
*   **How to start**:
    > `/architect Design the architecture for the PRD at [path/to/PRD.md]. Load the create-architecture workflow from @BMAD-Workflows-Solutioning.`

### Phase 4: Implementation (Amelia & Bob)
*   **Commands**: `/sprint` (for Bob/Scrum Master) then `/dev` (for Amelia/Dev)
*   **Workflow**: Use `@BMAD-Workflows-Implementation` to find `_bmad/bmm/workflows/4-implementation/`
*   **Goal**: Break the PRD into stories and implement them with 100% test coverage.
*   **How to start**:
    > `/sprint Plan the first sprint based on the PRD and Architecture. Use @BMAD-Workflows-Implementation for the sprint-planning workflow.`
    > `/dev Implement story [ID] from the sprint plan. Use @BMAD-Workflows-Implementation for the dev-story workflow.`

---

## 💡 Tips and Tricks

*   **Granular Context (@)**: Évitez d'utiliser `@BMAD-Core` qui charge tout le framework (plus de 400 fichiers), ce qui dépasse les limites de contexte du modèle Mistral. Utilisez plutôt des fournisseurs granulaires par phase comme `@BMAD-Workflows-Analysis`, `@BMAD-Workflows-Planning`, etc.
*   **Just-In-Time (JIT) Loading**: Always provide the specific step file (e.g., `@step-01-init.md`) as context. The agents are instructed to wait for your input after each step.
*   **The Tri-Modal Pattern**: Most BMAD workflows support **Create**, **Validate**, and **Edit** modes. Use `/prd -v` to validate an existing PRD or `/arch -e` to refine your design.
*   **Party Mode**: For complex architectural or product decisions, use `/brainstorm` or manually mention multiple agents to trigger a multi-perspective discussion.
*   **Excalidraw Integration**: Need a diagram? Use Sally (UX) or Winston (Architect) and ask for an Excalidraw output to visualize your data flows.

---

## ⚠️ Caveats

*   **Manual Step Advancement**: Continue does not automatically load the "next" file in a sequence. You must manually add the next step file to the context (using `@file`) when prompted by the agent.
*   **Context Window Limits**: Mistral (7b) a une fenêtre de contexte limitée. Évitez de charger `@BMAD-Core` au profit de contextes ciblés (ex: `@BMAD-Workflows-Analysis`).
*   **Validation is Key**: BMAD relies on the "Validate" phase. Never skip it—it's designed to catch hallucinations and missing requirements before you write a single line of code.
*   **Language Consistency**: The framework is configured for **Français** by default in `config.yaml`. If you want to switch to English, update the `communication_language` in `_bmad/bmm/config.yaml`.

---

## 🛠️ Maintenance and Extension

### Adding New Agents
1.  Add the agent details to `_bmad/_config/agent-manifest.csv`.
2.  Create a markdown shard in `.continue/agents/` and `.junie/agents/` for quick loading.
3.  (Optional) Add a custom slash command in `.continue/config.yaml`.

### Customizing Workflows
All workflows are stored in `_bmad/bmm/workflows/`. You can edit the markdown step files directly to adjust the instructions to your team's specific standards (e.g., specific linting rules or testing frameworks).

### Output Management
All generated artifacts go to `_bmad-output/`. This folder is excluded from most scans to keep your source tree clean while providing a clear audit trail of your development process.
