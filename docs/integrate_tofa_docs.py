# integrate_tofa_docs.py

import os
import re
import subprocess
from typing import List, Tuple

# Root relative to docs/
DOC_ROOT = "."
OUTPUT_FILE = ".all_tofa.md"

# Explicit include list (ordered). Paths are relative to repo root or DOC_ROOT as noted.
INCLUDE_FILES: List[str] = [
    "../README.md",
    "../onboarding.md",
    "onboarding.md",
    "pipeline/active/prd.md",
    "pipeline/active/microtasks.md",
    "pipeline/tags/master/pipeline_development.md",
    "pipeline/tags/master/pipeline_pickup.md",
    "external_knowledge/know_task_master_integration.md",
    # Optional authoritative help if present
    "docs/external_knowledge/know_task_master_help.md",  # note: this may not exist
    # Taskmaster workflow references
    "../.github/instructions/dev_workflow.md",
    "../.github/instructions/taskmaster.md",
    # Taskmaster configs
    "../.taskmaster/config.json",
    "../.taskmaster/state.json",
    "../.taskmaster/templates/example_prd.txt",
]

# Include limited directory trees for orientation
TREE_PATHS: List[str] = [
    ".",  # docs/
    "../.github/instructions",
    "../.taskmaster",
]

# Filters: UI boilerplate and repetitive noise patterns
UI_PREFIXES = (
    "Search...",
    "⌘K",
    "Navigation",
    "Was this page helpful?",
    "Assistant",
    "YesNo",
)

UI_CONTAINS = (
    "Responses are generated using AI and may contain mistakes.",
    "##### Welcome",
    "* * *",
)

# Compile regexes
RE_TRIPLE_BACKTICK = re.compile(r"^```")
RE_DASH_LINE = re.compile(r"^[-—]{3,}$")
RE_ERROR_TREE = re.compile(r"^\\[ERROR\\] No se pudo generar tree para ")
RE_MULTIBLANK = re.compile(r"\\n{3,}")

def is_code_fence(line: str) -> bool:
    return bool(RE_TRIPLE_BACKTICK.match(line.strip()))

def should_filter_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    # UI prefixes
    for p in UI_PREFIXES:
        if stripped.startswith(p):
            return True
    # Common UI fragments
    for c in UI_CONTAINS:
        if c in stripped:
            return True
    # Horizontal rule spam
    if RE_DASH_LINE.match(stripped):
        return True
    return False

def filter_content(text: str) -> Tuple[str, List[str]]:
    """
    Filter UI/boilerplate lines while preserving fenced code blocks.
    Aggregate tree error lines into a summary.
    Collapse excessive blank lines.
    """
    lines = text.splitlines()
    filtered: List[str] = []
    errors: List[str] = []
    in_code = False

    for line in lines:
        if is_code_fence(line):
            in_code = not in_code
            filtered.append(line)
            continue
        if in_code:
            filtered.append(line)
            continue

        # Collect tree error lines
        if RE_ERROR_TREE.match(line):
            errors.append(line.strip())
            continue

        # Drop UI/boilerplate lines
        if should_filter_line(line):
            continue

        filtered.append(line)

    result = "\n".join(filtered)
    # Collapse multi-blank lines to a single blank
    result = RE_MULTIBLANK.sub("\n\n", result)
    return result.strip(), errors

def safe_read(path_from_docs: str) -> Tuple[str, str]:
    """
    Read file content. path_from_docs is relative to docs/ unless starts with '../'
    Returns (rel_label_for_header, content) or raises.
    """
    if path_from_docs.startswith("../"):
        abs_path = os.path.normpath(os.path.join(DOC_ROOT, path_from_docs))
        label = path_from_docs
    else:
        abs_path = os.path.normpath(os.path.join(DOC_ROOT, path_from_docs))
        label = os.path.relpath(abs_path, start=DOC_ROOT)
    with open(abs_path, "r", encoding="utf-8") as f:
        return label, f.read()

def try_tree(path: str) -> Tuple[str, str]:
    label = os.path.normpath(path)
    try:
        output = subprocess.check_output(
            ["tree", "-a", "-I", "__pycache__|.DS_Store|*.pyc|_*", "-L", "5", path],
            encoding="utf-8",
            stderr=subprocess.STDOUT,
        )
        return label, output.strip()
    except Exception as e:
        return label, f"[INFO] tree unavailable or failed for {path}: {e}"

def resolve_active_file(relative_path: str) -> str:
    """
    Resolve docs/pipeline/active/* symlink target if 'active' is a symlink.
    If not a symlink or missing, return the input relative path as-is.
    """
    # Expect inputs like 'pipeline/active/prd.md' relative to DOC_ROOT
    parts = relative_path.split("/")
    try:
        idx = parts.index("active")
    except ValueError:
        return relative_path
    active_dir = os.path.join(DOC_ROOT, *parts[: idx + 1])
    if os.path.islink(active_dir):
        target = os.readlink(active_dir)  # may be relative
        # Build resolved path replacing 'active' with its target
        resolved_parts = parts[:]
        resolved_parts[idx] = target.rstrip("/")

        resolved = os.path.normpath(os.path.join(DOC_ROOT, *resolved_parts))
        # Return path relative to DOC_ROOT for reading via safe_read
        return os.path.relpath(resolved, start=DOC_ROOT)
    return relative_path

def main():
    output_lines: List[str] = []

    # Header banner
    output_lines.append("# TOFA-WDF documentation consolidated (non-canonical)")
    output_lines.append("")
    output_lines.append("> IMPORTANT: This file is auto-generated for LLM context only. It is NOT canonical documentation.")
    output_lines.append("> Source of truth remains in docs/, .github/instructions/, and .taskmaster/ files.")
    output_lines.append("")

    # Directory trees
    output_lines.append("## Included directory trees")
    output_lines.append("```")
    for p in TREE_PATHS:
        label, tree_txt = try_tree(p)
        output_lines.append(f"# {label}")
        output_lines.append(tree_txt)
    output_lines.append("```")
    output_lines.append("")

    # Consolidated docs
    output_lines.append("## Consolidated documentation")
    aggregated_errors: List[str] = []

    for rel in INCLUDE_FILES:
        # Resolve 'active' symlinked files first
        rel_for_docs = resolve_active_file(rel if not rel.startswith("../") else rel)
        try:
            label, raw = safe_read(rel_for_docs)
            filtered, errs = filter_content(raw)
            aggregated_errors.extend(errs)
            output_lines.append("\n" + "=" * 120)
            output_lines.append(f"\n## FILE: `{label}`\n")
            output_lines.append("```markdown")
            output_lines.append(filtered)
            output_lines.append("```")
        except Exception as e:
            output_lines.append("\n" + "=" * 120)
            output_lines.append(f"\n## ERROR: Could not read {rel_for_docs} - {str(e)}\n")

    # Append filtered error summary (if any)
    if aggregated_errors:
        output_lines.append("\n" + "=" * 120)
        output_lines.append("\n## Filtered Errors Summary\n")
        output_lines.append("The following tree-related errors were filtered from inline content and summarized here:\n")
        for err in aggregated_errors:
            output_lines.append(f"- {err}")

    # Final write
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()