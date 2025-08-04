# Helper Scripts (docs_scripts_readme)

This project ships a small set of helper scripts for documentation consolidation and GitHub workflow automation.

Location: scripts/

- docs/integrate_tofa_docs.py
  - Purpose: Generate a consolidated .all_tofa.md at the project root for LLM context.
  - Usage:
    - python scripts/docs/integrate_tofa_docs.py
  - Notes:
    - Writes ONLY to /.all_tofa.md
    - Reads from: docs/, .github/instructions/, .taskmaster/ (source of truth)
- installers/github_local_sync_installer/install_github_uploader.sh
  - Purpose: Install upload_to_github command to /usr/local/bin
  - Usage:
    - chmod +x scripts/installers/github_local_sync_installer/install_github_uploader.sh
    - sudo scripts/installers/github_local_sync_installer/install_github_uploader.sh
  - Then:
    - upload_to_github <repo-url-without-.git> "Commit message"
- installers/github_project_creator_tofa/install_github_project_creator_tofa.sh
  - Purpose: Install add_project_tofa command to /usr/local/bin
  - Usage:
    - chmod +x scripts/installers/github_project_creator_tofa/install_github_project_creator_tofa.sh
    - sudo scripts/installers/github_project_creator_tofa/install_github_project_creator_tofa.sh
  - Then:
    - add_project_tofa <template-repo> <project_name> "description"

Policy:
- Do not duplicate these scripts under docs/.
- The consolidated .all_tofa.md is non-canonical; canonical docs live in docs/.

Naming convention note:
- Only the repository root uses README.md.
- All other readme-like docs must include a context-specific suffix in the filename.
- This document title reflects its intended filename pattern: docs_scripts_readme.md.
