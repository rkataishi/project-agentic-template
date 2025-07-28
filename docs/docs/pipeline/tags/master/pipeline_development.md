# TOFA-WDF + Task Master – Iterative Development Pipeline (v4.0)

This pipeline governs the complete lifecycle of a technical task using **TOFA-WDF**, integrated with **Task Master** for planning and enhanced with real-time memory management for continuity and traceability.

> 🔧 **Directory Structure Guidelines:**
> - `docs/` is the single source of truth for all project documentation, including workflow guides, rules, templates, and external knowledge.
> - For TaskMaster documentation, see `docs/external_knowledge/know_docs_task-master.md`.
> - For TaskMaster integration details, see `docs/external_knowledge/know_task_master_integration.md`.

---

## Architecture Overview

### The Four-Tier Architecture

Think of TOFA-WDF as a **factory assembly line**:

1.  **Modules** (`simple/`) → **Atomic workers** doing one specific job (inside a capability's `functions/` directory).
2.  **Orchestrators** (`orchestrators/`) → **Team leaders** coordinating workers (inside a capability's `functions/` directory).
3.  **Flows** (`flows/`) → **Factory managers** coordinating multiple teams (at the project root).
4.  **Scripts** (`scripts/`) → **Control room** receiving external commands (inside a capability's directory).

### Project Structure

```plaintext
project/
├── data_processing/            # Capability-specific folder
│   ├── scripts/
│   ├── functions/
│   │   ├── simple/
│   │   └── orchestrators/
│   └── test_data/
├── reporting/                  # Another capability folder
│   └── ...
│
├── tasks/                      # For Task Master's generated .md files ONLY
│
├── docs/                       # ALL project documentation
│   ├── external_knowledge/
│   │   ├── know_docs_task-master.md
│   │   └── know_task_master_integration.md
│   ├── pipeline/
│   │   ├── active -> tags/master/        # Symlink to the active context
│   │   ├── pipeline_development.md       # This guide
│   │   ├── pipeline_pickup.md            # How to resume work
│   │   └── tags/
│   │       └── master/
│   │           ├── prd.md
│   │           └── ... (other active context files)
│   ├── rules/
│   │   ├── rule_code_review_manual.md
│   │   ├── rule_cross_task_coordination.md
│   │   ├── rule_doc_guidelines.md
│   │   └── ... (all other project rules)
│   └── templates/
│       ├── config/
│       │   └── template_config.py      # <-- MUST be copied to /config/config.py
│       ├── template_learning_by_doing.md
│       ├── template_memories.md
│       └── template_task_contract.md
│
├── flows/                      # Cross-capability orchestration
├── shared_modules/             # Reusable utilities
└── config/                     # Project-specific configuration (populated from template)
    └── config.py               # <-- This file is created from the template
```

---

### **Phase 1: AI-Led Scoping and Backlog Creation**

The project begins with an AI-powered scoping phase to generate a comprehensive task backlog.

1.  **Author the PRD:** Create or update the `prd.md` file within the active pipeline context (e.g., `docs/pipeline/active/prd.md`). This document outlines the high-level goals and requirements.
2.  **Generate the Task Backlog:** Run the native Taskmaster command to parse the PRD.
    *   **Command:** `task-master parse-prd docs/pipeline/active/prd.md`
    *   **Result:** Taskmaster creates the initial `tasks.json` file, populating it with a full list of tasks derived from the PRD. This is the project's **master backlog**.

---

### **Phase 2: Human-Approved Strategic Planning**

Before any code is written, a human developer must create a focused, strategic plan for the immediate work session.

1.  **Select the Next Task:** Review the master backlog using `task-master list` and identify the next task to be implemented. Use `task-master next` for a recommendation.
2.  **Define the Microtask Plan:** Open the `microtasks.md` file in the active context (e.g., `docs/pipeline/active/microtasks.md`). In this file, write a detailed, human-authored plan for implementing the single task selected in the previous step.
    *   **This document is the **single source of truth** for the AI agent's immediate coding session.** It provides the "what" and the "why."

---

### **Phase 3: AI-Assisted Implementation and Tactical Logging**

The AI agent executes the plan from `microtasks.md` and logs its progress in a separate, tactical log.

1.  **Implementation:** The agent writes code based on the plan in `microtasks.md`.
2.  **Tactical Logging:** As the agent works, it **must** log its findings, successes, and failures using the `update-subtask` command. This creates a timestamped, granular implementation history within `tasks.json`.
    *   **Example Command:** `task-master update-subtask --id=5.2 --prompt="[LOG] Successfully connected to the database. The connection string required ssl=true. This was not in the initial plan."`
    *   This log provides the "how."
3.  **Synthesize Knowledge:** Upon task completion, the strategic insights from the tactical log are synthesized and recorded in `docs/pipeline/active/memories.md`.

---

### **Phase 4: Iterative Implementation Loop**

#### **A. Module Development**
- Develop **Modules** (pure, atomic functions) in `<capability_name>/functions/simple/` (e.g., `data_processing/functions/simple/`).
- Each logical step is a **Microtask**.
- Immediately write and validate a unit test for each Module.
- **Principle**: No function exists without a test. Governed by `docs/rules/rule_test_data_policy.md`.
- Functions must be stateless: all logic must depend only on explicitly passed arguments.
- Return values must contain all necessary outputs for the next processing step.

#### **B. Composition**
- Compose **Modules** into **Orchestrators** in `<capability_name>/functions/orchestrators/`.
- Compose **Orchestrators** into **Flows** in the root `flows/` directory.
- Keep orchestrators focused on coordination, not atomic logic.
- Orchestrators must manage the data flow explicitly between modules via argument passing.
- Avoid using intermediate storage or global variables to transfer state between steps. See `docs/rules/rule_cross_task_coordination.md`.

#### **C. Script Construction and Testing**
- Write **Scripts** in `<capability_name>/scripts/` that run orchestrators or flows.
- Run on real, sampled data with logging.
- Use a structured logger for all outputs.
- Ensure that logs are saved to the root `logs/` directory and include task name and timestamp.
- Avoid inline `print()` for traceability—use logger methods like `.info()`, `.error()`, `.warning()` instead.
- Mark progress using the native Taskmaster command: `task-master set-status --id <id> --status in-progress`.
- **Every issue triggers**:
  - Documentation in `docs/pipeline/active/microtasks.md`.
  - A new task if significant: `task-master add-task --prompt "Investigate..."`.

#### **D. LLM-Assisted Revision**
- Use an LLM agent for refactors, alternatives, or diagnostics.
- **Certainty principle**: <80% certainty, ask; 80-95% certainty, offer options; >95% certainty, act.
- Update all relevant files if the scope changes.

#### **E. Re-Execution and Retest**
- Run again with updated code.
- Ensure all error paths are exercised and properly logged during execution.
- All raised exceptions must either be caught or allowed to propagate with structured logging.
- Silent failure is prohibited. Any unhandled exception must be visible and documented.
- Validate against the criteria in `docs/pipeline/active/task_contract.md`.
- Log failures and changes in `docs/pipeline/active/memories.md`, then retry.

---

### **Phase 5: Full Validation and Testing**
- Run scripts on full-sample or edge-case real data.
- Use unit tests for Modules, log outputs for Flows and Scripts.
- Confirm all validation points in `docs/pipeline/active/task_contract.md`.
- Confirm that all error-handling routines behave as expected under failure conditions.
- Ensure any runtime errors that impact task outcomes are logged in `docs/pipeline/active/memories.md`, along with attempted resolutions.
- Verify that all scripts log runtime behavior to the `logs/` directory with correct levels (INFO, ERROR, etc.).
- Ensure that any exceptions raised are logged with full traceback.
- Confirm logging of start/end markers and key transitions in control flow.
- Mark the task as testing: `task-master set-status --id <id> --status testing`.

---

### **Phase 6: Closure and Documentation Sync**
- Mark the task as done: `task-master set-status --id <id> --status done`.

- **Archive current microtask**:
  - Move the content of `docs/pipeline/active/microtasks.md` to an archive file inside `docs/pipeline/active/microtasks_done/`.
  - Update `docs/pipeline/active/microtasks_log.md` with a reference to the archived file.

- **Update documentation**:
  - `docs/pipeline/active/memories.md` → Log failures, discarded paths, and reasons.
  - `docs/pipeline/active/learning_by_doing.md` → Note process improvements.
  - `docs/pipeline/active/task_contract.md` → Confirm all conditions were met.

- Ensure the final state aligns with `docs/pipeline/pipeline_pickup.md`.

---

### **Core Principles (Mandatory)**
- Never develop without unit tests.
- Never execute changes without reviewing context via `docs/pipeline/pipeline_pickup.md`.
- Never modify logic without documenting changes and failures.
- Never assume a plan is valid until implementation validates it.
- Never mark a task done without:
  - Closing the microtask.
  - Logging learnings.
  - Documenting strategic knowledge in `docs/pipeline/active/memories.md`.

---

### **Quick Start Guide**

```bash
# 1. Setup the project for the first time
./setup_pipeline.sh

# 2. Check what you're working on
cat docs/pipeline/active/microtasks.md

# 3. See the project structure for a capability
tree data_processing/

# 4. List all tasks
task-master list

# 5. Get next recommended task
task-master next
```

---

### **Key Files Reference**

- **`docs/pipeline/pipeline_development.md`** → This complete workflow guide.
- **`docs/pipeline/pipeline_pickup.md`** → How to resume work after interruptions.
- **`docs/pipeline/active/microtasks.md`** → Your current active work.
- **`docs/pipeline/active/memories.md`** → Strategic knowledge and learnings.
- **`docs/pipeline/active/task_contract.md`** → Success criteria and validation points.
- **`docs/rules/`** → The single source of truth for all coding and process standards.

---

### **Setup Guide: Recreating the Pipeline Structure in a New Project**

When starting a new project, use these instructions to recreate the complete pipeline structure including all symlinks and directory organization.

#### **Automated Setup Script**
Create this script as `setup_pipeline.sh` in your project root:

```bash
#!/bin/bash
# TOFA-WDF Pipeline Setup Script v2.0

echo "Setting up TOFA-WDF pipeline structure..."

# Create root directory structure
mkdir -p config logs tasks shared_modules flows

# Create the full docs structure
mkdir -p docs/{external_knowledge,pipeline/tags/master/microtasks_done,rules,templates/config}
mkdir -p docs/pipeline/tags/.archive

# Create essential template and rule files
touch docs/rules/rule_{code_review_manual,cross_task_coordination,doc_guidelines,knowledge_sync,self_improve,test_data_policy,vscode_rules}.md
touch docs/templates/config/template_config.py
touch docs/templates/template_{learning_by_doing,memories,task_contract}.md

# Create essential tracking files within the master context
touch docs/pipeline/tags/master/{prd.md,microtasks.md,microtasks_log.md,memories.md,task_contract.md,learning_by_doing.md}

# Create the active symlink for the pipeline context
cd docs/pipeline/
ln -sfn tags/master/ active
cd ../../

echo "✅ Pipeline structure created successfully!"
echo "-> Remember to copy 'docs/templates/config/template_config.py' to 'config/config.py' and fill it out."
```

#### **Usage Instructions**
```bash
# Make the script executable
chmod +x setup_pipeline.sh

# Run the setup for a new project
./setup_pipeline.sh
```

---

### **Advanced Workflow: The "Two-Step Sync" Protocol for Context Management**

To manage different features or experiments in isolation, Taskmaster uses "tags." To keep our TOFA-WDF documentation perfectly synchronized, we use a simple **Two-Step Sync** protocol.

#### **How to Create a New Feature Context (e.g., "feature-dashboard")**

This creates a new, isolated workspace for both tasks and documentation.

*   **Step 1 (Taskmaster):** Create the new tag in Taskmaster, copying from master.
    *   **Command:** `task-master add-tag feature-dashboard --copy-from master`
*   **Step 2 (TOFA-WDF):** Create the corresponding documentation context.
    *   **Command:** `cp -r docs/pipeline/tags/master/ docs/pipeline/tags/feature-dashboard/`

#### **How to Switch Between Contexts**

This activates a different workspace.

*   **Step 1 (Taskmaster):** Switch to the desired tag in Taskmaster.
    *   **Command:** `task-master use-tag feature-dashboard`
*   **Step 2 (TOFA-WDF):** Update the `active` symlink to point to the new context.
    *   **Commands (run from the `docs/pipeline/` directory):**
        1.  `rm active`
        2.  `ln -s tags/feature-dashboard/ active`

*All tools and file paths will now automatically use the `feature-dashboard` context.*

#### **How to Delete a Feature Context**

This safely archives the workspace.

*   **Step 1 (Taskmaster):** Delete the tag from Taskmaster.
    *   **Command:** `task-master delete-tag feature-dashboard`
*   **Step 2 (TOFA-WDF):** Archive the documentation context (we never delete it completely).
    *   **Commands:**
        1.  `mv docs/pipeline/tags/feature-dashboard/ docs/pipeline/tags/.archive/feature-dashboard_$(date +%F)`