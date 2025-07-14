from produtos import produto
import random as rd

def gerarProdutos():
    produtos = []
    for x in range(15):
        y = produto(nome= f"produto {x+1}", preço=rd.random()*5)
        produtos.append(y)

    return produtos