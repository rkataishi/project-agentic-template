task-master help
Usage: task-master [options] [command]

Claude Task Master CLI

Options:
  -V, --version                    output the version number
  -h, --help                       Display help information

Commands:
  dev                              Run the dev.js script
  parse-prd [options]              Parse a PRD file and generate tasks
  update [options]                 Update multiple tasks with ID >= "from" based on new
                                   information or implementation changes
  update-task [options]            Update a single specific task by ID with new information (use
                                   --id parameter)
  update-subtask [options]         Update a subtask by appending additional timestamped
                                   information
  generate [options]               Generate task files from tasks.json
  set-status [options]             Set the status of a task
  list [options]                   List all tasks
  expand [options]                 Expand a task into subtasks using AI
  analyze-complexity [options]     Analyze tasks and generate expansion recommendations
  research [options]               Perform AI-powered research queries with project context
  clear-subtasks [options]         Clear subtasks from specified tasks
  add-task [options]               Add a new task using AI, optionally providing manual details
  next [options]                   Show the next task to work on based on dependencies and status
  show [options]                   Display detailed information about one or more tasks
  add-dependency [options]         Add a dependency to a task
  remove-dependency [options]      Remove a dependency from a task
  validate-dependencies [options]  Identify invalid dependencies without fixing them
  fix-dependencies [options]       Fix invalid dependencies automatically
  complexity-report [options]      Display the complexity analysis report
  add-subtask [options]            Add a subtask to an existing task
  remove-subtask [options]         Remove a subtask from its parent task
  remove-task [options]            Remove one or more tasks or subtasks permanently
  init [options]                   Initialize a new project with Task Master structure
  models [options]                 Manage AI model configurations
  lang [options]                   Manage response language settings
  move [options]                   Move a task or subtask to a new position
  rules [options]                  Add or remove rules for one or more profiles. Valid actions:
                                   add, remove (e.g., task-master rules add windsurf roo)
  migrate [options]                Migrate existing project to use the new .taskmaster directory
                                   structure
  sync-readme [options]            Sync the current task list to README.md in the project root
  add-tag [options]                Create a new tag context for organizing tasks
  delete-tag [options]             Delete an existing tag and all its tasks
  tags [options]                   List all available tags with metadata
  use-tag [options]                Switch to a different tag context
  rename-tag [options]             Rename an existing tag
  copy-tag [options]               Copy an existing tag to create a new tag with the same tasks
  help [command]                   display help for command

╭─────────────────────╮
│                     │
│   Task Master CLI   │
│                     │
╰─────────────────────╯


╭─────────────────────────────────╮
│  Project Setup & Configuration  │
╰─────────────────────────────────╯
    init                      [--name=<name>]                          Initialize a new project with Task       
                              [--description=<desc>] [-y]              Master structure                         
    models                                                             View current AI model configuration and  
                                                                       available models                         
    models --setup                                                     Run interactive setup to configure AI    
                                                                       models                                   
    models --set-main         <model_id>                               Set the primary model for task           
                                                                       generation                               
    models                    <model_id>                               Set the model for research operations    
    --set-research                                                                                              
    models                    <model_id>                               Set the fallback model (optional)        
    --set-fallback                                                                                              


╭───────────────────╮
│  Task Generation  │
╰───────────────────╯
    parse-prd                 --input=<file.txt> [--num-tasks=10]      Generate tasks from a PRD document       
    generate                                                           Create individual task files from        
                                                                       tasks.json                               


╭───────────────────╮
│  Task Management  │
╰───────────────────╯
    list                      [--status=<status>]                      List all tasks with their status         
                              [--with-subtasks]                                                                 
    set-status                --id=<id> --status=<status>              Update task status (pending, done,       
                                                                       in-progress, review, deferred,           
                                                                       cancelled)                               
    sync-readme               [--with-subtasks]                        Export tasks to README.md with           
                              [--status=<status>]                      professional formatting                  
    update                    --from=<id> --prompt="<context>"         Update multiple tasks based on new       
                                                                       requirements                             
    update-task               --id=<id> --prompt="<context>"           Update a single specific task with new   
                                                                       information                              
    update-subtask            --id=<parentId.subtaskId>                Append additional information to a       
                              --prompt="<context>"                     subtask                                  
    add-task                  --prompt="<text>"                        Add a new task using AI                  
                              [--dependencies=<ids>]                                                            
                              [--priority=<priority>]                                                           
    remove-task               --id=<id> [-y]                           Permanently remove a task or subtask     


╭──────────────────────╮
│  Subtask Management  │
╰──────────────────────╯
    add-subtask               --parent=<id> --title="<title>"          Add a new subtask to a parent task       
                              [--description="<desc>"]                                                          
    add-subtask               --parent=<id> --task-id=<id>             Convert an existing task into a subtask  
    remove-subtask            --id=<parentId.subtaskId>                Remove a subtask (optionally convert to  
                              [--convert]                              standalone task)                         
    clear-subtasks            --id=<id>                                Remove all subtasks from specified tasks 
    clear-subtasks --all                                               Remove subtasks from all tasks           


╭─────────────────────────────╮
│  Task Analysis & Breakdown  │
╰─────────────────────────────╯
    analyze-complexity        [--research] [--threshold=5]             Analyze tasks and generate expansion     
                                                                       recommendations                          
    complexity-report         [--file=<path>]                          Display the complexity analysis report   
    expand                    --id=<id> [--num=5] [--research]         Break down tasks into detailed subtasks  
                              [--prompt="<context>"]                                                            
    expand --all              [--force] [--research]                   Expand all pending tasks with subtasks   
    research                  "<prompt>" [-i=<task_ids>]               Perform AI-powered research queries with 
                              [-f=<file_paths>] [-c="<context>"]       project context                          
                              [--tree] [-s=<save_file>]                                                         
                              [-d=<detail_level>]                                                               


╭─────────────────────────────╮
│  Task Navigation & Viewing  │
╰─────────────────────────────╯
    next                                                               Show the next task to work on based on   
                                                                       dependencies                             
    show                      <id>                                     Display detailed information about a     
                                                                       specific task                            


╭──────────────────╮
│  Tag Management  │
╰──────────────────╯
    tags                      [--show-metadata]                        List all available tags with task counts 
    add-tag                   <tagName> [--copy-from-current]          Create a new tag context for organizing  
                              [--copy-from=<tag>] [-d="<desc>"]        tasks                                    
    use-tag                   <tagName>                                Switch to a different tag context        
    delete-tag                <tagName> [--yes]                        Delete an existing tag and all its tasks 
    rename-tag                <oldName> <newName>                      Rename an existing tag                   
    copy-tag                  <sourceName> <targetName>                Copy an existing tag to create a new tag 
                              [-d="<desc>"]                            with the same tasks                      


╭─────────────────────────╮
│  Dependency Management  │
╰─────────────────────────╯
    add-dependency            --id=<id> --depends-on=<id>              Add a dependency to a task               
    remove-dependency         --id=<id> --depends-on=<id>              Remove a dependency from a task          
    validate-dependenci…                                               Identify invalid dependencies without    
                                                                       fixing them                              
    fix-dependencies                                                   Fix invalid dependencies automatically   


╭─────────────────╮
│  Configuration  │
╰─────────────────╯
    .taskmaster/config.json        AI model configuration file (project root)         Managed by models cmd     
    API Keys (.env)                API keys for AI providers (ANTHROPIC_API_KEY,      Required in .env file     
                                   etc.)                                                                        
    MCP Keys (mcp.json)            API keys for Cursor integration                    Required in .cursor/      


╭───────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                       │
│   Quick Start:                                                                        │
│                                                                                       │
│   1. Create Project: task-master init                                                 │
│   2. Setup Models: task-master models --setup                                         │
│   3. Parse PRD: task-master parse-prd --input=<prd-file>                              │
│   4. List Tasks: task-master list                                                     │
│   5. Find Next Task: task-master next                                                 │
│                                                                                       │
╰───────────────────────────────────────────────────────────────────────────────────────╯

╭─────────────────────╮
│                     │
│   Task Master CLI   │
│                     │
╰─────────────────────╯


╭─────────────────────────────────╮
│  Project Setup & Configuration  │
╰─────────────────────────────────╯
    init                      [--name=<name>]                          Initialize a new project with Task       
                              [--description=<desc>] [-y]              Master structure                         
    models                                                             View current AI model configuration and  
                                                                       available models                         
    models --setup                                                     Run interactive setup to configure AI    
                                                                       models                                   
    models --set-main         <model_id>                               Set the primary model for task           
                                                                       generation                               
    models                    <model_id>                               Set the model for research operations    
    --set-research                                                                                              
    models                    <model_id>                               Set the fallback model (optional)        
    --set-fallback                                                                                              


╭───────────────────╮
│  Task Generation  │
╰───────────────────╯
    parse-prd                 --input=<file.txt> [--num-tasks=10]      Generate tasks from a PRD document       
    generate                                                           Create individual task files from        
                                                                       tasks.json                               


╭───────────────────╮
│  Task Management  │
╰───────────────────╯
    list                      [--status=<status>]                      List all tasks with their status         
                              [--with-subtasks]                                                                 
    set-status                --id=<id> --status=<status>              Update task status (pending, done,       
                                                                       in-progress, review, deferred,           
                                                                       cancelled)                               
    sync-readme               [--with-subtasks]                        Export tasks to README.md with           
                              [--status=<status>]                      professional formatting                  
    update                    --from=<id> --prompt="<context>"         Update multiple tasks based on new       
                                                                       requirements                             
    update-task               --id=<id> --prompt="<context>"           Update a single specific task with new   
                                                                       information                              
    update-subtask            --id=<parentId.subtaskId>                Append additional information to a       
                              --prompt="<context>"                     subtask                                  
    add-task                  --prompt="<text>"                        Add a new task using AI                  
                              [--dependencies=<ids>]                                                            
                              [--priority=<priority>]                                                           
    remove-task               --id=<id> [-y]                           Permanently remove a task or subtask     


╭──────────────────────╮
│  Subtask Management  │
╰──────────────────────╯
    add-subtask               --parent=<id> --title="<title>"          Add a new subtask to a parent task       
                              [--description="<desc>"]                                                          
    add-subtask               --parent=<id> --task-id=<id>             Convert an existing task into a subtask  
    remove-subtask            --id=<parentId.subtaskId>                Remove a subtask (optionally convert to  
                              [--convert]                              standalone task)                         
    clear-subtasks            --id=<id>                                Remove all subtasks from specified tasks 
    clear-subtasks --all                                               Remove subtasks from all tasks           


╭─────────────────────────────╮
│  Task Analysis & Breakdown  │
╰─────────────────────────────╯
    analyze-complexity        [--research] [--threshold=5]             Analyze tasks and generate expansion     
                                                                       recommendations                          
    complexity-report         [--file=<path>]                          Display the complexity analysis report   
    expand                    --id=<id> [--num=5] [--research]         Break down tasks into detailed subtasks  
                              [--prompt="<context>"]                                                            
    expand --all              [--force] [--research]                   Expand all pending tasks with subtasks   
    research                  "<prompt>" [-i=<task_ids>]               Perform AI-powered research queries with 
                              [-f=<file_paths>] [-c="<context>"]       project context                          
                              [--tree] [-s=<save_file>]                                                         
                              [-d=<detail_level>]                                                               


╭─────────────────────────────╮
│  Task Navigation & Viewing  │
╰─────────────────────────────╯
    next                                                               Show the next task to work on based on   
                                                                       dependencies                             
    show                      <id>                                     Display detailed information about a     
                                                                       specific task                            


╭──────────────────╮
│  Tag Management  │
╰──────────────────╯
    tags                      [--show-metadata]                        List all available tags with task counts 
    add-tag                   <tagName> [--copy-from-current]          Create a new tag context for organizing  
                              [--copy-from=<tag>] [-d="<desc>"]        tasks                                    
    use-tag                   <tagName>                                Switch to a different tag context        
    delete-tag                <tagName> [--yes]                        Delete an existing tag and all its tasks 
    rename-tag                <oldName> <newName>                      Rename an existing tag                   
    copy-tag                  <sourceName> <targetName>                Copy an existing tag to create a new tag 
                              [-d="<desc>"]                            with the same tasks                      


╭─────────────────────────╮
│  Dependency Management  │
╰─────────────────────────╯
    add-dependency            --id=<id> --depends-on=<id>              Add a dependency to a task               
    remove-dependency         --id=<id> --depends-on=<id>              Remove a dependency from a task          
    validate-dependenci…                                               Identify invalid dependencies without    
                                                                       fixing them                              
    fix-dependencies                                                   Fix invalid dependencies automatically   


╭─────────────────╮
│  Configuration  │
╰─────────────────╯
    .taskmaster/config.json        AI model configuration file (project root)         Managed by models cmd     
    API Keys (.env)                API keys for AI providers (ANTHROPIC_API_KEY,      Required in .env file     
                                   etc.)                                                                        
    MCP Keys (mcp.json)            API keys for Cursor integration                    Required in .cursor/      


╭───────────────────────────────────────────────────────────────────────────────────────╮
│                                                                                       │
│   Quick Start:                                                                        │
│                                                                                       │
│   1. Create Project: task-master init                                                 │
│   2. Setup Models: task-master models --setup                                         │
│   3. Parse PRD: task-master parse-prd --input=<prd-file>                              │
│   4. List Tasks: task-master list                                                     │
│   5. Find Next Task: task-master next                                                 │
│                                                                           