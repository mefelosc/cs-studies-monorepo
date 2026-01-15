# Exemplos de Scripts Bash

Aqui estão alguns exemplos de scripts Bash para você praticar. Lembre-se sempre de dar permissão de execução com `chmod +x nome_do_arquivo.sh` antes de rodar.

## 1. Variáveis e Input do Usuário
Este script pergunta o nome e idade e imprime na tela.

```bash
#!/bin/bash

echo "Qual é o seu nome?"
read nome
echo "Quantos anos você tem?"
read idade

echo "Olá, $nome! Você tem $idade anos."
```

## 2. Condicionais (If/Else)
Verifica se um número é maior que 10.

```bash
#!/bin/bash

echo "Digite um número:"
read numero

if [ $numero -gt 10 ]; then
    echo "O número $numero é maior que 10."
else
    echo "O número $numero é menor ou igual a 10."
fi
```

## 3. Loops (For)
Conta de 1 até 5.

```bash
#!/bin/bash

echo "Contando até 5..."
for i in {1..5}
do
   echo "Número: $i"
done
```

## 4. Verificar se um Arquivo Existe
Útil para scripts de sistemas.

```bash
#!/bin/bash

ARQUIVO="teste.txt"

if [ -f "$ARQUIVO" ]; then
    echo "O arquivo $ARQUIVO existe."
else
    echo "O arquivo $ARQUIVO não existe. Criando agora..."
    touch $ARQUIVO
    echo "Arquivo criado com sucesso!"
fi
```

## 5. Ping Simples (Verificar Conexão)
Verifica se o Google está respondendo.

```bash
#!/bin/bash

SITE="google.com"

echo "Pingando $SITE..."
ping -c 3 $SITE

if [ $? -eq 0 ]; then
    echo "Sucesso! $SITE está online."
else
    echo "Falha ao conectar com $SITE."
fi
```
