# Pipeline Memories

This file contains rejected approaches, architecture changes, and important decisions.

### [2025-07-23] Boss Feedback: Practical Gaps

Added minimalistic responses to six reported gaps:
- Performance: clarified in `task_contract.md`
- Security: input assumptions clarified
- Documentation: policy added in `docs/`
- Review Process: markdown + git combo formalized

No structural changes to workflow or logic.

### [2025-07-23] Structural Design Hardening

Documented protocol to prevent:
- circular dependencies across layers
- test data mismanagement
- cross-task ambiguity
- inconsistency in naming

No need to refactor existing code. Future work adheres to these modular protocols.
### [2025-07-23] Task Master CLI clarified

Integrated CLI-to-TOFA-WDF interaction mapping in `docs/task_master_integration.md`, distinguishing between execution, planning, and coordination.