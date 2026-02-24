numero = int(input("Digite um numero: "))
if numero % 2 == 0:
    print(f"O numero {numero} é par.")
else:
    print(f"O numero {numero} é impar.")


idade = int(input("Digite a sua idade: "))
if idade >= 18:
    print("Parabéns já pode exercer o seu direito de voto.")
else:
    print(f"Você ainda não pode votar. Precisa aguardar mais {18-idade} anos.")

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))

if numero_1 > numero_2:
    print(f"O {numero_1} é maior que o {numero_2}.")
elif numero_2 > numero_1:
    print(f'O {numero_1} é menor que o {numero_2}.')
else:
    print("Os números são iguais.")

print("Os números da lista são: ")
for lista in range(2,101,2):
    print(lista)

for elementos in range(1,100):
    if elementos % 3 == 0 and elementos % 5 == 0:
        print("I LOVE YOU")
    elif elementos %3 ==0: 
        print("BABY") 
    elif elementos% 5 == 0:
        print("BUZZ")
    else:
        print(elementos)

tabuada = int(input("Digite um numero: "))
print(f"A tabuada de multiplicação de {tabuada} é:")
for i in range(1,11):
    print(f"{tabuada} X {i} é = { i * tabuada}")

palavra = input("Insira uma palavra: ")
if palavra == palavra[::-1]:
    print(f" A palavra {palavra} é um palindromo.")
else:
    print(f" A palavra {palavra} não é um palindromo.")

numero_int = int(input("Digite um numero inteiro: "))
primo = True
for i in range(2, int(numero_int ** 0.5) + 1):
    if numero_int % i == 0:
       primo = False
       break

if primo:
    print(" O número é primo.")
else:
    print(" O número não é primo.")


from math import factorial
fator = int(input("Digite um numero para calcularmos o seu fatorial: "))
resultado = factorial(fator)
print(resultado) 

 # Crie um programa que peça um tamanho e crie uma lista com esse tamanho, preenchendo-a com números informados pelo usuário.

lista_de_tam_calça = int(input("Digite o tamanho de sua calça: "))
lista_de_tam_blusa = int(input("Digite o tamanho de sua blusa: "))

print(f"\n\t[Calça]: O tamanho de sua calça é: {lista_de_tam_calça}.")
print(f"\n\t[Blusa]: O tamanho de sua blusa é: {lista_de_tam_blusa}.")

resultado_soma= 0
for i in range(10):
    soma_num = float(input(" Digite 10 numeros:  "))
    resultado_soma += soma_num
    print(f" A soma dos numeros digitados é {resultado_soma}")

frase = input("Informe uma frase: ").lower()
letras = set()
for letra in frase:
    if letra.isalpha():
         letras.add(letra)
    if len(letras) == 26:
        print("A frase é um pangrama.")
    else:
        print("A frase não é um pangrama.")



