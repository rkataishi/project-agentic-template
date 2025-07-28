# 🔁 TOFA-WDF + Task Master – Iterative Development Pipeline (Corrected & Memory-Integrated)

This pipeline governs the complete lifecycle of a technical task using the **Task-Oriented Functional Architecture with Decoupled Flows (TOFA-WDF)**, integrated with **Task Master** for planning, and enhanced with **real-time task memory management**. It is designed to ensure continuity, traceability, and reproducibility across sessions.

──────────────────────────────────────────────
1. TASK DEFINITION AND MICROTASK INITIALIZATION
──────────────────────────────────────────────
• Draft a clear technical and functional description in:  
  docs/<task>/prd.md  

• Initialize microtasks.md as a live working file:  
  - General objective of the task  
  - Current sub-objective  
  - Context of the implementation (previous & next steps)  
  - Proposed plan and methods  
  - Expected results  
  - Known constraints (to be refined iteratively)  
  - Updated constraints (as they emerge)  

• Create task entry in Task Master  
  (task prd "Describe goal of the task in one line")

• If replacing a previous microtask, archive it in:  
  microtasks_stack/

• Prepare support files for tracking (if not already created):  
  - docs/<task>/task-prd-revision.md  
  - docs/<task>/criterios_cierre.md  
  - docs/<task>/memories.md  
  - docs/<task>/learning_by_doing.md

↓  

──────────────────────────────────────────────
2. TASK PARSING AND STRUCTURAL HYPOTHESIS
──────────────────────────────────────────────
• Parse the PRD to get a first hypothesis of subtasks  
  (task parse_prd)

• Rearrange, reword, split or combine subtasks manually

• Define expected completion conditions in:  
  docs/<task>/criterios_cierre.md  
  (e.g., specific outputs, logs, runtime behavior, correctness of transformations)

• Set task priorities  
  (task set_priority --task "X" --level high)  

• Define dependencies explicitly  
  (task add_dependency --task "Y" --depends-on "X")

↓  

──────────────────────────────────────────────
3. ITERATIVE IMPLEMENTATION LOOP
──────────────────────────────────────────────

╭──→ [A] FUNCTION DEVELOPMENT  
│ • Write each simple function (single responsibility, no I/O)  
│ • Immediately write and validate a unit test  
│ • Always use real, randomly sampled data (never synthetic or handcrafted)  
│ • Never write a script without a test  
│  
╰──→ [B] FLOW COMPOSITION  
  • Compose simple functions into an orchestrator  
  • Keep orchestrators free of logic, focused on coordination  
  • Prepare to be reused in script entry-points  

↓  

╭──→ [C] SCRIPT CONSTRUCTION AND TESTING  
│ • Write a script that takes real input and runs the orchestrator  
│ • Run it on real data (sampled) with logging  
│ • Check for errors, logs, outputs  
│ • Mark progress in Task Master  
│   (task set_task_status --task "X" --status in-progress)  
│ • Regardless of severity, every implementation issue should trigger:  
│   - Documentation in microtasks.md  
│   - Task creation in Task Master  
│     (task add_task "Investigate null cleaning error")  
│  
╰──→ [D] LLM-ASSISTED REVISION  
  • Use LLM agent to:  
    - Propose refactors  
    - Explore alternatives  
    - Diagnose errors  
  • Never act if certainty < 95%  
  • If certainty is 80–95%, offer options and ask user  
  • If certainty < 80%, never proceed — ask first  
  • If task scope or logic changes:  
    - Update prd.md  
    - Update task-prd-revision.md  
    - Update microtasks.md  
    - Log misassumptions in memories.md  
    - Log procedural learning in learning_by_doing.md  

↓  

╭──→ [E] RE-EXECUTION AND RETEST  
│ • Run again with updated functions and flows  
│ • Validate against criterios_cierre.md  
│ • If failed, repeat the cycle from the appropriate step  
│ • Log what failed, what was changed, and retry  
│  
╰──→ Always ensure everything is reflected in microtasks.md

↓  

──────────────────────────────────────────────
4. FULL VALIDATION AND TESTING
──────────────────────────────────────────────
• Run script(s) on full-sample or edge-case real data  
• Use:  
  - Unit tests to validate functions  
  - Terminal and log outputs to validate flows and scripts  
• Confirm all validation points in criterios_cierre.md  
• Mark task as testing  
  (task set_task_status --task "X" --status testing)

↓  

──────────────────────────────────────────────
5. CLOSURE AND DOCUMENTATION SYNC
──────────────────────────────────────────────
• Mark task as complete in Task Master  
  (task set_task_status --task "X" --status done)

• Archive current microtask in microtasks_stack/

• Update all relevant documentation:  
  - microtasks.md → archived  
  - memories.md → log key failures, discarded paths, reasons  
  - learning_by_doing.md → note procedural, structural improvements  
  - task-prd-revision.md → update structural understanding  
  - criterios_cierre.md → confirm met conditions  
  - README.md → only if it’s relevant to overall project summary  

• Ensure that the pipeline, workflow and TOFA-WDF documents are referenced and aligned

↓  

──────────────────────────────────────────────
CORE PRINCIPLES (MANDATORY)
──────────────────────────────────────────────
• Never develop a script without a unit test  
• Never execute any change without reviewing microtasks, memories and learning_by_doing  
• Never modify logic without writing what was changed, why, and what failed before  
• Never assume a plan is valid until the implementation validates it  
• Never drop a failure without understanding why it failed  
• Never abandon a failed path without retrying or exploring alternatives  
• Never mark a task as done without:  
  - Closing the microtask  
  - Logging what worked and what didn’t  
  - Writing what was learned  
  - Documenting new strategic knowledge in memories  