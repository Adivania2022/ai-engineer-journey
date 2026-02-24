
resultado = 0
for i in range(3):
    numero_soma = float(input("Digite um numero: "))
    resultado += numero_soma
    print(f' A soma dos numeros é {resultado}.')


frase = input("Informe uma frase: ").lower()
letras = set()

for letra in frase:
    if letra.isalpha():
         letras.add(letra)

# O teste deve ser feito APENAS DEPOIS de o ciclo terminar
if len(letras) >= 23:
    print("A frase é um pangrama.")
else:
    print("A frase não é um pangrama.")

expressao = input("Digite uma expressão matemática: ")
pilha = []

for char in expressao:
    if char == "(":
        pilha.append(char)
    elif char == ")":
        if len(pilha) == 0:
            pilha.append(char)  # Adiciona para a pilha não ficar vazia
            break               # Interrompe pois já deu erro
        else:
            pilha.pop()         # Remove o "(" correspondente

if len(pilha) == 0:
    print("Os parênteses estão balanceados.")
else:
    print("Os parênteses não estão balanceados.")

limite = int(input("Informe um número limite: "))

fibonacci = [] # Criamos uma lista vazia
anterior, atual = 0, 1

while anterior <= limite:
    fibonacci.append(anterior) # Adiciona o número ao final da lista
    # A "dança" das variáveis numa única linha (forma Pythonica):
    anterior, atual = atual, anterior + atual

print(f"A sequência de Fibonacci até {limite} é:")
print(fibonacci)

import random
numero_secreto = random.randint(1, 100) 
tentativas = 0
while True:
    tentativa = int(input("Digite um número entre 1 e 100: ")) 
    tentativas += 1
    if tentativa == numero_secreto:
        print(f"Parabéns, você adivinhou o número em {tentativas})tentativas.") 
        break
    elif tentativa < numero_secreto:
        print("O número a ser encontrado é maior.") 
    else:
        print("O número a ser encontrado é menor.")