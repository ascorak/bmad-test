---
description: Enforces BMAD step-file architecture when executing workflows from _bmad/
globs: ["_bmad/**/workflow.md", "_bmad/**/step-*.md"]
alwaysApply: true
---

# Step-File Architecture Enforcement

When a BMAD workflow file (from `_bmad/bmm/workflows/` or `_bmad/core/workflows/`) is loaded, you MUST:

1. Read the entire workflow file completely before taking any action.
2. Execute ONLY the current step defined in the file.
3. Halt for user input/selection before proceeding to any subsequent file or step.
4. Do NOT optimize the sequence or skip steps.
5. Identify your persona: adopt the agent's communication style and identity.
6. YOU MUST ALWAYS SPEAK OUTPUT in the configured `communication_language` from `_bmad/bmm/config.yaml` (default: Français).
7. Output patterns: Use provided patterns as flexible guides (e.g., "analysis → insights → action").
8. Stay relevant: Tie elicitation to specific content being analyzed.
9. Iterative enhancement: Each method application should improve the current version of the content.
10. Final acceptance: Confirm or ask the user what should be accepted from the session.

## State Management
- Track progress via frontmatter `stepsCompleted` in output documents.
- Detect existing documents for continuation (step-01b patterns).
- Never pre-load future steps — use just-in-time loading.
