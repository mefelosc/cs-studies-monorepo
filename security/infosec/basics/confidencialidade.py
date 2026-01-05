# Uma função simples de XOR
def xor_cipher(texto, chave):
    resultado = ""
    for i in range(len(texto)):
        # Pega o caractere e faz o XOR (^) com a chave
        # O % garante que a chave se repita se for menor que o texto
        char_original = texto[i]
        char_chave = chave[i % len(chave)]
        
        # O símbolo ^ é o operador XOR em Python
        novo_char_num = ord(char_original) ^ ord(char_chave)
        resultado += chr(novo_char_num)
        
    return resultado

# 1. Nossa mensagem secreta e a CHAVE original definida no código
mensagem = "Ataque as 5h"
chave_original = "paz123"

# 2. Encriptar
secreto = xor_cipher(mensagem, chave_original)
print(f"Mensagem Trancada: {secreto}")

print("-" * 30)
# 3. PERGUNTAR a chave para o usuário
tentativa_chave = input("Digite a chave para descriptografar: ")

# 4. Tentar decriptar com o que o usuário digitou
original = xor_cipher(secreto, tentativa_chave)
print(f"Resultado da tentativa: {original}")