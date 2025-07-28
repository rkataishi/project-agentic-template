#!/bin/bash
# v3 - Manejo robusto de conflictos y sincronización remota

sudo tee /usr/local/bin/upload_to_github > /dev/null <<EOF
#!/bin/bash

if [ \$# -lt 2 ]; then
  echo "Uso: upload_to_github <URL del repositorio> \"Mensaje de commit\""
  exit 1
fi

REPO_BASE_URL="\$1"
COMMIT_MSG="\$2"
REPO_URL="\${REPO_BASE_URL}.git"
REPO_NAME=\$(basename "\$REPO_BASE_URL")

echo "Repositorio: \$REPO_NAME"
echo "Commit: \$COMMIT_MSG"

if [ ! -d .git ]; then
  git init -b main
fi

git add --all
git commit -m "\$COMMIT_MSG"

if ! git remote | grep -q origin; then
  git remote add origin "\$REPO_URL"
fi

echo "Sincronizando con el remoto..."
git fetch origin
git pull origin main --allow-unrelated-histories --no-rebase

echo "Empujando los cambios..."
git push origin main

if [ \$? -ne 0 ]; then
  echo "❌ Falló el push. Requiere resolución manual."
  exit 1
fi

echo "Actualización completada correctamente."
EOF

sudo chmod +x /usr/local/bin/upload_to_github
echo "Comando 'upload_to_github' instalado en /usr/local/bin"