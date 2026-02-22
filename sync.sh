#!/bin/bash
echo "🔄 Sincronizando MetaForge v5 con GitHub..."
git add .
read -p "Mensaje del cambio: " msg
git commit -m "$msg"
git push
echo "✅ Repositorio actualizado."
