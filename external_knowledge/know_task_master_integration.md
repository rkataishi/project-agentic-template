# Task Master Integration Guide (TOFA-WDF)

This guide explains how the **Task Master CLI** is integrated into the TOFA-WDF project structure. It maps the commands to your TOFA documents and execution flow, showing where they interact and how they are reflected.

---

## 1. Installation

Inside your working environment:

```bash
pip install task-master
```

If using conda:

```bash
conda activate <env_name>
pip install task-master
```

---

## 2. Initialization

Run once from the root of the project:

```bash
task init
```

This creates `.taskmaster/` and sets up basic project config.

---

## 3. CLI Commands and TOFA Interactions

| Task Master Command | Affected TOFA File(s) | Purpose |
|-------------------|----------------------|---------|
| `task prd "Task name"` | `pipeline/prd.md` + scaffold | Creates initial Product Requirement Document |
| `task parse_prd` | `pipeline/microtasks.md` (structure only) | Scaffolds sections for active microtask record |
| `task add_task "new subtask"` | none (CLI state only) | Adds a node to the task tree, not tracked in TOFA yet |
| `task set_task_status --task X --status Y` | `pipeline/microtasks_log.md` | Updates state reflected in logs and MCP-compatible tools |
| `task list` | CLI/interactive only | Lists task tree states and open/closed subtasks |

---

## 4. Roles and Separation of Responsibility

| Source | Responsible For |
|--------|------------------|
| `task prd` | Scaffolds project with TOFA structure |
| `pipeline/prd.md` | Defines the plan, objectives, and motivations |
| `pipeline/microtasks.md` | Describes the active microtask: includes current objective, its constraints, reasoning path, and expected result |
| `task parse_prd` | Can fill preliminary structure in microtasks.md, but does not define the plan |
| Developer | Manually writes the plan in prd.md and the current objective in microtasks.md |

---

## 5. Integration Lifecycle (Typical Use Case)

1. **Define PRD**
   ↓
   `task prd "Extract firm innovation patterns"`

2. **(Optional) Parse it**
   ↓
   `task parse_prd`

3. **Write implementation plan manually in:**
   - `pipeline/prd.md` (goals, constraints, rationale)
   - `pipeline/microtasks.md` (active microtask record)

4. **Work on code**
   ↓
   - `modules/` → `orchestrators/` → `flows/` → `scripts/`

5. **Use status commands as needed:**
   - `task set_task_status --task "X" --status in-progress`

6. **Finalize, close task:**
   - `task set_task_status --task "X" --status done`

7. **Archive:**
   - Move to `microtasks_done/`
   - Log in `microtasks_log.md`
   - Document in `memories.md` and `learning_by_doing.md`

---

## 6. MCP Compatibility

You can integrate Task Master into LLM pipelines, IDE agents, or model coordination by defining:

```json
{
  "mcpServers": {
    "task": {
      "command": "task",
      "args": ["status"],
      "disabled": false,
      "autoApprove": [],
      "timeout": 60
    }
  }
}
```

This allows other tools to interact with your current task state.

---

## 7. Summary

Task Master is not a replacement for TOFA. It is a coordination assistant.

All plans, reasoning, and documentation must be written directly in:
- `pipeline/prd.md`
- `pipeline/microtasks.md`
- `pipeline/memories.md`
- `pipeline/learning_by_doing.md`

The task CLI helps track status, list subtasks, assign tags, and initiate PRDs—but never generates logic or strategies.