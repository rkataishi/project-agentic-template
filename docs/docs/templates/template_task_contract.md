# Task Contract

This document defines the contract for data processing tasks in this project.

## Performance Guidelines (Optional, for Data Tasks)

- Expected runtime: under 60 seconds for 1K rows
- Memory usage: not a concern unless explicitly logged
- Batch vs streaming behavior: pure batch unless documented

---

## Input Validation / Security

- All inputs are assumed to be pre-validated or internal
- No user-facing API; no injection risk assumed
- Input structure assumptions must be noted in `microtasks.md` or inline comments