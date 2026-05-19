# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **BMAD (Business Modular Agentic Development) framework** project (v6.0.0-Beta.4), project name **"gladium"**. BMAD is an AI-driven methodology that orchestrates a full project lifecycle through specialized agent personas and structured step-file workflows. It is not a traditional codebase with build/test commands — it is a framework of markdown-based agents, workflows, and templates.

## Language

The project is configured for **French** (`communication_language: Français` in `_bmad/bmm/config.yaml`). All interactions and generated artifacts should be in French unless the user requests otherwise.

## Architecture

### Directory Structure

- **`_bmad/`** — Framework core (reference source of truth for all agents, workflows, configs, resources)
  - **`_config/`** — Manifests (agents, workflows, tasks, tools, files) and global config
  - **`core/`** — Core module: bmad-master agent, brainstorming/party-mode workflows, Excalidraw resources, help tasks
  - **`bmm/`** — Main business module: phase-based workflows, agent definitions, team configs, data/templates
  - **`bmb/`** — External builder module (bmad-builder)
- **`.claude/`** — Claude Code integration (agent shards + rules adapted for Claude Code)
- **`.junie/`** — Junie IDE agent integration (agent shards + rules)
- **`.continue/`** — Continue IDE plugin integration (mirrors `.junie/` structure)
- **`_bmad-output/`** — Generated artifacts directory (planning and implementation artifacts)
- **`BMAD-GUIDE.md`** — User-facing integration guide for all IDE tools

### Workflow Phases (in `_bmad/bmm/workflows/`)

1. **`1-analysis/`** — Strategic analysis (Analyst persona "Mary")
2. **`2-plan-workflows/`** — PRD creation, UX design (PM "John", UX "Sally")
3. **`3-solutioning/`** — Technical architecture, epics & stories (Architect "Winston")
4. **`4-implementation/`** — Sprint planning and dev stories (SM "Bob", Dev "Amelia")
5. **`bmad-quick-flow/`** — Quick spec + dev for fast one-off tasks (Barry)

### Step-File Architecture

Workflows are composed of ordered step files (`step-01-*.md`, `step-02-*.md`, etc.). When executing a workflow:
1. Read the `workflow.md` file to understand the full sequence
2. Execute only the current step
3. Stop and ask for user validation before proceeding to the next step
4. Never skip or reorder steps
5. Adopt the agent persona's communication style and identity
6. Output in the configured `communication_language` (Français)

### Tri-Modal Pattern

Most workflows support three modes: **Create** (new artifact), **Validate** (check existing), and **Edit** (refine). Look for `steps-c/`, `steps-v/`, and `steps-e/` subdirectories.

## Agents

Agent shards in `.claude/agents/` are lightweight references. For full agent definitions with menus and handlers, read the corresponding file in `_bmad/bmm/agents/` or `_bmad/core/agents/`.

| Command | Agent | Name | Role |
|---------|-------|------|------|
| analyst | Mary | Business Analyst | Strategic analysis, research, product briefs |
| pm | John | Product Manager | PRD creation/validation/editing, epics |
| architect | Winston | Architect | Technical architecture, implementation readiness |
| ux-designer | Sally | UX Designer | UX design specifications |
| dev | Amelia | Developer | Story implementation, code review |
| sm | Bob | Scrum Master | Sprint planning, story creation |
| quick-flow-solo-dev | Barry | Quick Flow Dev | Fast spec + implementation |
| quinn | Quinn | QA Engineer | Test automation |
| tech-writer | Paige | Technical Writer | Documentation |
| bmad-master | BMad Master | Orchestrator | Default agent, workflow routing, party mode |

## Key Config Files

- `_bmad/bmm/config.yaml` — Project settings (name, language, output paths, user: Ascorak)
- `_bmad/core/config.yaml` — Core module config (mirrors language/output settings)
- `_bmad/_config/manifest.yaml` — Installed modules and versions
- `_bmad/_config/agent-manifest.csv` — Full registry of all agent personas
- `_bmad/_config/workflow-manifest.csv` — Registry of all 28 workflows
- `_bmad/_config/bmad-help.csv` — Help catalog for workflow navigation

## Working with This Repo

- There are no build, lint, or test commands — this is a markdown/YAML framework
- To add a new agent: add to `agent-manifest.csv`, create shards in `.claude/agents/`, `.continue/agents/`, and `.junie/agents/`
- Generated output goes to `_bmad-output/` (split into `planning-artifacts/` and `implementation-artifacts/`)
- When a workflow or agent is referenced, explore `_bmad/` to find the relevant files rather than guessing paths
- Always load `_bmad/bmm/config.yaml` first when adopting an agent persona (mandatory for all agents)
