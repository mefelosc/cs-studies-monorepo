#!/bin/bash
# batch_rename_files.sh
# Script para renomear arquivos em massa adicionando um prefixo ou sufixo.
# Uso: ./batch_rename_files.sh [diretório] [prefixo]
# Exemplo: ./batch_rename_files.sh ./fotos "ferias_2023_"

DIR="${1:-.}"
PREFIX="${2:-renamed_}"

if [ ! -d "$DIR" ]; then
  echo "Erro: Diretório $DIR não encontrado."
  exit 1
fi

echo "Renomeando arquivos em '$DIR' com prefixo '$PREFIX'..."
count=0

# Loop pelos arquivos
for file in "$DIR"/*; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")
    new_name="${DIR}/${PREFIX}${filename}"
    
    mv "$file" "$new_name"
    echo "Renomeado: $filename -> ${PREFIX}${filename}"
    ((count++))
  fi
done

echo "Concluído! $count arquivos renomeados."
