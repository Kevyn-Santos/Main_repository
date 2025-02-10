a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
numeroEscolhido = int(input("Digite um numero: "))


# for elements in a:
#     if elements < 5:
#         print(elements)

# Fazer uma lista que contenha os numeros menosres que 5 e printar a lista
# b = []

# for elements in a:
#     if elements < 5:
#         b.append(elements)

# print(b)

# Escrever o código em uma linha

# for elements in a: print(elements) if elements < 5 else print(f"elemento maior que 5")

# Elementos menores dos que o atribuido pelo usuario

c = []
maximo = max(a)

for elements in a:
    if elements < numeroEscolhido and elements < maximo:
        c.append(elements)
        print(c)
    else:
        print("Numero escolhido excede o numero maximo da lista")



