# Task Master Integration Guide (TOFA-WDF)

This guide explains how the **Task Master CLI** is integrated into the TOFA-WDF project structure. It maps the commands to your TOFA documents and execution flow, showing where they interact and how they are reflected.

---

## 1. Installation

Install the CLI globally (recommended):

```bash
npm install -g task-master-ai
```

Verify installation:

```bash
task-master --version
```

---

## 2. Initialization

Run once from the root of the project:

```bash
task-master init -y
```

This creates `.taskmaster/` and sets up basic project config.

---

## 3. CLI Commands and TOFA Interactions

The canonical CLI is `task-master`. Command names, flags, and usage align with the authoritative help reference in [docs/docs/external_knowledge/know_task_master_help.md](docs/docs/external_knowledge/know_task_master_help.md).

| Task Master Command | Affected TOFA File(s) | Purpose |
|---------------------|-----------------------|---------|
| `task-master parse-prd docs/pipeline/active/prd.md` | Generates `.taskmaster/tasks/tasks.json` | Parse PRD to generate initial tasks |
| `task-master add-task -p "New task"` | Tasks JSON only | Adds a new task via AI |
| `task-master set-status --id=5 --status=done` | Tasks JSON only | Update task status |
| `task-master list` | CLI output | Lists task tree states and open/closed subtasks |
| `task-master next` | CLI output | Suggests the next task to work on |

---

## 4. Roles and Separation of Responsibility

| Source | Responsible For |
|--------|------------------|
| `task-master init` | Initialize Task Master project structure |
| `docs/pipeline/active/prd.md` | Defines the plan, objectives, and motivations |
| `docs/pipeline/active/microtasks.md` | Describes the active microtask: includes current objective, constraints, reasoning, expected result |
| `task-master parse-prd` | Generates tasks from the PRD (does not define the plan) |
| Developer | Manually writes the plan in prd.md and the current objective in microtasks.md |

---

## 5. Integration Lifecycle (Typical Use Case)

1. **Define PRD**
   ↓
   Edit: `docs/pipeline/active/prd.md`

2. **Parse PRD**
   ↓
   `task-master parse-prd docs/pipeline/active/prd.md`

3. **Write implementation plan manually in:**
   - `pipeline/prd.md` (goals, constraints, rationale)
   - `pipeline/microtasks.md` (active microtask record)

4. **Work on code**
   ↓
   - `modules/` → `orchestrators/` → `flows/` → `scripts/`

5. **Use status commands as needed:**
   - `task-master set-status --id=<id> --status=in-progress`

6. **Finalize, close task:**
   - `task-master set-status --id=<id> --status=done`

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
    "task-master": {
      "command": "task-master",
      "args": ["list"],
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
- `docs/pipeline/active/prd.md`
- `docs/pipeline/active/microtasks.md`
- `docs/pipeline/memories.md`
- `docs/pipeline/learning_by_doing.md`

The `task-master` CLI helps track status, list subtasks, manage tags, and parse PRDs—but never generates logic or strategies.