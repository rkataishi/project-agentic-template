# Best Practices for Python Task Scripting with TOFA-WDF (v3.0)

This document outlines a modular and disciplined methodology for managing scripting projects using the **Task-Oriented Functional Architecture with Decoupled Flows (TOFA-WDF)**, supported by **Task Master** for planning and tracking. This approach defines clear architectural roles, separates concerns across layers, and introduces a memory-based task tracking pipeline (`pipeline/`) for iteration control, error traceability, and workflow continuity.

### 1. Organizing the Project Around Tasks and Capabilities
TOFA-WDF organizes scripting efforts around self-contained operational units. Each unit, or **task**, encapsulates a specific capability—such as automation, reporting, or data ingestion—and is implemented within its own directory under `tasks/`. This structure prevents cross-contamination of logic. Shared, cross-cutting functionality is placed in `shared_modules/` and kept stateless and pure to allow safe reuse.

### 2. Layered Architecture: Scripts, Flows, and Modules
TOFA-WDF enforces a strict three-tier design:
- **Scripts** serve as entrypoints. They handle argument parsing and configuration loading, and dispatch to flows. They do not contain logic.
- **Flows** implement the orchestration logic. They sequence operations, catch exceptions, and manage logic branching. They contain no I/O or CLI concerns.
- **Modules** implement atomic operations—transforming a string, parsing a file, validating an email. They must be independently testable and deterministic.

Each script executes a flow. Each flow uses functions. Each function is isolated and accompanied by a unit test. Logic always flows downward—no upward coupling is permitted.

### 3. Directory Structure and Semantic Separation
```plaintext
project/
├── tasks/                      # Code: Self-contained operational units
│   ├── data_processing/
│   │   ├── scripts/            # Entrypoints (CLI)
│   │   ├── functions/
│   │   │   ├── simple/         # Modules/Functions (Tasks)
│   │   │   └── orchestrators/  # Orchestrators
│   │   └── test_data/
│   └── ...
│
├── flows/                      # Code: High-level business flows
│
├── shared_modules/             # Code: Cross-cutting, stateless functionality
│
├── pipeline/                   # The Reflexive Core: Planning, execution, and memory of the ACTIVE task
│   ├── prd.md                  # The "What" and "Why" of the current task
│   ├── criterios_cierre.md     # The definition of "done" for the current task (was task_contract.md)
│   ├── task-prd-revision.md
│   ├── microtasks.md           # The live working file: "What I am doing right now"
│   ├── microtasks_stack/       # The archive of completed microtasks (was microtasks_done/)
│   ├── memories.md             # The log of decisions, errors, and discarded paths
│   └── learning_by_doing.md    # The log of procedural lessons learned
│
├── docs/                       # Static Knowledge Base: External library docs, guides, etc.
│   ├── selenium_guide.md
│   └── library_specs/
│
└── ...
```
The `pipeline/` folder contains the reflexive layer of the system. All live tracking of work-in-progress, strategic decisions, learning, and iteration happens here. The `docs/` folder is strictly for external documentation and library-specific references.

### 4. Microtask Tracking System
- **`microtasks.md`**: Describes the current subtask, with general objective, immediate goal, known context, proposed plan, expected result, and constraints.
- **`microtasks_stack/`**: An archive of all completed microtask markdown files. Filenames should follow a convention (e.g., `023_clean_nulls.md`) that ensures traceability.
- **`memories.md`**: Logs critical decisions, rejected approaches, and discarded hypotheses. Essential for not repeating mistakes.
- **`learning_by_doing.md`**: Captures lessons, workflow adjustments, and planning errors.

*Naming conventions, identifiers, and classification strategies must be defined in the task’s `pipeline/prd.md`.*

### 5. Task Contracts and Testing
The file `pipeline/criterios_cierre.md` replaces ambiguous completion criteria. It defines what constitutes “done”: required outputs, performance bounds, conditions to test, and environmental assumptions. Testing is not optional:
- Each function must have an accompanying unit test using realistic subsampled data (no synthetic inputs).
- Each flow is validated by terminal output and system behavior.
- No script is valid without being exercised under dry-run and verbose conditions.
- Completion requires fulfillment of the contract.

### 6. Task Master Integration
Task Master serves as the timeline and controller for task-level progress. Typical commands:
- `task prd "..."`: Initializes the PRD in `pipeline/prd.md`.
- `task parse_prd`: Generates initial subtasks.
- `task add_task`: Manually defines additional steps.
- `task set_task_status`: Tracks progress (pending, in-progress, testing, done).

Every execution state must be reflected in `pipeline/microtasks.md`. If a plan fails, it must be redefined, logged in `pipeline/memories.md`, and the pipeline reoriented accordingly. No code modification is allowed without 95% certainty. If below, alternatives must be presented, and user confirmation is required.

### 7. Philosophical Modularity and Reflexivity
Modularity in TOFA-WDF is absolute. No function crosses its layer. Scripts do not host logic. Flows do not perform operations. Modules do not access context.

Reflexivity is equally strict: no task is done without audit. If a microtask is completed, it is archived. If a solution fails, it is logged and replaced. If a method works, it is remembered. This guarantees reversibility, reproducibility, and coherence across time. Nothing is undocumented. Nothing is assumed. Every decision has a trace.

⸻

If scripting is to be treated as a system, it must also produce its own memory. TOFA-WDF and Task Master combine structural discipline with reflexive tracking, yielding a workflow that is not only executable, but legible, testable, and improvable. All architectural rules are defined in this document. All strategic decisions are logged in `pipeline/memories.md`. All progress is tracked in `pipeline/microtasks.md`. Nothing advances without being written, reviewed, tested, and remembered.