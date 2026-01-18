#!/bin/bash

# Port Scanner Simples em Bash
# Uso: ./port_scanner.sh <IP>

target=$1

# Lista de portas comuns para verificar
ports=(21 22 23 25 53 80 443 3306 8080)

if [ -z "$target" ]; then
    echo "Uso: $0 <endereço IP>"
    echo "Exemplo: $0 127.0.0.1"
    exit 1
fi

echo "Iniciando scan em $target..."
echo "Verificando portas: ${ports[*]}"

for port in "${ports[@]}"; do
    # Tenta conectar na porta usando /dev/tcp (feature do bash)
    # timeout 1 define um tempo limite de 1 segundo
    # 2>/dev/null silencia erros
    timeout 1 bash -c "echo >/dev/tcp/$target/$port" 2>/dev/null && \
        echo "[+] Porta $port está ABERTA" || \
        echo "[-] Porta $port está FECHADA"
done
