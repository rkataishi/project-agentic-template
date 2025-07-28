# Project Onboarding: Your Starting Point

Welcome to the project. This document is your guide to getting set up, understanding our workflow, and contributing effectively. **Read this entire document before writing any code.**

Its purpose is to be your onboarding lead, your initial set of instructions, and a central hub that links to all other critical documentation. Following these steps will allow you to start working autonomously and correctly.

**Assumption:** The initial Product Requirements Document (`prd.md`) has been created and is located at `docs/pipeline/active/prd.md`.

---

## Step 1: Initial Environment Setup

These commands will prepare your local environment.

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```

2.  **Create the Project Structure (if not already present):**
    ```bash
    # This script creates all the necessary directories and template files.
    chmod +x setup_pipeline.sh
    ./setup_pipeline.sh
    ```

3.  **Set up the Python Environment (using Poetry):**
    *Our project uses [Poetry](https://python-poetry.org/) for dependency management. See `docs/rules/rule_dependency_management.md` for details.*
    ```bash
    # This command reads pyproject.toml, creates a virtual environment, and installs all dependencies.
    poetry install
    ```

4.  **Configure Local Secrets:**
    *This is a critical security step. We never commit secrets to the repository.*
    ```bash
    # 1. Copy the template to create your local, untracked config file.
    cp docs/templates/config/template_config.py config/config.py

    # 2. Create a .env file for your secrets. This file is in .gitignore.
    touch .env
    ```
    **Action:** Open the `.env` file and add your secret keys (e.g., `OPENAI_API_KEY="sk-..."`). The `config/config.py` file will load these automatically.

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

## Step 4: Your First Task

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