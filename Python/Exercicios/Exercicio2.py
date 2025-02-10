#desafio sistema de preços

produtos = ["Celular", "Camera", "Fone de ouvido", "Monitor"]
Vendas = [1500, 1000, 800, 2000]
produto_Usuario = input("Digite o produto que quer buscar: ").lower().capitalize()

if produto_Usuario in produtos:
    indice = produtos.index(produto_Usuario)
    print(Vendas[indice])
else:
    cadastroProduto = input("Produto não cadastrado, deseja cadastra-lo? SIM / NÃO (Y/N): ").upper()
    if cadastroProduto == "SIM" or cadastroProduto == "Y":
        NovoProduto = input("Digite o nome do novo produto: ").capitalize()
        NovoPreco = float(input("Digite o novo preço do produto: "))
        produtos.append(NovoProduto)
        Vendas.append(NovoPreco)
        print(produtos)
        print(Vendas)
    elif cadastroProduto == "NÃO" or cadastroProduto == "N":
        print("O produto não foi encontrado e não foi cadastrado")
        print(produtos)
        print(Vendas)
