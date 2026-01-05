import hashlib

# 1. Escolha uma palavra
texto = "senha123"

# 2. Gere a "impressão digital" (Hash) usando o algoritmo SHA-256
# O .encode() transforma o texto em bytes para o computador
hash_resultado = hashlib.sha256(texto.encode()).hexdigest()

print(f"Texto: {texto}")
print(f"Hash:  {hash_resultado}")