#Funçoes lambda, map, filter, reduce

# Lambda(anonimas) -> funções sem nome que são usadas em um lugar especifico de momento.
# Lambda argumentos: expressão


### iterar uma função lambda

# quadrado = lambda x: x**2 # atribuição da função lambda dentro da variavel quadrado

# for i in range(1,11): 
#     print(quadrado(i)) # a chamada da variavel quadrado passando o valor de i como o parametro que alimenta x na função



### podemos passar um unico valor dependendo da função

# par = lambda x: x%2 == 0 

# print(par(12))



### Podemos passar mais de um valor dentro da função lambda, e atribuir valores padrão para os argumentos(tal qual em uma fujnção normal)

# teste = lambda x,y=2: x%y == 0 
# print(teste(21, 21))



#### Função Map() -> permite aplicar uma função para cada objeto iteravel, é como um foreach
# Map(função, objetos iteraveis(geralmente listas))

# lista = [1,2,3,4,5]
# resultado = list(map(lambda x: x*2, lista))# executa a função lambda em cada elemento de "lista", depois cria uma lista com os resultados e armazena a lista na variavel "Resultado"
# print(resultado)
# for itens in resultado:
#     print(itens)


# def maiuscula(): #definindo uma função externa ao map
#     return str.upper

# palavras = ["um", "dois", "TreS", "Quatro", "Cinco"]
# Res_String = list(map(maiuscula(), palavras)) # Executa a função definida "Maiuscula" em cada palavra da lista "palavras"
# print(Res_String)


### Função Filter() -> extrai elementos de uma sequencia dado um certo criterio
# filter(Função de criterios, objetos iteraveis)

# def maiuscula(): 
#     return str.upper

# palavras = ["um", "dois", "TreS", "Quatro", "Cinco"]

# ele verifica se os valores de uma lista são verdadeiros ou falsos dada uma função, se for verdadeiro ele armazena dentro da variavel, se for falso não faz nada. 
# Por isso a função filter não funcionou com a função maiuscula, pois esta ultima não retorna verdadeiro ou falso


# listaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# numPar = list(filter(lambda x: x%2==0, listaNumeros))
# numimpar = list(filter(lambda x: x%2==1, listaNumeros))
# print(f"""São pares os numeros {numPar}
# E são impares os numeros {numimpar}""")



### Função reduce() -> deve ser importada de functools, executa uma função cumulativa em uma lista de elementos, retornando um unico valor acumulado
# Reduce(Função, objetos iteraveis, valor inicial(opcional))

from functools import reduce

# def mult(x,y):
#     return x * y

# numeros = [1,2,3,4,5]
# total = reduce(mult, numeros) # A função esta multiplicando cada valor de numeros de maneira acumulativa, ou seja, 1*2, o resultado *3, o resultado *4, e o resutado *5. Ao final retornando um unico valor, ao invés de uma lista de valores
# print(total)

 
# numeros = [1,2,3,4,5]

# # Eleva dois elementos ao quadrado e soma seus resultados, isso é feito até o ultimo elemento da lista e no final retorna um unico valor como resultado

# total = reduce(lambda x,y: x**2 + y**2, numeros) 
# print(total)




### Sintaxe das funções
# lambda -> lambda argumento: expressao (a função lambda pode ser usada em qualquer outra função especial)
# map() -> map(função, lista de elementos)
# Filter -> filter(função de criterio, lista de elementos) --> funciona apenas com funções que retornam verdadeiro ou falso
# reduce -> reduce(função cumulativa, lista de elementos) --> executa de maneira acumuativa um calculo sobre uma lista de elementos e retorna o valor acumulado ao final
# A função reduce precisa ser importada da biblioteca 'functools'

