# Exercício 1: Crie um dicionário vazio chamado linguagens.
linguagem = {}
print(linguagem)

#Exercício 2: Adicione as seguintes informações ao dicionário linguagens:
#Chave: ‘Python’, Valor: ‘Linguagem de programação de alto nível’
#Chave: ‘Java’, Valor: ‘Linguagem de programação orientada a objeto’
#Chave: ‘JavaScript’, Valor: ‘Linguagem de programação interpretada’
linguagem_1 = {
    "Python" : "Linguagem de programação de alto nível",
    "Java" : "Linguagem de programação orientada a objeto",
    "JavaScript" :  "Linguagem de programação interpretada"
}
print(linguagem_1)

#Exercício 3: Acesse o valor correspondente à chave ‘Java’ no dicionário linguagens e armazene-o em uma variável chamada descricao_java.

descricao_java = linguagem_1["Java"]
print(f' A descrição Java é {descricao_java}.')


#Exercício 4: Verifique se a chave ‘Python’ existe no dicionário linguagens e armazene o resultado em uma variável chamada python_existe.

python_existe = "Python" in linguagem_1
print(python_existe)

#Exercício 5: Crie um novo dicionário chamado linguagens_populares com as seguintes informações:
#Chave: ‘Python’, Valor: 2
#Chave: ‘Java’, Valor: 1
#Chave: ‘JavaScript’, Valor: 3

linguagens_populares = {
    "Python" : "2",
    "Java" : "1",
    "JavaScript" : "3"
}

print(linguagens_populares)
itens = linguagens_populares.items()
print(itens)

#Exercício 6: Atualize o valor da chave ‘Python’ no dicionário linguagens_popularespara 4.
linguagens_populares["Python"] = 4
print(linguagens_populares)

#Exercício 7: Remova a chave ‘Java’ do dicionário linguagens_populares.
linguagens_populares.pop("Java")
print(linguagens_populares)

#Exercício 8: Crie uma variável chamada chaves e atribua a ela uma lista com todas aschaves do dicionário linguagens_populares.
Chaves = linguagens_populares.keys()
print(Chaves)

#Exercício 9: Crie uma variável chamada valores e atribua a ela uma lista com todos os valores do dicionário linguagens_populares.
Valores = linguagens_populares.values()
print(Valores)

#Exercício 10: Crie uma variável chamada itens e atribua a ela uma lista de tuplas contendo todos os itens do dicionário linguagens_populares.

itens = list[linguagens_populares.items()]
print(itens)

#Exercício 11: Crie um novo dicionário chamado linguagens_duplicadas com as seguintes informações:
#Chave: ‘Python’, Valor: 3
#Chave: ‘Java’, Valor: 3
#Chave: ‘JavaScript’, Valor: 3
linguagens_duplicadas = {
   "Python" : 3,
   "Java" : 3,
   "JavaScript" : 3 
}
print(linguagens_duplicadas)

#Exercício 12: Verifique se pelo menos um dos valores do dicionário linguagens_duplicadas é igual a 5 e armazene o resultado em uma variável chamada 

valor_cinco_existe = 5 in linguagens_duplicadas.values()
print(valor_cinco_existe)
