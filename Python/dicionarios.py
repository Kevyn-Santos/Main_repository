# Um dicionario é uma estrutura de dados onde cada elemento possui umvalor diretamente atribuido a ele.
# Ou seja, é uma estrutura chave-valor, como um objeto
#  dicionarios são escritos entre {}, e possuem a estrutura Chave : Valor <- pode ser qualquer tipo de dado

produtos = ["Celular", "Camera", "Fone de ouvido", "Monitor"]
Precos = [1500, 1000, 800, 2000]

dicPrecos = {
    "Celular": 1500,
     "Camera": 1000,
     "Fone de ouvido": 800,
     "monitor": 2000
}

# seleção e edição de itens

precoCelular = dicPrecos["Celular"] # Para selecionar um item, passe o dicionario e a chave do item
print(precoCelular)

dicPrecos["Camera"] = 5000 # Para editar um item, passe o dicionario e a chave de um item de um lado da igualdade, e o novo valor do outro lado
print(dicPrecos["Camera"])

# Adição de itens

dicPrecos["Macbook"] = 8000 # para adicionar um item usamos a mesma sintatica da edição. Se o item existir ele é editado, senão, ele é adicionado ao dicionario 
print(dicPrecos)

# Remoção de itens

dicPrecos.pop("Macbook") # Usa-se o POP para remover um item, bastando passar sua chave
print(dicPrecos)

# Tamanho do dicionario
print(len(dicPrecos)) # Usa-se o len para extrair o tamanho de um dicionario, este será a quantidade de itens nele

# Busca de valores

print("Celular" in dicPrecos) # Se não for passada nenhuma keyword, a busca por padrão sera feita nas chaves do dicionario
print(1500 in dicPrecos) # portanto, a chave "Celular" existe, mas a chave "1500" não
print (1500 in dicPrecos.values()) # Para procurar um valor ao invés da chave, passe a keyword values()
print(dicPrecos.keys()) # a keyword keys, retorna as chaves do dicionario
print(dicPrecos.values()) # a keyword values, retorna os valores da chave