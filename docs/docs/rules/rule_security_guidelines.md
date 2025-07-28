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