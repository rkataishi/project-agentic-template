# Optimal Practices for Python Technical Scripts with Task Master

Based on the analysis of your Python technical scripting workflow and the Task Master documentation, here are tailored best practices recommendations that reflect your feedback about organizing by tasks with clear script-function relationships.

## 1. Project Structure & Organization by Task

Organize your project around specific capabilities or tasks, where each directory contains both the scripts and their supporting functions. This structure clearly shows that functions are tools for scripts within a specific domain.

```
project-root/
├── data_processing/            # Capacidad: Procesamiento de datos
│   ├── scripts/                #   Scripts principales para esta capacidad
│   │   ├── process_csv.py      #   - Script principal para CSV
│   │   └── process_json.py     #   - Script principal para JSON
│   ├── functions/              #   Funciones auxiliares para esta capacidad
│   │   ├── simple/             #   - Funciones simples (una sola responsabilidad)
│   │   │   ├── validate.py     #     * Validación de datos
│   │   │   ├── transform.py    #     * Transformación de datos
│   │   │   └── clean.py        #     * Limpieza de datos
│   │   └── orchestrators/      #   - Funciones orquestadoras (lógica compleja)
│   │       └── workflow.py     #     * Coordinación de procesos
│   └── test_data/              #   Datos de prueba específicos para esta capacidad
│       ├── sample.csv          #   - Datos de ejemplo
│       └── invalid.csv         #   - Datos inválidos para pruebas
│
├── automation/                 # Capacidad: Automatización
│   ├── scripts/                #   Scripts principales para automatización
│   │   ├── backup.py           #   - Script de respaldo
│   │   └── cleanup.py          #   - Script de limpieza
│   ├── functions/              #   Funciones auxiliares para automatización
│   │   ├── simple/             #   - Funciones simples
│   │   │   ├── file_ops.py     #     * Operaciones con archivos
│   │   │   └── system.py       #     * Operaciones del sistema
│   │   └── orchestrators/      #   - Funciones orquestadoras
│   │       └── schedule.py     #     * Programación de tareas
│   └── test_data/              #   Datos de prueba para automatización
│
├── reporting/                  # Capacidad: Generación de reportes
│   ├── scripts/                #   Scripts principales para reportes
│   │   ├── generate.py         #   - Generación de reportes
│   │   └── export.py           #   - Exportación de datos
│   ├── functions/              #   Funciones auxiliares para reportes
│   │   ├── simple/             #   - Funciones simples
│   │   │   ├── format.py       #     * Formateo de datos
│   │   │   └── calculate.py    #     * Cálculos para reportes
│   │   └── orchestrators/      #   - Funciones orquestadoras
│   │       └── template.py     #     * Manejo de plantillas
│   └── test_data/              #   Datos de prueba para reportes
│
├── shared/                     # Componentes compartidos entre capacidades
│   ├── functions/              #   Funciones compartidas
│   │   ├── simple/             #   - Funciones simples compartidas
│   │   │   ├── logging.py      #     * Registro de eventos
│   │   │   └── config.py       #     * Gestión de configuración
│   │   └── orchestrators/      #   - Funciones orquestadoras compartidas
│   │       └── error.py        #     * Manejo de errores
│   └── utils.py                #   Utilidades generales
│
├── config/                     # Configuración general del proyecto
│   ├── app.json                #   - Configuración principal
│   └── logging.json            #   - Configuración de registro
│
├── logs/                       # Registros del sistema
└── docs/                       # Documentación
```

### Key Principles of This Structure:

1. **Task-Centric Organization**: Each top-level directory represents a specific capability or task domain
2. **Clear Tool-User Relationship**: Functions are organized as tools within the same directory as the scripts that use them
3. **Autonomous Units**: Each capability directory contains everything needed for that domain
4. **Scalability**: Easy to add new capabilities as independent directories
5. **Maintainability**: All related code is co-located

## 2. Function Design Philosophy

### Simple Functions
- **Single Responsibility**: Each function does one thing well
- **Single-Level Conditionals**: Only one level of if-else statements
- **Pure Functions**: When possible, avoid side effects
- **Small Scope**: Limited to specific domain within the capability
- **No Classes**: Prefer functions over classes unless absolutely necessary

### Orchestrator Functions
- **Coordination Role**: Combine simple functions to achieve complex outcomes
- **Complex Logic**: Handle multi-level conditionals and decision trees
- **Error Handling**: Manage exceptions from simple functions
- **Workflow Management**: Control execution flow
- **No Implementation**: Should not contain business logic implementation

## 3. Function Categorization and Naming

### Simple Function Categories

**Data Validation Functions**
- Purpose: Validate input data, return boolean
- Naming Pattern: `is_valid_<entity>_<property>` or `validate_<entity>_<property>`
- Examples: `is_valid_email`, `validate_age_range`, `has_required_keys`

**Data Transformation Functions**
- Purpose: Transform data from one format to another
- Naming Pattern: `convert_<from>_<to>` or `format_<entity>`
- Examples: `convert_date_format`, `format_currency`, `normalize_text`

**File Operations Functions**
- Purpose: Read, write, or manipulate files
- Naming Pattern: `read_<entity>`, `write_<entity>`, `process_<file_type>`
- Examples: `read_csv_file`, `write_json_output`, `backup_file`

**Calculation Functions**
- Purpose: Perform mathematical operations
- Naming Pattern: `calculate_<metric>` or `compute_<value>`
- Examples: `calculate_discount`, `compute_statistics`, `determine_tax_rate`

**String Operations Functions**
- Purpose: Manipulate strings
- Naming Pattern: `format_<purpose>`, `extract_<entity>`, `clean_<data_type>`
- Examples: `format_phone_number`, `extract_domain`, `clean_whitespace`

### Orchestrator Function Categories

**Processing Orchestrators**
- Purpose: Coordinate processing of specific entity types
- Naming Pattern: `process_<entity>` or `handle_<entity>_workflow`
- Examples: `process_customer_record`, `handle_order_workflow`

**Automation Orchestrators**
- Purpose: Coordinate multi-step automation tasks
- Naming Pattern: `execute_<process>_workflow` or `run_<automation>`
- Examples: `execute_data_import_workflow`, `run_daily_backup`

**Integration Orchestrators**
- Purpose: Coordinate interactions between systems
- Naming Pattern: `sync_<system1>_<system2>` or `integrate_<service>`
- Examples: `sync_crm_database`, `integrate_payment_gateway`

**Report Orchestrators**
- Purpose: Coordinate report generation
- Naming Pattern: `generate_<report_type>_report` or `create_<analysis>`
- Examples: `generate_monthly_sales_report`, `create_customer_analysis`

### Naming Conventions
- Use lowercase with underscores (snake_case)
- Be specific and descriptive
- Start with verb for action functions
- Start with "is_" or "has_" for predicate functions
- Use full words rather than abbreviations

## 4. File Organization by Task

### Directory Structure per Task

Each task directory follows the same pattern:

```
task-name/
├── scripts/                    # Main executable scripts
├── functions/                  # Supporting functions
│   ├── simple/                 # Simple functions (single responsibility)
│   └── orchestrators/          # Orchestrator functions (complex logic)
└── test_data/                  # Test data for this task
```

### Example: Data Processing Task

**Script Usage Pattern**:
```python
# data_processing/scripts/process_csv.py
from data_processing.functions.simple.validate import is_valid_csv_format
from data_processing.functions.simple.transform import convert_csv_to_dict
from data_processing.functions.orchestrators.workflow import process_data_batch

def main():
    # Use functions from the same task directory
    if is_valid_csv_format(input_file):
        data = convert_csv_to_dict(input_file)
        process_data_batch(data, config)
```

This structure makes it clear that:
- The script is the primary user
- The functions are tools that serve the script
- Everything is organized by task domain

### Shared Components

For functions used across multiple tasks, use the `shared/` directory:

```
shared/
├── functions/
│   ├── simple/
│   │   ├── logging.py
│   │   └── config.py
│   └── orchestrators/
│       └── error.py
└── utils.py
```

Import shared functions when needed:
```python
from shared.functions.simple.logging import setup_logging
from shared.functions.simple.config import load_config
```

## 5. Task Master Integration

Use Task Master to manage your script development lifecycle:

- **Project Setup**: Start with `initialize_project` to set up Task Master
- **Requirements**: Use `parse_prd` to convert script requirements into actionable tasks
- **Task Breakdown**: Break complex scripts into subtasks using `expand_task`
- **Prioritization**: Set appropriate priorities (high for critical automation, medium for data processing, low for utilities)
- **Dependencies**: Use `add_dependency` to sequence interdependent scripts
- **Progress Tracking**: Use `set_task_status` to track progress through 'pending', 'in-progress', 'testing', and 'done' states
- **Task Management**: Use `next_task` to identify what to work on next

## 6. Script Development Workflow

Follow a structured development process:

1. **Initialization**: Start with `initialize_project` to set up Task Master
2. **Requirements**: Create a PRD outlining script requirements
3. **Task Planning**: Use `parse_prd` to generate initial tasks
4. **Development**:
   - Create a task directory for the new capability
   - Implement simple functions first
   - Create orchestrator functions to coordinate them
   - Write scripts that use these functions
   - Test frequently with small data sets
5. **Testing**: Execute scripts with test data and verify terminal output
6. **Completion**: Mark tasks as complete with `set_task_status`

## 7. Error Handling & Logging

Implement robust error handling and logging:

- **Exception Handling**: Use specific exception types (ValueError, FileNotFoundError, etc.) rather than generic Exception
- **Graceful Degradation**: Handle errors gracefully with meaningful messages
- **Structured Logging**: Use the logging module with timestamps and severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- **Log Files**: Create dated log files in the `logs/` directory
- **Error Context**: Include relevant context in error messages (file names, line numbers, variable values)
- **Recovery Suggestions**: Provide actionable suggestions for resolving common errors
- **Exit Codes**: Use standard exit codes (0 for success, 1 for errors, 2 for usage errors)

## 8. Configuration Management

Manage configuration effectively:

- **Environment Variables**: Store environment-specific settings in `.env` files using python-dotenv
- **Configuration Validation**: Validate configuration at script startup
- **Fallback Values**: Implement sensible fallback values for optional parameters
- **Security**: Keep sensitive data (passwords, API keys) out of version control
- **Configuration Files**: Use JSON, YAML, or INI files for complex configurations
- **Command Line Overrides**: Allow command-line arguments to override configuration values

## 9. Testing & Validation

Implement comprehensive testing that aligns with your terminal-based verification approach:

### Terminal-Based Testing Workflow

**Immediate Feedback Loop**:
- Run scripts frequently during development to verify output
- Test after each significant change
- Use small data sets initially, then scale up

**Output Verification**:
- Check terminal output against expected results
- Verify exit codes (0 for success, non-zero for errors)
- Confirm file creation/modification when expected
- Validate data transformations with sample outputs

**Progressive Testing**:
1. Test with minimal data (1-2 records)
2. Test with typical data volume
3. Test with edge cases (empty files, malformed data)
4. Test with maximum expected data volume

### Testing Simple Functions
- Test each simple function in isolation
- Verify single-level conditional logic
- Test edge cases and error conditions
- Use simple test data

### Testing Orchestrator Functions
- Test workflow coordination
- Verify error handling and recovery
- Test different configuration scenarios
- Use realistic data sets

### Script Execution Testing Strategies

**Dry-Run Mode**:
- Implement a `--dry-run` flag that shows what would be done without making changes
- Example: "Would process 150 files" instead of actually processing them

**Verbose Output**:
- Use `--verbose` flag to show detailed processing steps
- Include progress indicators for long operations
- Show summary statistics at completion

**Interactive Mode**:
- For destructive operations, implement confirmation prompts
- Allow users to review actions before execution

**Exit Codes**:
- Use standard exit codes to indicate script status
- 0: Success
- 1: General error
- 2: Usage error
- 3+: Specific error types

## 10. Documentation Practices

Maintain comprehensive documentation:

- **Docstrings**: Include detailed docstrings with purpose, parameters, return values, and examples
- **Task Documentation**: Use `update_task` to keep task descriptions current
- **Dependencies**: Document script dependencies and requirements
- **README**: Maintain a README.md with usage examples, installation instructions, and troubleshooting tips
- **Inline Comments**: Use comments to explain complex logic
- **Change Log**: Track significant changes and updates

## 11. Code Reusability

Maximize code reuse:

- **Task-Specific Functions**: Keep functions close to the scripts that use them
- **Shared Functions**: Extract truly reusable functions to the `shared/` directory
- **Parameterization**: Use parameters to increase script flexibility
- **Command-Line Arguments**: Implement argument parsing with argparse
- **Configuration Files**: Use external configuration to avoid hardcoding

This structure optimizes your technical scripting workflow by organizing code around tasks, with a clear relationship between scripts (users) and functions (tools), while supporting your preference for simple functions with single-level conditionals and orchestrator functions for complex logic.