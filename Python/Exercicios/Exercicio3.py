#desafio sistema de preços

dicPrecos = {
    "Celular": 1500,
     "Camera": 1000,
     "Fone de ouvido": 800,
     "monitor": 2000
}
produto_Usuario = input("Digite o produto que quer buscar: ").lower().capitalize()

if produto_Usuario in dicPrecos:
    print(f"O produto {produto_Usuario} custa R${dicPrecos[produto_Usuario]}")
else:
    cadastroProduto = input("Produto não cadastrado, deseja cadastra-lo? SIM / NÃO (Y/N): ").upper()
    if cadastroProduto == "SIM" or cadastroProduto == "Y":
        NovoProduto = produto_Usuario.capitalize()
        NovoPreco = float(input("Digite o novo preço do produto: "))
        dicPrecos[NovoProduto] = NovoPreco
        print(f"Produto {NovoProduto} cadastrado com sucesso", dicPrecos)
    elif cadastroProduto == "NÃO" or cadastroProduto == "N":
        print("O produto não foi encontrado e não foi cadastrado")
        print(dicPrecos)

