Step-File Architecture Enforcement:
When a BMAD workflow file (e.g., from _bmad/bmm/workflows/) is provided in context, you MUST:
1. Read the entire file completely before taking any action.
2. Execute ONLY the current step defined in the file.
3. Halt for user input/selection before proceeding to any subsequent file or step.
4. Do NOT optimize the sequence or skip steps.
5. Identify your persona: For single or multi-persona methods, clearly identify viewpoints, and use party members if available in memory already.
6. YOU MUST ALWAYS SPEAK OUTPUT In your Agent communication style with the configured `communication_language` (Français).
7. Output patterns: Use provided patterns as flexible guides (e.g., "analysis -> insights -> action").
8. Stay relevant: Tie elicitation to specific content being analyzed.
9. Iterative enhancement: Each method application should apply to the current version of the content and show improvements.
10. Final acceptance: Confirm or ask the user what should be accepted from the session.