# compile_all_tofa_docs.py

import os
import subprocess

# IMPORTANT:
# - This script lives in scripts/docs/
# - It must write ONLY to the project root '.all_tofa.md'
# - It must read canonical sources from repo root (docs/, .github/instructions/, .taskmaster/)
SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
# scripts/docs/ -> repo root is two levels up
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))

doc_root = REPO_ROOT
external_dirs = [
    os.path.join(REPO_ROOT, ".github", "instructions"),
    os.path.join(REPO_ROOT, ".taskmaster"),
]

all_dirs = [doc_root] + external_dirs
output_file = os.path.join(REPO_ROOT, ".all_tofa.md")
output_lines = []

# Header (English, with source-of-truth notice)
output_lines.append("# TOFA-WDF documentation consolidated (non-canonical)\n")
output_lines.append("> IMPORTANT: This file is auto-generated for LLM context only. It is NOT canonical documentation.\n")
output_lines.append("> Source of truth remains in docs/, .github/instructions/, and .taskmaster/ files.\n")

# Included directory trees
output_lines.append("## Included directory trees\n")
output_lines.append("```")
for path in all_dirs:
    # Show relative path for readability
    rel = os.path.relpath(os.path.normpath(path), start=REPO_ROOT)
    output_lines.append(f"# {rel}")
    try:
        tree_output = subprocess.check_output(
            ["tree", "-a", "-I", "__pycache__|.DS_Store|*.pyc|_*", "-L", "5", path],
            encoding="utf-8",
        )
        output_lines.append(tree_output.strip())
    except Exception as e:
        output_lines.append(f"[INFO] tree unavailable or failed for {rel}: {e}")
output_lines.append("```\n")

# Consolidated documentation
output_lines.append("## Consolidated documentation\n")

for base_dir in all_dirs:
    for root, _, files in os.walk(base_dir):
        for file in sorted(files):
            if (
                file.startswith(".")
                or file.startswith("_")
                or file.endswith(".DS_Store")
            ):
                continue
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, start=REPO_ROOT)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                output_lines.append("\n" + "=" * 119 + "\n")
                output_lines.append(f"## FILE: `{rel_path}`\n")
                output_lines.append("```markdown")
                output_lines.append(content.strip())
                output_lines.append("```")
            except Exception as e:
                output_lines.append("\n" + "=" * 119 + "\n")
                output_lines.append(f"## ERROR: Could not read {rel_path} - {str(e)}\n")

# Final write to root
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))