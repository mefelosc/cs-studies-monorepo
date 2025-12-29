from typing import List, TypeVar

T = TypeVar('T')  # Permite definir un tipo genérico


def merge_sort(arr: List[T]) -> List[T]:
    """
    Descifra uma lista usando o algoritmo Merge Sort.

    """
    if len(arr) <= 1: # Se a lista tem 0 ou 1 elemento, já está ordenada
        return arr

    mid = len(arr) // 2 # Encontra o ponto médio da lista
    left_half = arr[:mid] # Divide a lista em duas metades
    right_half = arr[mid:]

    sorted_left_half = merge_sort(left_half) # Ordena recursivamente cada metade
    sorted_right_half = merge_sort(right_half) 

    return merge(sorted_left_half, sorted_right_half) # Mescla as duas metades ordenadas

def merge(left: List[T], right: List[T]) -> List[T]: # Função auxiliar para mesclar duas listas ordenadas

    merged = [] # Lista para armazenar o resultado da mesclagem
    left_idx, right_idx = 0, 0 # Índices para rastrear a posição atual em cada lista

    while left_idx < len(left) and right_idx < len(right): # Enquanto houver elementos em ambas as listas
        if left[left_idx] < right[right_idx]: # Compara os elementos atuais de ambas as listas
            merged.append(left[left_idx]) # Adiciona o menor elemento à lista mesclada
            left_idx += 1 # Move o índice da lista esquerda para a frente
        else: # Se o elemento da lista direita for menor ou igual
            merged.append(right[right_idx]) # Adiciona o elemento da lista direita à lista mesclada
            right_idx += 1 # Move o índice da lista direita para a frente

    # Adiciona quaisquer elementos restantes de ambas as listas
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:]) #

    return merged # Retorna a lista mesclada e ordenada

if __name__ == "__main__":
    my_list = [38, 27, 43, 3, 9, 82, 10]
    print("Original list:", my_list) 
    sorted_list = merge_sort(my_list) # Ordena a lista usando Merge Sort
    print("Sorted list:", sorted_list) #
    
