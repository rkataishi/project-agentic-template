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