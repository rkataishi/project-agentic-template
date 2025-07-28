# Manual Code Review Protocol (TOFA-WDF + Git)

## Review Approach

This project uses two layers of review:
1. Markdown-level traceability in:
   - `pipeline/microtasks.md`
   - `pipeline/memories.md`
2. Git diff-based visual review before committing.

## Review Checklist

- [ ] Each microtask must define purpose, logic plan, and constraints
- [ ] Code must match `microtasks.md` description
- [ ] Every new function must be accompanied by:
  - [ ] Functional inline comment above it
  - [ ] Unit test with real data
- [ ] No logic outside `simple/`, `orchestrators/`, `flows/`
- [ ] No undocumented deviation from microtask plan

No approval = no merge.

---

## Circular Dependency Policy

- Flows (`flows/`) must not reference task-local orchestrators directly.
- Task orchestrators must not import from flows.
- All dependencies are one-directional:
  - `simple/` → `orchestrators/` → `flows/` → `scripts/`