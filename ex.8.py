# 1.Fazer uma lista de frutas
fruta = ['maça', 'pera', 'uva']   
print(fruta)


# 2. imprimir um elemento de uma lista
numeros = [1, 3, 5, 7, 9]
print(numeros[3])

# 3. replace um nome em uma lista
nomes = ['Varun', 'Adi', 'Daya', 'Dhiman']
nomes[1]= 'Adivania'
print(nomes)
print('Primeiro', nomes[0])

# 4. fazer a media de notas dewde um aluno
notas = [9, 7, 9, 10, 8]
resultado = sum(notas) / 5
print(f'A nota final do aluno é {resultado}.')

# 5. Criar lista de 1-10 e imprimir apenas os pares
for elemento in range(1,11):
    if elemento % 2 == 0:
        print(elemento)

# 6.Considere a seguinte lista de frutas . Imprima o primeiro e o último elemento da lista
lista_frutas = ['banana', 'maçã', 'uva', 'abacaxi', 'morango' ]
print(f' O primeiro elemento da lista é {lista_frutas[0]} e o ultimo elemento da lista é {lista_frutas[4]}.')
print(lista_frutas[1])
lista_frutas = ['banana', 'maçã', 'uva', 'abacaxi', 'morango']

# --- Opção 1: Usando vírgula no print (método padrão) ---
# A vírgula no print adiciona automaticamente um espaço entre os elementos.
print('Primeiro:', lista_frutas[0], '| Último:', lista_frutas[4])

# --- Opção 2: Concatenação com operador + ---
# É necessário converter o elemento para str() se ele não for uma string.
print('Frutas selecionadas: ' + lista_frutas[1] + ' e ' + lista_frutas[3])

# --- Opção 3: Usando o método .format() (estilo antigo/alternativo) ---
print('Frutas: {} e {}'.format(lista_frutas[0], lista_frutas[4]))

# --- Opção 4: Desempacotamento de lista (print com desempacotamento) ---
# Imprime os dois elementos separados por espaço
print(lista_frutas[0], lista_frutas[4])

# 7. Crie uma lista chamada numeros com os números de 1 a 5. Utilize um loop para imprimir cada número da lista.
numeros = [1, 2, 3, 4, 5]
for elemento in numeros:
    print(elemento)

# 8. Imprimir apenas idades maiores que 30 utilizando loop
idades = [18, 25, 32, 47, 53, 60]
for elemento in idades:
   if elemento >= 30:
       print(elemento)

# 9. Slicing para imprimir de 3-8
numeros = [1, 2, 3, 4, 5, 6, 7, 8,9, 10]
print(numeros[2: 10: 1])

# 10. Crie uma lista chamada letras com as letras de A a J. Utilize o slicing para imprimir as letras de C a G.
letras_alf = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(letras_alf[2:10:1])

# 11.Crie uma lista chamada cores com 5 cores diferentes. Utilize o método sort() para ordenar a lista em ordem alfabética. Imprima a lista ordenada.
cores = ['azul', 'branco', 'verde', 'amarelo', 'vermelho']
cores.append('preto')
cores.insert(0,'roxo')
cores.sort()

print(cores)

# 12. Crie uma lista chamada numeros com 3 números repetidos. Utilize o método count() para contar quantas vezes o número 3 aparece na lista. Imprima o resultado:

num_repetidos = [1, 2, 3, 3,4, 6, 7, 7, 9, 10, 11, 3]
print(num_repetidos.count(3))

# 13. Exercício 13: Crie uma lista chamada frutas com 3 elementos. Utilize o métodoappend() para adicionar mais uma fruta à lista. Imprima a lista atualizada.
fruta_fresca = ['acerola', 'manga', 'abacate']
fruta_fresca.append('caju')
print(fruta_fresca)

# 14. Crie uma lista chamada numeros com os números de 1 a 3. Utilize o método reverse() para inverter a ordem dos números na lista. Imprima a listainvertida.
num_inv = [1, 2, 3]
num_inv.reverse()
print(num_inv)

# 15. Crie uma lista chamada animais com 5 elementos. Utilize o método pop() para remover o terceiro elemento da lista. Imprima a lista após a remoção.
anim = ['elefante', 'jacaré', 'urso', 'borboleta', 'macaco']
anim.pop(3)
print(anim)