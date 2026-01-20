import os
import platform
import subprocess

def ping(host):
    """
    Retorna True se o host (str) responder a uma solicitação de ping.
    Lembre-se de que um host pode não responder a uma solicitação de ping (ICMP) mesmo se o nome do host for válido.
    """
    # Opção para o número de pacotes como função do sistema operacional
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Construindo o comando. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

if __name__ == '__main__':
    target_host = "8.8.8.8"
    print(f"Verificando conectividade com {target_host}...")
    if ping(target_host):
        print("A Rede está Ativa")
    else:
        print("A Rede está Inativa")
