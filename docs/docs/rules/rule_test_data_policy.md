# Test Data Management Policy

## Folder Structure
Each task stores test samples in:

tasks/<task_name>/test_data/

## Requirements
- Use real data samples only (no synthetic)
- Prefer `.csv` or `.json` format
- Redact if needed, but preserve structure
- Document assumptions in `microtasks.md`

## Maintenance
- Each module's unit test must operate on a real example from this folder
- No function is valid without test coverage using data from here