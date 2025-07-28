# Rule: Code Quality & Automated Tooling

To ensure consistency, readability, and prevent common errors, this project mandates the use of automated code quality tools. These are not optional.

---

## **Note on `pyproject.toml` Location**

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