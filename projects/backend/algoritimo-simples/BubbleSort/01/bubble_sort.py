

def bubble_sort(arr): # Define a função bubble_sort e recebe uma lista como parâmetro
    """
   Desembaralha uma lista usando o algoritmo Bubble Sort.

    Args:
        arr (list): Lista de números a serem ordenados.
    """
    n = len(arr) # Obtém o tamanho da lista

    # Visita cada elemento na lista
    for i in range(n):
        # Uma flag para verificar se houve troca durante a passagem. Se não houver troca, significa que a lista já está ordenada.
        swapped = False 

        # Último i elementos já estão no lugar correto, não é necessário verificar novamente
        for j in range(0, n - i - 1):
            # Atravessa a lista e compara o elemento atual com o próximo elemento
            # Se o elemento atual for maior que o próximo, eles são trocados
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] # Troca os elementos
                swapped = True # Marca que houve uma troca

        # Se não houve troca, a lista já está ordenada e podemos sair do loop
        if not swapped:
            break

if __name__ == "__main__": # Bloco de execução principal
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted list: {my_list}") # Lista não ordenada
    bubble_sort(my_list) # Chama a função de ordenação
    print(f"Sorted list: {my_list}") # Lista ordenada
