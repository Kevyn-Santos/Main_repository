#Temos tres formas para mostrar o valor das variaveis junto de textos, podemos escrever a função Print desta forma: print("Texto", Variavel).
# Ou podemos escrever desta forma Print(f"Texto {variavel}"), onde o f indica que o texto é uma string formatada
# Ou podemos concatenar os textos utilizando "+", porem ele só concatenará strings. Print("texto" + "outro texto")
# Caso seja uma variavel numerica, podemos mudar seu tipo com a função str(). Print("Texto" + str(Variavel))

# Sendo assim, as funções de transformação de dados, devem ser usadas depois da declaração inicial das variaveis, 
# ou seja, na hora de sua amostragem ou na hora que ela for usado de outra forma

# Nós possuimos nativamente algumas funções para manipulação de textos como: 
# .lower(Coloca o texto em minusculo) e .upper(coloca o texto em maiusculo)
# Capitalize(Coloca a primeira letra do texto em maiuscula)
# title(), coloca a primeira letra de cada palavra em maiusculo
# find(Procura um caractere especifico no texto), a contagem começa em 0, se o caractere não for encontrado retorna -1
# len(), retorna o tamanho de um texto
# replace(), substitui uma parte do texto

# É possivel passar duas funções ao mesmo tempo para strings Print(variavel.lower().capitalize()) 
# Isso mostrará a variavel completamente minuscula, com excessão da primeira letra 

"""
faturamento = 1000
custo = 700
lucro = faturamento - custo

print(f"Faturamento: R${faturamento}, Custo: R${custo}, Lucro: R${lucro}")
print("faturamento: " + str(faturamento))
print(str(lucro))
"""

email = "EmAil_TEste@gmail.COM"

# Mudar a formatação do texto
nome = "kevyn santos"
email = email.lower().capitalize()
print(email)
print(nome.title())

# Encontrar e mostrar pedaços do texto
print(email.find("_"))
print(email[5]) # É possivel extrair um pedaço do texto indicando a variavel e o indice onde esta o pedaço que se quer extrair, esta indicação do indice deve ser feita com colchetes

posiçãoInicioServidor = email.find("@")
posiçãoFinalServidor = email.find(".")
print(email[posiçãoInicioServidor : posiçãoFinalServidor]) # é possivel delimitar a busca do pedaço de texto utilizando (:) onde ao lado esquerdo fica o primeiro caractere de busca e ao direito o ultimo caractere de busca

# Se não for estipulado um ultimo caractere, a função retornará tudo até o final da string
# A direçao de busca é definida por onde estão os dois pontos, se estiverem na frente do delimitador inicial, a busca retornará tudo o que estiver á frente. 
# Se estiverem atras do delimitador inicial, a busca retornará tudo o que estiver atras 

# Encontrar o tamanho de um texto
tamanho = len(email)
print(tamanho)

# Susbtituir um pedaço do texto

novoEmail = email.replace("gmail.com", "outlook.com") # Para usar a funçaoi replace é necessario passar o texto antigo e o texto novo.
print(novoEmail)

# Formatações especiais

# numericas
faturamento = 1000
custo = 700
lucro = faturamento - custo
margem = lucro / faturamento
print(f"Faturamento: R${faturamento: ,.2F}, Custo: R${custo: .2F}\n Lucro: R${lucro: .2F}, Margem: {margem: .2%}") # O : indica que uma variavel estará sendo formatada, portanto as formatações devem vir depois deles

# .2F indica que aquele numero será um float de duas casas decimais, portanto o ponto é o separador decimal
# ,.2F indica que aquele numero será um float com separação de milhar e decimal. Portanto a virgula é o separador de milhar e deve obrigatoriamente vir antes do ponto, senão da erro
# .1% Indica que aquele numero será formatado como porcentagem contendo uma casa decimal
# \n quebra de linha