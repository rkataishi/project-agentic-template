# Pipeline iterativo TOFA-WDF + Task Master (versión integral, jerárquica y estructurada)

╭────────────────────────────────────────────╮  
│  1. DEFINICIÓN DE LA TAREA                 │  
╰────────────────────────────────────────────╯  
• Redactar el PRD inicial como documento técnico orientado a funciones  
  (crear archivo: docs/mi_tarea/prd.md)  
• Registrar la tarea principal en Task Master  
  (task prd "Descripción clara y concreta de la tarea")  

↓  

╭────────────────────────────────────────────╮  
│  2. PARSEO Y PLANIFICACIÓN                 │  
╰────────────────────────────────────────────╯  
• Generar una primera expansión automática de subtasks  
  (task parse_prd)  
• Revisar y refinar subtasks: dividir, agrupar, priorizar, validar dependencias  
  (documentar cambios en: docs/mi_tarea/task-prd-revision.md)  
• Asignar prioridad por tarea  
  (task set_priority --task "X" --level high)  
• Declarar dependencias explícitas si existen  
  (task add_dependency --task "Y" --depends-on "X")  
• Especificar criterios objetivos de cierre por subtask  
  (crear archivo: docs/mi_tarea/criterios_cierre.md)  

↓  

╭────────────────────────────────────────────╮  
│  3. CICLO DE DESARROLLO ITERATIVO          │  
╰────────────────────────────────────────────╯  

╭──→ [A] IMPLEMENTACIÓN DE FUNCIONES SIMPLES  
│ • Diseñar cada función con una única responsabilidad  
│ • Inmediatamente después, crear su test unitario asociado  
│   (escribir test en test/test_<función>.py y validarlo con pytest)  
│ • Testear cada función en aislamiento antes de integrarla al flujo  

╰──→ [B] COMPOSICIÓN DEL FLUJO FUNCIONAL  
  • Implementar la función orquestadora que encadena funciones simples  
  • Verificar condiciones de entrada y salida con asserts internos  
  • No usar lógica de negocio en scripts  

↓  

╭──→ [C] CONSTRUCCIÓN Y PRUEBA DEL SCRIPT  
│ • Crear script lanzador que use el flujo  
│ • Ejecutar con dataset de prueba mínima  
│ • Analizar logs, salidas, errores y comportamiento  
│ • Marcar como “in progress” si se ejecuta parcialmente  
│   (task set_task_status --task "X" --status in-progress)  
│ • Si hay fallos: generar nuevas subtasks específicas para debugging o refactor  
│   (task add_task "Agregar control sobre filas vacías")  

╰──→ [D] REVISIÓN ASISTIDA POR LLM  
  • Consultar ambigüedades funcionales, proponer refactor o reestructuración  
  • Si la lógica de la tarea cambia, actualizar:  
    docs/mi_tarea/prd.md  
    docs/mi_tarea/task-prd-revision.md  

↓  

╭──→ [E] RE-EJECUCIÓN Y VALIDACIÓN PARCIAL  
│ • Ejecutar nuevamente con entradas controladas  
│ • Verificar logs, salidas esperadas y condiciones definidas en criterios_cierre.md  
│ • Si falla, volver a [A] o [B] según el tipo de error  
│  
╰──→ (Este ciclo puede repetirse múltiples veces por tarea)

↓  

╭────────────────────────────────────────────╮  
│  4. VALIDACIÓN FINAL Y ESTADO TESTING      │  
╰────────────────────────────────────────────╯  
• Ejecutar el script completo con datos representativos o reales  
• Validar outputs, comportamiento y registros frente a criterios definidos  
• Si se cumplen todos los requisitos:  
  (task set_task_status --task "X" --status testing)

↓  

╭────────────────────────────────────────────╮  
│  5. CIERRE Y DOCUMENTACIÓN DE LA TAREA     │  
╰────────────────────────────────────────────╯  
• Marcar como finalizada cuando esté validado y reproducible  
  (task set_task_status --task "X" --status done)  
• Registrar versión final, decisiones clave y estructura de entrada/salida  
  (agregar sección en README o update_task)  
• Archivar test_data usado y outputs relevantes para trazabilidad  

---

 Observaciones estructurales:

• Toda función simple debe nacer con su test unitario asociado (test-first discipline)  
• El parseo del PRD genera hipótesis; los errores deben inducir nuevas tareas formalmente  
• Cada modificación estructural del flujo o de la lógica debe actualizar el PRD y dejar rastro documental  
• El LLM puede asistir en composición, debugging, refactor y diseño de tests, pero no define el estado `done`  
• La documentación (`task-prd-revision.md`, `criterios_cierre.md`, `README`) es parte obligatoria del proceso técnico  