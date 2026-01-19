# IT Support Automation Scripts

Este diretório contém scripts de exemplo para automação de tarefas comuns de suporte de TI em Linux (Bash) e Windows (PowerShell/Batch).

## Estrutura

- `linux/`: Scripts Bash para ambientes Linux.
- `windows/`: Scripts PowerShell e Batch para ambientes Windows.

## Melhores Práticas de Automação

1. **Idempotência**: Scripts devem produzir o mesmo resultado independentemente de quantas vezes forem executados.
2. **Logs**: Sempre registre a saída ou erros importantes.
3. **Tratamento de Erros**: Verifique se os comandos foram bem-sucedidos antes de prosseguir.
4. **Comentários**: Documente o que o script faz, especialmente para fins de estudo.
