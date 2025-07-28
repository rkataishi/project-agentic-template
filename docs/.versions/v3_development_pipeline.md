# 🔁 TOFA-WDF + Task Master – Iterative Development Pipeline (v3.0)

This pipeline governs the complete lifecycle of a technical task using the **Task-Oriented Functional Architecture with Decoupled Flows (TOFA-WDF)**, integrated with **Task Master** for planning, and enhanced with **real-time task memory management**. It is designed to ensure continuity, traceability, and reproducibility across sessions.

──────────────────────────────────────────────
### 1. TASK DEFINITION AND MICROTASK INITIALIZATION
──────────────────────────────────────────────
• **Create Task Entry in Task Master**:
  `task prd "Describe goal of the task in one line"`
  *This command bootstraps the active task, creating `pipeline/prd.md` and other necessary tracking files.*

• **Initialize `pipeline/microtasks.md` as the live working file**:
  - **General objective of the task**: What is the overall function trying to accomplish?
  - **Current sub-objective**: What is this specific microtask trying to accomplish?
  - **Context of the implementation**: Previous & next steps.
  - **Proposed plan and methods**: How to execute the sub-objective.
  - **Expected results**: Concrete outputs, behaviors, or changes.
  - **Known constraints (to be refined iteratively)**.
  - **Updated constraints (as they emerge)**.

• **If replacing a previous microtask, archive it in**:
  `pipeline/microtasks_stack/`

• **Ensure all tracking files are present in `pipeline/`**:
  - `pipeline/prd.md`
  - `pipeline/task-prd-revision.md`
  - `pipeline/criterios_cierre.md`
  - `pipeline/memories.md`
  - `pipeline/learning_by_doing.md`

↓

──────────────────────────────────────────────
### 2. TASK PARSING AND STRUCTURAL HYPOTHESIS
──────────────────────────────────────────────
• **Parse the PRD to get a first hypothesis of subtasks**:
  `task parse_prd`

• **Manually rearrange, reword, split or combine subtasks** within your plan in `pipeline/microtasks.md`.

• **Define expected completion conditions in `pipeline/criterios_cierre.md`**:
  *(e.g., specific outputs, logs, runtime behavior, correctness of transformations)*

• **Set task priorities**:
  `task set_priority --task "X" --level high`

• **Define dependencies explicitly**:
  `task add_dependency --task "Y" --depends-on "X"`

↓

──────────────────────────────────────────────
### 3. ITERATIVE IMPLEMENTATION LOOP
──────────────────────────────────────────────

╭──→ **[A] FUNCTION DEVELOPMENT (The "Task")**
│ • A **Task** corresponds to a single-responsibility function.
│ • Each logical step to build or modify it is a **Microtask**.
│ • Immediately write and validate a unit test for each function.
│ • **Complexity Heuristic**: A function should not exceed 400 lines.
│ • **Principle**: Never write a script without a test.
│
╰──→ **[B] FLOW COMPOSITION (The "Orchestrator")**
  • Compose simple functions (Tasks) into an **Orchestrator**.
  • Keep orchestrators free of atomic logic, focused on coordination.
  • **Flows** (in the root `flows/` directory) are a higher level of abstraction, coordinating multiple orchestrators to achieve a full business goal.

↓

╭──→ **[C] SCRIPT CONSTRUCTION AND TESTING**
│ • Write a script that takes real input and runs the orchestrator.
│ • Run it on real, randomly sampled data with logging.
│ • Check for errors, logs, and outputs.
│ • Mark progress in Task Master:
│   `task set_task_status --task "X" --status in-progress`
│ • **Regardless of severity, every implementation issue should trigger**:
│   - Documentation of the issue in `pipeline/microtasks.md`.
│   - A new task in Task Master if it's a significant diversion:
│     `task add_task "Investigate null cleaning error"`
│
╰──→ **[D] LLM-ASSISTED REVISION**
  • Use the LLM agent to propose refactors, explore alternatives, or diagnose errors, governed by `pipeline/llm_instructions.md`.
  • **Never act if certainty < 95%**.
  • If certainty is 80–95%, offer options and ask for user confirmation.
  • If certainty < 80%, never proceed — ask first.
  • If task scope or logic changes, update all relevant files:
    - `pipeline/prd.md` and `pipeline/task-prd-revision.md`
    - `pipeline/microtasks.md`
    - Log misassumptions in `pipeline/memories.md`
    - Log procedural learning in `pipeline/learning_by_doing.md`

↓

╭──→ **[E] RE-EXECUTION AND RETEST**
│ • Run again with updated functions and flows.
│ • Validate against `pipeline/criterios_cierre.md`.
│ • If it fails, log what failed, what was changed, and retry.
│
╰──→ **Always ensure everything is reflected in `pipeline/microtasks.md`**.

↓

──────────────────────────────────────────────
### 4. FULL VALIDATION AND TESTING
──────────────────────────────────────────────
• Run script(s) on full-sample or edge-case real data.
• Use:
  - **Unit tests** to validate functions.
  - **Terminal and log outputs** to validate flows and scripts.
• Confirm all validation points in `pipeline/criterios_cierre.md`.
• Mark task as `testing` in Task Master:
  `task set_task_status --task "X" --status testing`

↓

──────────────────────────────────────────────
### 5. CLOSURE AND DOCUMENTATION SYNC
──────────────────────────────────────────────
• **Mark task as complete in Task Master**:
  `task set_task_status --task "X" --status done`

• **Archive current microtask** by moving it from `pipeline/microtasks.md` to `pipeline/microtasks_stack/`.

• **Update all relevant documentation for future reference**:
  - `pipeline/memories.md` → Log key failures, discarded paths, and the reasons why.
  - `pipeline/learning_by_doing.md` → Note procedural or structural improvements.
  - `pipeline/task-prd-revision.md` → Update structural understanding of the task.
  - `pipeline/criterios_cierre.md` → Confirm all conditions were met.
  - `README.md` → Only if it’s relevant to the overall project summary.

• **Ensure the final state is ready for a future developer** (or your future self) by aligning with `pipeline/pickup_roadmap.md`.

↓

──────────────────────────────────────────────
### CORE PRINCIPLES (MANDATORY)
──────────────────────────────────────────────
• Never develop a script without a unit test.
• Never execute any change without first reviewing the context as guided by `pipeline/pickup_roadmap.md`.
• Never modify logic without writing what was changed, why, and what failed before.
• Never assume a plan is valid until the implementation validates it.
• Never drop a failure without understanding why it failed.
• Never abandon a failed path without retrying or exploring alternatives.
• Never mark a task as done without:
  - Closing the microtask.
  - Logging what worked and what didn’t.
  - Writing what was learned.
  - Documenting new strategic knowledge in `pipeline/memories.md`.