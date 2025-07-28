# Learning by Doing

This file captures workflow and process lessons learned through implementation.

### [2025-07-23] Formalizing Implicit Practices

Documented minimal responses to perceived gaps raised by external reviewer:
- Adopted markdown protocols to preempt future critiques
- Standardized our inline and process documentation strategy

Outcome: full compliance with no added weight.

### [2025-07-23] Structural Guidance Formalized

Captured and resolved key missing structural guarantees:
- Defined data test layout and naming expectations
- Codified file/function naming
- Locked architecture boundaries for flows and orchestrators

This makes TOFA-WDF auditable by external reviewers without increasing workload.
### [2025-07-23] CLI/TOFA boundary made explicit

Clarified that `task` only scaffolds and tracks state. Human writes the plan and logic in `prd.md` and `microtasks.md`.