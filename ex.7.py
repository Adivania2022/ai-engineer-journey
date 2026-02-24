numero = int(input("Digite um numero: "))
if numero % 2 == 0:
    print(f"O numero {numero} é par.")
else:
    print(f"O numero {numero} é impar.")


idade = int(input("Digite a sua idade:"))
if idade >= 18:
    print("Parabéns você já pode votar.")
else:
    print(f" Você não pode votar ainda. Precisa aguardar {18 - int(idade)} anos.")

numero_1 = float(input(" Digite um numero: "))
numero_2 = float(input(" Digite um numero: "))
if numero_1 > numero_2:
    print("O primeiro numero é maior.")
elif numero_2 > numero_1:
    print("O segundo numero é maior.")
else:
    print("Os numeros são iguais")


for num_par in range(2,101,2):
    print(num_par)

for num_para in range (1,101):
    if num_para % 3 == 0 and num_para % 5 == 0:
        print("FIZZ BUZZ")
    elif num_para % 3 == 0:
        print("FIZZ")
    elif num_para % 5 == 0:
        print("BUZZ")
    else: 
        print(num_para)

numero_tabuada = int(input("Digite um número: "))

for i in range(1, 11):

    print(f" {numero_tabuada} x {i} = {numero_tabuada * i}")

palavra = input(" Digite uma palavra: ")
if palavra == palavra[::-1]:
    print(f"Essa palavra {palavra} é um palindromo.")
else:
    print(f"Essa palavra {palavra} não é um palindromo.")

num_prim = int(input("Digite um numero para verificar se ele é primo: "))
primo = true
for i in range(2, int(numero ** 0.5) + 1):
    if numero % i == 0:
        primo = False
        break

if primo:
    print("O numero é primo.")
else:
    print(" O numero não é primo.")

