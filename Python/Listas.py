
# Criação de array

Vendas =  [100, 50, 300, 120, 800, 1200] # Uma lista é um array, ou seja, como trabalhar com arrays
# As regras são as mesmas, a contagem dos indices começa do zero 

# Exibição de array

print(Vendas[4]) # e para mostrar um indice especifico basta passa-lo junto do nome do array
print(Vendas[-1]) # se for passado um indice negativo, a contagem passa a ser da direita para a esquerda(send assim -1 é o ultimo indice)

# Funções/Operações em arrays

TotalVendas = sum(Vendas) # soma todos os valores do array
QuantidadeVendas = len(Vendas) # Retorna o tamanho do array, ou seja, a quantidade de elementos
ValorMax = max(Vendas) # Retorna o valor maximo do array
ValorMin = min(Vendas) # retorna o valor minimo do array

# print(TotalVendas, QuantidadeVendas, ValorMax, ValorMin)

# Parametros do array
print(Vendas.index(300)) # Index retorna a posição de um elemento

Produtos = ["Iphone", "Ipod", "Airpod"]
precos = [4000, 5000, 2000]

## Edição e verificação de elementos
precos[1] = 4500 # é possivel mudar o valor de um elemento especifico passando seu indice atribuindo um novo valor
print("Iphone" in Produtos) # "in" Verifica se um elemento esta no array, faz diferenciação entre maiusculas e minusculas
print(precos)

## Adição de itens
Produtos.append("Macbook") # O Append inclui um valor no ultimo indice do array
precos.append(10000)

print(Produtos)
print(precos)

## Remoção de itens
Produtos.remove("Macbook") # "Remove", retira um elemento do array de acordo com seu valor
precos.pop(-1) # "pop", retira um elemento do array de acordo com seu indice

print(Produtos)
print(precos)

## Inserção de valores

Produtos.insert(2, "Iphone") # "insert", insere um valor em um indice definido
print(Produtos)

## Contagem de valores
print(Produtos.count("Iphone")) # "Count", conta quantas vezes um valor especifico aparece no array

## Ordenação
precos.sort() # "sort", ordena os valores de uma lista em ordem crescente ou alfabetica. Para ordenar de maneira decrescente basta passar o parametro reverse=True
print(precos)