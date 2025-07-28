# Documentation Guidelines (Minimal Style)

## Function Documentation
Use inline comments above each function:

```python
# This function loads a CSV and drops NA rows
def clean_data(df):
    ...
```

Deeper Reasoning or Process Logic

Use:
- pipeline/microtasks.md for active rationales
- pipeline/memories.md for rejected approaches or architecture changes
- pipeline/learning_by_doing.md for workflow/process lessons

---

## Naming Conventions

- Files must use `snake_case`
- Functions must use **action_noun** pattern, e.g., `load_csv`, `parse_metadata`, `validate_schema`
- File names must reflect purpose (e.g., `clean_data.py` not `utils.py`)
- No generic names like `helper.py`, `common.py`, `functions.py`