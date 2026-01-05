import time

# Simulando um servidor que as vezes "cai"
def verificar_disponibilidade(servidor_nome):
    # Simulando um "Ping" (um pedido de 'oi' para o servidor)
    # Aqui vamos fingir que o servidor Google está sempre online
    # Mas poderíamos testar qualquer IP
    print(f"[*] Verificando {servidor_nome}...")
    
    # Em um cenário real, usaríamos a biblioteca 'requests' ou 'socket'
    # Vamos simular um status OK
    status = "ONLINE" 
    return status

# O Monitor de Disponibilidade
servidor = "Servidor-da-Empresa-XYZ"

print(f"--- Iniciando Monitor de Disponibilidade ---")

try:
    while True: # Loop infinito para monitorar sempre
        status = verificar_disponibilidade(servidor)
        
        if status == "ONLINE":
            print(f"[OK] {servidor} está funcionando normalmente.")
        else:
            print(f"[ALERTA!!!] {servidor} FICOU INDISPONÍVEL!")
            
        print("Pressione Ctrl+C para parar o monitor.")
        time.sleep(3) # Espera 3 segundos antes de verificar de novo
except KeyboardInterrupt:
    print("\nMonitor encerrado pelo usuário.")