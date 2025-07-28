Excellent. Your feedback is sharp and moves the project from a well-defined process to an industrial-grade, scalable framework. By focusing on these areas, you are proactively solving the problems of team growth, long-term maintenance, and production readiness.

Let's implement all of these changes. I will provide the complete text for the five new files you've approved.

### Clarification on `pyproject.toml`

You asked if `pyproject.toml` should go inside `config/`. **No, it must be placed in the project's root directory.**

*   **Why?** Tools like `pip`, `poetry`, `black`, `ruff`, and `mypy` are designed to automatically detect `pyproject.toml` in the root of the repository. This is a universal standard. Placing it anywhere else would break this automated discovery and require complex, non-standard configurations for every tool.

---

Here are the new documents that will complete your project roadmap.

### 1. The Onboarding Hub and Guide

This is the new "front door" for any developer joining the project. It's designed to be the central hub you described.

--- START OF FILE docs/onboarding.md ---

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
--- START OF FILE docs/rules/rule_code_quality.md ---

# Rule: Code Quality & Automated Tooling

To ensure consistency, readability, and prevent common errors, this project mandates the use of automated code quality tools. These are not optional.

---

### **Note on `pyproject.toml` Location**

The `pyproject.toml` file **must** reside in the project's root directory. This is the industry-standard location that all modern Python tools expect. Do not move it.

---

## 1. Code Formatting: Black

-   **Tool:** [Black](https://github.com/psf/black), the uncompromising code formatter.
-   **Purpose:** Eliminates all arguments about code style. Black's style is non-negotiable and automatically applied.
-   **Configuration (`pyproject.toml`):**
    ```toml
    [tool.black]
    line-length = 88
    target-version = ['py310'] # Or your target Python version
    ```
-   **Usage:**
    ```bash
    # To format all files in the project
    poetry run black .
    ```

## 2. Linting: Ruff

-   **Tool:** [Ruff](https://github.com/astral-sh/ruff), an extremely fast Python linter.
-   **Purpose:** Catches a wide range of errors, from unused imports to logical mistakes, and enforces best practices (including PEP 8).
-   **Configuration (`pyproject.toml`):**
    ```toml
    [tool.ruff]
    line-length = 88
    select = [
        "E",  # pycodestyle errors
        "W",  # pycodestyle warnings
        "F",  # pyflakes
        "I",  # isort
        "C",  # flake8-comprehensions
        "B",  # flake8-bugbear
    ]
    ignore = ["E501"] # Ignored by Black's line wrapping
    ```
-   **Usage:**
    ```bash
    # To check all files for errors
    poetry run ruff .

    # To automatically fix fixable errors
    poetry run ruff . --fix
    ```

## 3. Pre-Commit Hooks (Recommended)

To automate these checks, it is highly recommended to use [pre-commit](https://pre-commit.com/). This ensures that no code that violates our quality standards is ever committed. A `.pre-commit-config.yaml` file should be present in the root directory.
---
--- START OF FILE docs/rules/rule_dependency_management.md ---

# Rule: Dependency Management

To ensure a reproducible and stable environment, this project mandates a strict policy for managing external dependencies.

## 1. Tooling: Poetry

-   **Official Tool:** [Poetry](https://python-poetry.org/) is the sole authority for managing dependencies and virtual environments.
-   **Reasoning:** Poetry provides deterministic builds via the `poetry.lock` file, unified dependency and environment management, and a clean `pyproject.toml` standard.

## 2. Installing Dependencies

-   **Command:** Never use `pip install`. Always use Poetry to install dependencies from the lock file.
    ```bash
    # This installs the exact versions specified in poetry.lock
    poetry install
    ```

## 3. Adding a New Dependency

-   **Command:** Use the `poetry add` command. This will update both `pyproject.toml` and `poetry.lock`.
    ```bash
    # Add a new production dependency
    poetry add pandas

    # Add a new development-only dependency (e.g., for testing)
    poetry add pytest --group dev
    ```
-   **Action:** After adding a dependency, commit both the `pyproject.toml` and `poetry.lock` files together in the same commit.

## 4. Updating Dependencies

-   **Command:** Use `poetry update` to safely upgrade packages according to the version constraints in `pyproject.toml`.
    ```bash
    # Update all dependencies
    poetry update

    # Update a single package
    poetry update pandas
    ```
-   **Caution:** Run the test suite (`poetry run pytest`) immediately after updating to catch any breaking changes.
---
--- START OF FILE docs/rules/rule_security_guidelines.md ---

# Rule: Security Guidelines

Security is not an afterthought; it is a core design principle. All code must adhere to the following guidelines.

## 1. Secrets Management

-   **Principle:** Secrets (API keys, tokens, passwords) **must never** be hardcoded or committed to the repository.
-   **Mechanism:**
    1.  All secrets must be defined as environment variables in a local `.env` file at the project root.
    2.  The `.env` file is listed in `.gitignore` and must never be committed.
    3.  The `config/config.py` file is the only place where environment variables are read into the application. Other parts of the code must import them from `config`.

## 2. Input Validation

-   **Principle:** Never trust input.
-   **Action:** The assumption "All inputs are assumed to be pre-validated" is a temporary convenience for isolated development. For any function that could potentially receive external data (file uploads, API calls, user-provided parameters), perform explicit validation.
    -   Check data types (e.g., using Pydantic or simple type assertions).
    -   Sanitize inputs to prevent injection attacks.
    -   Validate file paths to prevent directory traversal.

## 3. Dependency Vulnerability Scanning

-   **Principle:** Our code is only as secure as its dependencies.
-   **Action:** Regularly scan project dependencies for known vulnerabilities.
-   **Recommended Tool:** Use `pip-audit` or `safety` via Poetry.
    ```bash
    # Install pip-audit
    pip install pip-audit

    # Run the audit against the Poetry environment
    poetry run pip-audit
    ```
-   **Policy:** Any "High" or "Critical" vulnerability must be addressed immediately, either by updating the package or replacing it.
---
--- START OF FILE docs/rules/rule_knowledge_management.md ---

# Rule: Knowledge Management & Architecture Decisions

To prevent knowledge loss and ensure that our documentation remains valuable, we follow a strict protocol for managing long-term learnings and architectural decisions.

## 1. The Knowledge Synthesis & Archiving Protocol

-   **Problem:** `memories.md` and `learning_by_doing.md` can become bloated and unreadable over time, hiding valuable insights.
-   **Trigger:** This protocol is executed at the end of a major epic, a significant feature release, or at minimum, on a quarterly basis.
-   **Process:**
    1.  **Synthesize:** A designated developer reads through the active `memories.md` and `learning_by_doing.md`.
    2.  **Extract & Formalize:** Key strategic decisions, discarded architectural paths, and permanent process improvements are extracted and formalized into **Architecture Decision Records (ADRs)**. See below for details.
    3.  **Archive:** The content of the active `memories.md` and `learning_by_doing.md` is moved to a dated file in the archive (e.g., `docs/pipeline/active/archive/memories_q3_2025.md`).
    4.  **Reset:** The active `memories.md` and `learning_by_doing.md` are reset using their respective templates from `docs/templates/`.

## 2. Architecture Decision Records (ADRs)

-   **Purpose:** An ADR is a short document that captures a single, significant architectural decision. It is the permanent, high-level memory of the project.
-   **When to Create an ADR:**
    -   A decision that impacts the overall structure (e.g., choosing a new database, adopting a new library for a core function).
    -   A decision that has long-term consequences and trade-offs.
    -   A decision that a new developer must understand to grasp the "why" behind the codebase.
-   **Location:** ADRs are stored in a new top-level directory: `docs/adr/`.
-   **Format:** Create new ADRs by copying `docs/templates/template_adr.md`.
---
--- START OF FILE docs/templates/template_adr.md ---

# ADR-XXX: [Title of Decision]

-   **Status:** [Proposed | Accepted | Deprecated | Superseded by ADR-YYY]
-   **Date:** [YYYY-MM-DD]

## Context

*What is the issue that we're seeing that is motivating this decision or change? What is the context in which we are making this decision?*

---

## Decision

*What is the change that we're proposing and/or doing? This should be stated in full sentences, active voice.*

---

## Consequences

*What becomes easier or more difficult to do because of this change? What are the positive, negative, and neutral consequences? This section is critical for future decision-making.*
---