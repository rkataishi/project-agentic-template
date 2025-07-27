# Knowledge Synchronization and Validation Policy

This document mandates how project-specific rules are updated and used, ensuring all development aligns with the latest best practices. The `docs/rules/` directory is the single source of truth.

## The Rule Update Workflow

1.  **Documentation-First:** Any change to a coding standard **must** first be documented by editing the relevant file in `docs/rules/`. The commit message for this change should clearly state the new rule.
2.  **Mandatory AI Validation:** Before applying any new or changed rule, the AI agent **must** first validate its understanding of the change. This is done by running a `research` query targeting the specific rule file.
    *   **Purpose:** This step forces the AI to re-read the rule and confirms its context is up-to-date, preventing it from using outdated, cached knowledge.
    *   **Example Command:** `task-master research --query="Explain the new required format for function docstrings." --files="docs/rules/doc_guidelines.md"`
3.  **Informed Application:** Only after the AI receives a correct summary from its research query can it proceed to apply the new pattern to the codebase.