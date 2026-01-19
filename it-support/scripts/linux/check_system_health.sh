#!/bin/bash
# check_system_health.sh
# Script para verificar a saúde básica do sistema Linux (Disco, Memória, CPU)

echo "=== Verificação de Saúde do Sistema ==="
date
echo ""

# 1. Verificar uso de disco
echo "--- Uso de Disco ---"
df -h | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $5 " " $1 }' | while read output;
do
  usep=$(echo $output | awk '{ print $1}' | cut -d'%' -f1 )
  partition=$(echo $output | awk '{ print $2 }' )
  if [ $usep -ge 90 ]; then
    echo "CRÍTICO: Partição $partition está com $usep% de uso!"
  elif [ $usep -ge 70 ]; then
    echo "ALERTA: Partição $partition está com $usep% de uso."
  else
    echo "OK: Partição $partition está com $usep% de uso."
  fi
done
echo ""

# 2. Verificar Memória RAM
echo "--- Uso de Memória ---"
free -h
echo ""

# 3. Verificar Uptime e Load Average
echo "--- Uptime e Load ---"
uptime
echo ""

echo "=== Fim da Verificação ==="
