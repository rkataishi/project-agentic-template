# Project Onboarding: Your Starting Point

Welcome to the project. This document is your guide to getting set up, understanding our workflow, and contributing effectively. **Read this entire document before writing any code.**

Its purpose is to be your onboarding lead, your initial set of instructions, and a central hub that links to all other critical documentation. Following these steps will allow you to start working autonomously and correctly.

**PRD Source of Truth:** We maintain PRDs under `docs/prd/`. Create or update your working PRD at:
- `docs/prd/current_prd.md` (recommended)

Use the template and example provided:
- Template: [`docs/templates/template_prd.md`](docs/templates/template_prd.md)
- Example: [`docs/templates/example_prd.md`](docs/templates/example_prd.md)

---

## Step 1: Initial Setup and Task Master Configuration

These steps will prepare your local environment and configure Task Master.

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```

2.  **Create the Project Structure (if not already present):**
*This script creates all the necessary directories and template files.*
```bash
chmod +x setup_pipeline.sh
./setup_pipeline.sh
```

3.  **Set up the Python Environment (using Poetry):**
*Our project uses [Poetry](https://python-poetry.org/) for dependency management. See `docs/rules/rule_dependency_management.md` for details.*
*Ensure `pyproject.toml` is present in the project root. If missing, refer to project documentation or use a template.*
```bash
# This command reads pyproject.toml, creates a virtual environment, and installs all dependencies.
poetry install
```

4.  **Task Master Setup:**
*Install Task Master CLI, initialize the project, and configure models and API keys.*
```bash
# Install Task Master CLI
npm install -g task-master-ai

# Verify installation
task-master --version

# Initialize Task Master
task-master init -y

# PRD templates are under docs/templates/, the working PRD required by the workflow must live under docs/prd/
# Create the PRD folder and base file from the template (if you don't already have one)
mkdir -p docs/prd
cp docs/templates/template_prd.md docs/prd/current_prd.md

# Parse the PRD (content‑rich, adapted from template) to generate initial tasks
task-master parse-prd docs/prd/current_prd.md -o .taskmaster/tasks/tasks.json -n 8 -f

# Optional: Configure AI models (guided)
task-master models --setup

# Configure API keys:
# - CLI: place provider keys in .env (e.g., OPENROUTER_API_KEY=..., ANTHROPIC_API_KEY=..., OPENAI_API_KEY=...)
# - MCP/IDE: configure keys in .vscode/mcp.json (or your IDE's MCP config)
```
*Only add keys required by your chosen provider. Use one provider to start (e.g., OpenRouter) to simplify setup.*
 
5.  **Configure Local Secrets:**
*This is a critical security step. We never commit secrets to the repository.*
```bash
# 1. Copy the template to create your local, untracked config file.
cp docs/templates/config/template_config.py config/config.py

# 2. Create a .env file for your secrets. This file is in .gitignore.
touch .env
```
**Action:** Open the `.env` file and add your secret keys (e.g., `OPENROUTER_API_KEY="..."`). The `config/config.py` file will load these automatically.

5.  **Verify Your Setup:**
    *Run the project's test suite to ensure everything is installed and configured correctly.*
    ```bash
    poetry run pytest
    ```
    If all tests pass, your environment is ready.

---

## Step 2: Understand the Mission and Workflow

Your next step is to absorb the project's context.

-   **The "Why" (The Mission):**
    -   **Action:** Read the Product Requirements Document (PRD).
    -   **Location:** `docs/prd/current_prd.md`

PRD workflow requirements:
- PRD templates live under: [`docs/templates/`](docs/templates/)
  - Start from: [`docs/templates/template_prd.md`](docs/templates/template_prd.md) or the example: [`docs/templates/example_prd.md`](docs/templates/example_prd.md)
- The actual, required PRD used by the workflow must live under: `docs/prd/` as a file (recommended name: `docs/prd/current_prd.md`).
  - The template is a prerequisite: you copy/adapt it to produce a content‑rich PRD that guides the end‑to‑end workflow.
  - Once authored, this PRD is parsed by Task Master to generate `.taskmaster/tasks/tasks.json`, then expanded and generated into task files per our workflow.

-   **The "How" (The Development Process):**
    -   **Action:** This is a **mandatory reading**. It defines our entire development lifecycle.
    -   **Location:** `docs/pipeline/pipeline_development.md`

-   **Resuming Work:**
    -   **Action:** Familiarize yourself with the checklist for picking up work after a break.
    -   **Location:** `docs/pipeline/pipeline_pickup.md`

---

## Step 3: Understand the Rules and Principles

This project is governed by a set of rules to ensure quality, consistency, and security. It is your responsibility to know and follow them.

-   **The Rulebook:**
    -   **Action:** Review the contents of the `docs/rules/` directory. All files within are mandatory.
    -   **Key Rules to Internalize:**
        -   `rule_code_quality.md`: How we write and format code (Black, Ruff).
        -   `rule_doc_guidelines.md`: Naming conventions and documentation standards.
        -   `rule_security_guidelines.md`: Our policies on handling secrets and data.
        -   `rule_knowledge_management.md`: How we document decisions using ADRs.

-   **Core Behavioral Principles:**
    1.  **Documentation First:** Changes to standards or architecture are documented *before* they are coded.
    2.  **Traceability is Non-Negotiable:** Every piece of logic must be traceable back to a plan in `microtasks.md`.
    3.  **No Silent Failures:** Code must fail loudly and explicitly. Errors are valuable data.
    4.  **Automate Quality:** Rely on linters and formatters, not manual perfection.
    5.  **Commit Defensively:** Write clear commit messages. Ensure your code is linted and tested before you push.

---

## Step 4: Context Management with Tags

For advanced workflows, this project uses tags to manage different task contexts (features, experiments, etc.). See `docs/pipeline/pipeline_development.md` for details on creating and switching between tags and how tags interplay with Task Master tasks.json.

---

## Step 5: Your First Task

You are now ready to begin.

1.  **Find Your Next Task:**
    ```bash
    # Use the Task Master CLI to see the task list or get a recommendation.
    task-master list
    task-master next
    ```

2.  **Review the Active Plan:**
    -   **Action:** Read the current plan for your assigned task.
    -   **Location:** `docs/pipeline/active/microtasks.md`

3.  **Begin the Development Cycle:**
    -   **Action:** Follow the process outlined in `docs/pipeline/pipeline_development.md`.

---

## Helper Scripts (packaged)

The project ships helper tools under `scripts/`:

- `scripts/docs/integrate_tofa_docs.py`
  - Generates consolidated `.all_tofa.md` at project root for LLM context.
  - Run: `python scripts/docs/integrate_tofa_docs.py`
  - Sources of truth: `docs/`, `.github/instructions/`, `.taskmaster/`
- `scripts/installers/github_local_sync_installer/install_github_uploader.sh`
  - Installs `upload_to_github` to `/usr/local/bin`.
  - Usage:
    - `chmod +x scripts/installers/github_local_sync_installer/install_github_uploader.sh`
    - `sudo scripts/installers/github_local_sync_installer/install_github_uploader.sh`
  - Then:
    - `upload_to_github <repo-url-without-.git> "Commit message"`
- `scripts/installers/github_project_creator_tofa/install_github_project_creator_tofa.sh`
  - Installs `add_project_tofa` to `/usr/local/bin`.
  - Usage:
    - `chmod +x scripts/installers/github_project_creator_tofa/install_github_project_creator_tofa.sh`
    - `sudo scripts/installers/github_project_creator_tofa/install_github_project_creator_tofa.sh`
  - Then:
    - `add_project_tofa <template-repo> <project_name> "description"`

Notes:
- Do not duplicate scripts under `docs/`.
- `.all_tofa.md` is non-canonical; canonical documentation is in `docs/`.

Documentation naming policy:
- Only the repository root uses `README.md`.
- All other readme-like documents must include a context-specific suffix in the filename.
- The scripts docs live here in onboarding and under `docs/scripts/` content files, not `README.md`.


## Current Project Structure (essential paths)

The canonical documentation lives in `docs/`. Helper tools live in `scripts/`.

```
.
├── .add_context_results
│   └── docs_task-master
├── .all_tofa.md
├── .context
│   └── docs_task-master.md
├── .env
├── .github
│   └── instructions
├── .gitignore
├── .taskmaster
│   ├── config.json
│   ├── state.json
│   └── templates
├── .versions
│   ├── .archive
│   ├── my_workflow.md
│   ├── pipeline.md
│   ├── sitemap_stats.log
│   ├── TOFA-WDF.md
│   ├── v2 pipeline.md
│   ├── v2 TOFA-WDF.md
│   ├── v2 workflow.md
│   ├── v3_architectural_best_practices.md
│   ├── v3_development_pipeline.md
│   ├── v3_pickup.md
│   └── v3_workflow.md
├── .vscode
│   └── mcp.json
├── docs
│   ├── adr
│   ├── external_knowledge
│   ├── github_local_sync_installer
│   ├── github_project_creator_tofa
│   ├── onboarding
│   ├── onboarding.md
│   ├── pipeline
│   ├── rules
│   ├── scripts
│   └── templates
├── improvements.md
├── LICENSE
├── next.md
├── onboarding.md
├── README.md
└── scripts
    ├── docs
    └── installers

24 directories, 24 files
```

## Quick Reference Links

- **Project Root:** `docs/pipeline/active/`
- **PRD (required for workflow):** `docs/prd/current_prd.md`
- **PRD Templates (prerequisite source):** `docs/templates/`
- **Rules:** `docs/rules/`
- **Templates:** `docs/templates/`
- **ADRs:** `docs/adr/`
- **Configuration:** `config/`
- **Scripts:** `scripts/`

---

**Welcome aboard! If you have questions, check the documentation first, then ask in the project chat.**