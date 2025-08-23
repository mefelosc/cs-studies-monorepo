def fatorial_recursivo(n: int) -> int:
    """
    Calcula o fatorial de n usando recursão padrão.
    Esta função é mais clara e idiomática em Python.
    """
    # Caso base: fatorial de 0 ou 1 é 1.
    if n <= 1:
        return 1
    # Passo recursivo: n * fatorial(n-1).
    # A multiplicação ocorre APÓS o retorno da chamada recursiva.
    else:
        return n * fatorial_recursivo(n - 1)

def main():
    """Função principal que gerencia a entrada do usuário e a saída do programa."""
    try:
        numero = int(input("Digite um número inteiro: "))

        if numero < 0:
            print("Número inválido. Fatorial não é definido para números negativos.")
        else:
            resultado = fatorial_recursivo(numero)
            print(f"O fatorial de {numero} é {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    # Este bloco garante que a função main() só execute quando o script é rodado diretamente.
    main()