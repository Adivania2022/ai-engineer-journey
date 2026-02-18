
numero_1 = input("Digite o primeiro numero: ")
numero_2 = input("Digite o segundo numero: ")

print("Operação a ser realizada: \n\t+ para adição \n\t- para subtração \n\t* para multiplicação \n\t/ para divisão")

operação = input("Digite a operaçao: ")

equação = f"{numero_1} {operação} {numero_2}"

resultado = eval(equação)

print(f"{"*" * 25}\nResultado: {resultado}\n{"*" * 25}")



idade = input("Digite a sua idade: ")

sexo = input('Digite seu sexo ("M" para Masculino e "F" para Feminino: ')

if sexo.upper() == 'M':
# Código para o Sexo Masculino 
    if int (idade) >= 65:
        print("Parabéns! Chegou a sua vez.") 
    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {65 - int (idade)} anos.')

elif sexo.upper() == 'F':
# Código para o Sexo Feminino 
    if int (idade) >= 60:
        print("Parabéns! Chegou a sua vez.") 
    else:
        print(f'Sua vez ainda não chegou! Aguarde mais {60 - int (idade)} anos.')