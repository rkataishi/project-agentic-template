# Cross-Task Coordination (TOFA-WDF)

## Strategy

- Use `flows/` as the only place where multiple tasks meet
- Never call a task-local orchestrator from another task

## Allowed Data Sharing

- Use `shared_modules/` for utilities reused across tasks
- Use `flows/` to coordinate outputs from multiple task orchestrators
- Pass outputs explicitly from one flow step to another, never via shared state

## Example Pattern

```python
# inside flows/integration_flow.py

from tasks.data_processing.functions.orchestrators.cleaning_pipeline import run_cleaning
from tasks.analysis.functions.orchestrators.analysis_pipeline import run_analysis

def integration_flow():
    clean_df = run_cleaning("data.csv")
    result = run_analysis(clean_df)
    ...