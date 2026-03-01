#!/bin/bash
# ============================================================================
# AUTHOR_IDENTITY_BLOCK [ROOT_ACCESS_ONLY]
# ============================================================================
# IDENTIFIER:  Salvador Ferrer
# PROJECT:     METAFORGE_v5 (Community Tools Registry)
# BOOK_REF:    "CÓMO CONSTRUIR AGENTES DE IA QUE NO ALUCINAN"
# STATUS:      COMMUNITY_GATEWAY_ACTIVE
# ============================================================================
# METAFORGE v5 - Sincronizador de Repositorio

set -e # Detiene la ejecución si ocurre un error

echo "----------------------------------------------------"
echo "🔄 METAFORGE v5: Iniciando Sincronización Industrial"
echo "----------------------------------------------------"

# Verificar si estamos en un repositorio git
if [ ! -d .git ]; then
    echo "❌ Error: No se detecta un repositorio Git en este directorio."
    exit 1
fi

# Proceso de commit
git add .
read -p "📝 Introduzca identificador de cambio (Commit Message): " msg

if [ -z "$msg" ]; then
    msg="Update Metaforge Assets: $(date +'%Y-%m-%d %H:%M')"
fi

git commit -m "$msg"

echo "🚀 Desplegando cambios al repositorio remoto..."
git push

echo "----------------------------------------------------"
echo "✅ Sincronización completada con éxito."
echo "----------------------------------------------------"
