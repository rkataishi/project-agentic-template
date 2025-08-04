#!/bin/bash

sudo tee /usr/local/bin/add_project_tofa > /dev/null <<EOF
#!/bin/bash

if [ \$# -lt 3 ]; then
  echo "Uso: add_project_tofa <repo_template> <nombre_proyecto> \"descripción\""
  exit 1
fi

TEMPLATE_REPO="\$1"
PROJECT_NAME="\$2"
DESCRIPTION="\$3"

PARENT_DIR="/Users/rho/Library/CloudStorage/Dropbox/Apps/Mis_Apps"
LINK_DIR="/Users/rho/Library/CloudStorage/Dropbox/= Working Now ="

mkdir -p "\$PARENT_DIR"
cd "\$PARENT_DIR" || exit 1

gh repo create "\$PROJECT_NAME" \
  --template "\$TEMPLATE_REPO" \
  --public \
  --description "\$DESCRIPTION" \
  --clone

ln -sfn "\$PARENT_DIR/\$PROJECT_NAME" "\$LINK_DIR/\$PROJECT_NAME"

echo "Proyecto '\$PROJECT_NAME' creado en:"
echo "- Carpeta: \$PARENT_DIR/\$PROJECT_NAME"
echo "- Enlace:  \$LINK_DIR/\$PROJECT_NAME"
EOF

sudo chmod +x /usr/local/bin/add_project_tofa
echo "Comando 'add_project_tofa' instalado en /usr/local/bin"

# ejemplo:
# add_project_tofa "repo" "proyecto" "descripcion"
# add_project_tofa rkataishi/project-agentic-template Googler "Agente que busca usando Playwright + browser-use"