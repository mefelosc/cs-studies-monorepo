# Linux Scripts & Security Studies

Este diretório é dedicado ao aprendizado e prática de **Shell Scripting (Bash)** no Linux.

O objetivo desta seção é entender como automatizar tarefas, interagir com o sistema operacional e realizar verificações básicas de segurança e rede através da linha de comando.

## Conteúdo

- **Conceitos Básicos**: Criação de arquivos, permissões (`chmod`), e execução.
- **Automação**: Scripts para verificar status de arquivos e serviços.
- **Rede**: Verificação de conectividade (ping, curl).
- **Segurança**: Ferramentas simples como port scanners para diagnósticos de rede.

## Scripts Disponíveis

### 1. `hello_linux.sh`
Script introdutório para testar o ambiente.

### 2. `ping-site.sh`
Verifica a conectividade com um site específico usando o comando `ping`.

### 3. `port_scanner.sh`
Um scanner de portas simples que verifica se portas comuns (como 80, 443, 22) estão abertas em um alvo. Utiliza a funcionalidade nativa `/dev/tcp` do Bash.
