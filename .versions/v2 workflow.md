# Best Practices for Python Task Scripting with TOFA-WDF and Task Master

This document presents a refined modular methodology for managing scripting projects using the **Task-Oriented Functional Architecture with Decoupled Flows (TOFA-WDF)**, complemented by the **Task Master** planning framework. It integrates a structured architecture of tasks, flows, and modules with a memory-based iterative pipeline, tracked in a dedicated `pipeline/` folder.

## 1. Project Structure: Vertical Cohesion and Layered Separation

TOFA-WDF organizes all development around **capability-specific tasks**, with each task encapsulated as an autonomous directory. Logic is stratified across three distinct roles: `scripts` for execution, `flows` for orchestration, and `modules` for atomic operations. Each task operates as an independent unit with its own logic, test samples, and documentation.

```plaintext
project/
├── tasks/
│   ├── data_processing/
│   │   ├── scripts/
│   │   │   └── process_csv.py
│   │   ├── functions/
│   │   │   ├── simple/
│   │   │   └── orchestrators/
│   │   └── test_data/
│   ├── automation/
│   ├── reporting/
│   └── ...
│
├── flows/
│   ├── data_flow.py
│   ├── report_flow.py
│   └── integration_flow.py
│
├── shared_modules/
│   ├── io/
│   ├── transformation/
│   ├── strings/
│   └── validation/
│
├── pipeline/
│   ├── prd.md
│   ├── task_contract.md
│   ├── task-prd-revision.md
│   ├── microtasks.md
│   ├── microtasks_log.md
│   ├── microtasks_done/
│   ├── memories.md
│   └── learning_by_doing.md
│
├── docs/
│   ├── selenium.md
│   ├── seaborn.md
│   └── library_specs/
│
├── logs/
└── config/

	•	The tasks/ folder contains all task logic organized by operational goal.
	•	The pipeline/ folder is the reflexive memory system for planning, tracking, and documenting the lifecycle of development.
	•	The docs/ folder is reserved for external documentation, library manuals, and technical API references.

2. Roles of Files in the Pipeline
	•	prd.md: high-level description of the task scope, objectives, hypotheses, and key steps (to be clarified per task).
	•	task_contract.md: defines success criteria, input/output expectations, constraints, and test conditions.
	•	task-prd-revision.md: logs changes and revisions to the PRD during implementation.
	•	microtasks.md: contains the active subtask. Includes context, objective, plan, expected result, discovered constraints, implementation detail, and state.
	•	microtasks_log.md: flat registry of completed microtasks (by ID and name), cross-referencing their .md files in microtasks_done/.
	•	microtasks_done/: archive of completed microtasks in individual markdown files. The filename corresponds to the identifier used in the log.
	•	memories.md: strategic and conceptual log of failures, discarded strategies, and validated decisions.
	•	learning_by_doing.md: reflects on process improvements, workflow flaws, and long-term insights.

3. Conventions and Guarantees
	•	All folder and file names must be in English and lowercase.
	•	No script or flow may exist without an associated test and log.
	•	Every function is accompanied by a unit test written against a random sample of real data. Synthetic or handcrafted samples are not permitted.
	•	Every modification or failed strategy must be documented in memories.md.
	•	Every active task must be reflected in microtasks.md and archived upon completion.

4. Directory Semantics
	•	scripts/ → receives CLI input, executes orchestrators
	•	orchestrators/ → sequence and manage simple functions
	•	simple/ → pure atomic functional units
	•	flows/ → cross-task orchestration logic
	•	shared_modules/ → reusable utilities not bound to a single task
	•	pipeline/ → reflexive control layer (not implementation)
	•	docs/ → static documentation of libraries and dependencies

5. Summary

This architecture:
	•	Separates roles with mathematical precision
	•	Provides a formal memory and validation structure via the pipeline/ directory
	•	Enables exact traceability of failures and successful design paths
	•	Synchronizes tightly with Task Master while extending it with reflexive microtracking

TOFA-WDF guarantees that technical development remains auditable, modular, and reversible. No part of the workflow exists without explanation. No decision exists without record. No script is ever developed without a plan, a purpose, and a trace.

