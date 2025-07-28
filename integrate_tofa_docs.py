# compile_all_tofa_docs.py

import os
import subprocess

# Rutas específicas a incluir, relativas a docs/
doc_root = "."
external_dirs = [
    "../.github/instructions",
    "../.taskmaster"
]

all_dirs = [doc_root] + external_dirs
output_file = ".all_tofa.md"
output_lines = []

# Encabezado general
output_lines.append("# TOFA-WDF DOCUMENTATION CONSOLIDATED\n")
output_lines.append("Este documento fue generado automáticamente con todos los archivos relevantes del ciclo TOFA-WDF.\n")

# Árbol limitado a las carpetas relevantes
output_lines.append("## Árbol de directorios incluidos\n")
output_lines.append("```")
for path in all_dirs:
    output_lines.append(f"# {os.path.normpath(path)}")
    try:
        tree_output = subprocess.check_output(["tree", "-a", "-I", "__pycache__|.DS_Store|*.pyc|_*", "-L", "5", path], encoding="utf-8")
        output_lines.append(tree_output.strip())
    except Exception as e:
        output_lines.append(f"[ERROR] No se pudo generar tree para {path}: {e}")
output_lines.append("```\n")

# Compilación de documentos
output_lines.append("## Documentación consolidada\n")

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
            rel_path = os.path.relpath(file_path, start=doc_root)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                output_lines.append("\n" + "=" * 120)
                output_lines.append(f"\n## FILE: `{rel_path}`\n")
                output_lines.append("```markdown")
                output_lines.append(content.strip())
                output_lines.append("```")
            except Exception as e:
                output_lines.append("\n" + "=" * 120)
                output_lines.append(f"\n## ERROR: Could not read {rel_path} - {str(e)}\n")

# Escritura final
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(output_lines))