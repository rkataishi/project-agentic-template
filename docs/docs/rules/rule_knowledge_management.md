# Rule: Knowledge Management & Architecture Decisions

To prevent knowledge loss and ensure that our documentation remains valuable, we follow a strict protocol for managing long-term learnings and architectural decisions.

## 1. The Knowledge Synthesis & Archiving Protocol

-   **Problem:** `memories.md` and `learning_by_doing.md` can become bloated and unreadable over time, hiding valuable insights.
-   **Trigger:** This protocol is executed at the end of a major epic, a significant feature release, or at minimum, on a quarterly basis.
-   **Process:**
    1.  **Synthesize:** A designated developer reads through the active `memories.md` and `learning_by_doing.md`.
    2.  **Extract & Formalize:** Key strategic decisions, discarded architectural paths, and permanent process improvements are extracted and formalized into **Architecture Decision Records (ADRs)**. See below for details.
    3.  **Archive:** The content of the active `memories.md` and `learning_by_doing.md` is moved to a dated file in the archive (e.g., `docs/pipeline/active/archive/memories_q3_2025.md`).
    4.  **Reset:** The active `memories.md` and `learning_by_doing.md` are reset using their respective templates from `docs/templates/`.

## 2. Architecture Decision Records (ADRs)

-   **Purpose:** An ADR is a short document that captures a single, significant architectural decision. It is the permanent, high-level memory of the project.
-   **When to Create an ADR:**
    -   A decision that impacts the overall structure (e.g., choosing a new database, adopting a new library for a core function).
    -   A decision that has long-term consequences and trade-offs.
    -   A decision that a new developer must understand to grasp the "why" behind the codebase.
-   **Location:** ADRs are stored in a new top-level directory: `docs/adr/`.
-   **Format:** Create new ADRs by copying `docs/templates/template_adr.md`.