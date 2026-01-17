# Playground de Fundamentos de CS

Este diretório contém minhas soluções para desafios fundamentais de Ciência da Computação. O foco aqui não é apenas "fazer funcionar", mas entender profundamente como a memória e os algoritmos operam.

## Exercícios

### 1. Inverter uma Lista Encadeada (`ex1.py`)
**Tópico:** Estruturas de Dados (Linked Lists), Ponteiros e Referências.

**Objetivo:** Dada a cabeça (head) de uma lista encadeada simples, inverter a ordem dos nós de forma iterativa e retornar a nova cabeça.

#### O que este código ensina?

Este exercício simples é uma aula completa sobre quatro pilares da computação:

1.  **Manipulação de Ponteiros vs Valores**
    *   Em Python, variáveis como `curr` e `prev` são referências (ponteiros). Ao fazer `curr.next = prev`, não estamos movendo o valor dos dados, mas sim alterando para onde a "seta" aponta na memória. Estamos "recabeando" a estrutura.

2.  **A Importância da Ordem de Execução**
    *   A linha `next_temp = curr.next` é crítica. Se tentássemos inverter o ponteiro (`curr.next = prev`) *antes* de salvar quem é o próximo, perderíamos o acesso ao restante da lista para sempre (memory leak em outras linguagens). Isso ensina a planejar a sequência de operações para não perder dados.

3.  **Algoritmos "In-Place" (Eficiência de Espaço)**
    *   A inversão ocorre reaproveitando os nós existentes. Não criamos uma `nova_lista = []`.
    *   Isso resulta em **Complexidade de Espaço $O(1)$** (constante), pois usamos apenas 3 variáveis auxiliares, não importa se a lista tem 10 ou 1 milhão de itens.

4.  **Estruturas Lineares sem Acesso Aleatório**
    *   Diferente de Arrays onde acessamos `arr[5]` instantaneamente ($O(1)$), numa Linked List somos "cegos". Só conhecemos o vizinho imediato. Para inverter, somos obrigados a visitar todos os nós.
    *   Isso resulta em **Complexidade de Tempo $O(n)$**.

#### Como rodar
```bash
python ex1.py
```
