Precos = [1500, 1000, 800, 2000]


# for preco in Precos: # é como um for each, onde o primeiro nome representa o segundo, e o limite do FOR é dado pelo segundo parametro, 
#     print(preco) # nesse caso o python calcula automaticamente o tamanho da lista e exibibe a quantidade de informações baseado no tamanho


# for i in range(len(Precos)): # Neste caso, temos a variavel i e temos o parametro range, o mais importante é o segundo parametro, pois ele define a quantidade de repetiçoes do for
#     print(Precos[i]) #neste caso, serão mostrados os preços na posição de i, e este vai se repetir conforme o tamanho do aray preços


# for i in range(10): # esta é outra forma de escrever usando Range, aqui passamos diretamente quantas vezes o codigo repetira.
#     print("Olá mundo")

# for preco in Precos:
#     imposto = preco * 0.1
#     print("imposto sobre o produto: ", imposto)
#     print("valor total com o imposto: ", preco + imposto)

# imposto até/acima 1000

# for preco in Precos:
#     if preco <= 1000:
#         imposto = 0.1
#         valor_imposto = preco * 0.1
#         novo_valor = preco + valor_imposto
#         print(f"Valor do produto: R${preco: .2F}, valor do imposto: R${valor_imposto: .2F}, Valor final do produto: R${novo_valor: .2F}")
#     elif preco >= 1000:
#         imposto = 0.15
#         valor_imposto = preco * imposto
#         novo_valor = preco + valor_imposto
#         print(f"Valor do produto: R${preco: .2F}, valor do imposto: R${valor_imposto: .2F}, Valor final do produto: R${novo_valor: .2F}")

# Imposto acumulado

# ImpostoAcumulado = 0
# porcentagemImposto = 0
# for preco in Precos:
#     if preco <= 1000:
#         imposto = 0.1
#         valor_imposto = preco * 0.1

#         ImpostoAcumulado = ImpostoAcumulado + valor_imposto
#         porcentagemImposto = porcentagemImposto + imposto
#         novo_valor = preco + valor_imposto
#         print(f"Valor do produto: R${preco: .2F}, valor do imposto: R${valor_imposto: .2F}, Valor final do produto: R${novo_valor: .2F}, imposto acumumulado: R${ImpostoAcumulado: .2F}")
#     elif preco >= 1000:
#         imposto = 0.15
#         valor_imposto = preco * imposto

#         ImpostoAcumulado = ImpostoAcumulado + valor_imposto
#         porcentagemImposto = porcentagemImposto + imposto
#         novo_valor = preco + valor_imposto
#         print(f"Valor do produto: R${preco: .2F}, valor do imposto: R${valor_imposto: .2F}, Valor final do produto: R${novo_valor: .2F}, imposto acumumulado: R${ImpostoAcumulado: .2F}")

# porcentagemImposto = porcentagemImposto * 100
# print("O imposto acumulado foi de: ", ImpostoAcumulado)
# print(f"A porcentagem de imposto acumulado foi de: {porcentagemImposto}%")


# Variação de vendas

vendas22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

for mes in vendas23:
    valor22 = vendas22[mes]
    valor23 = vendas23[mes]

    variacao = ((valor23 / valor22) - 1)

    print(f"{valor22: .2F}, {valor23: .2F}, {mes}, {variacao: .2%}")
