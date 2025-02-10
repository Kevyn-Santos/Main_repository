vendas = {
    "Andre": [1000, 500, 300, 5000, 80, 3000],
    "Andressa": [1500, 9000, 300, 150, 1500, 120],
    "Alan": [800, 100],
    "Ana": [800, 900, 950, 1200, 1600, 130]
}

# A cada venda, o vendedor ganha R$2 e 1% do valor da venda
# calcular o valor total de bonus pago e o valor de bonus para cada vendedor

def calcularBonus(lista_vendas): # é criada uma função para calcular o bonus que recebera uma lista de vendas

    qtde = len(lista_vendas) # A quantidade de vendas é igual ao tamanho de cada lista no dicionario
    bonus1 = qtde *2 # o primeiro bonus (2R$ para cada venda) é calculado

    valorTotal = sum(lista_vendas) # é calculada a soma das vendas das listas dos dicionarios
    bonus2 = 0.01 * valorTotal # o bonus2 (1% do valor da venda) é calculado com  base no valor total de vendas, retornando assim o bonus total por todas as vendas da lista

    bonus = bonus1 + bonus2 # O bonus final é a soma dos dois bonus calculados ao longo da função
    return bonus

bonusTotal = 0
for vendedor in vendas: # será percorrido o dicionario
    listaDeVendasVendedor = vendas[vendedor] # A varivael armazena cada valor da lista que passar pelo for
    bonus = calcularBonus(listaDeVendasVendedor) # é executada uma finção para calcular o bonus dependendo dos valores da lista
    print(f"Vendedor: {vendedor}, bonus: {bonus}")
    bonusTotal = bonusTotal + bonus

print(bonusTotal)
