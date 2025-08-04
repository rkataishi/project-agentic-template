# Project Onboarding: Your Starting Point

Welcome to the project. This document is your guide to getting set up, understanding our workflow, and contributing effectively. **Read this entire document before writing any code.**

Its purpose is to be your onboarding lead, your initial set of instructions, and a central hub that links to all other critical documentation. Following these steps will allow you to start working autonomously and correctly.

**Assumption:** The initial Product Requirements Document (`prd.md`) has been created and is located at `docs/pipeline/active/prd.md`.

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

# Ensure PRD exists (or create it using the template)
# If you already have a PRD at docs/pipeline/active/prd.md, skip this copy.
cp docs/templates/template_task_contract.md docs/pipeline/active/prd.md

# Parse the PRD to generate initial tasks
task-master parse-prd docs/pipeline/active/prd.md

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
    -   **Location:** `docs/pipeline/active/prd.md`

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

## Quick Reference Links

- **Project Root:** `docs/pipeline/active/`
- **Rules:** `docs/rules/`
- **Templates:** `docs/templates/`
- **ADRs:** `docs/adr/`
- **Configuration:** `config/`

---

**Welcome aboard! If you have questions, check the documentation first, then ask in the project chat.**