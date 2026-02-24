from random import sample

# 1. Sortear 5 números únicos entre 1 e 50
numeros = sample(range(1, 51), 5)

# 2. Sortear 2 estrelas únicas entre 1 e 12 (Regra atual)
estrelas = sample(range(1, 13), 2)

# Organizar em ordem crescente para ficar bonito
numeros.sort()
estrelas.sort()

print("--- CHAVE DO EUROMILHÕES ---")
print(f"Números: {numeros}")
print(f"Estrelas: {estrelas}")

