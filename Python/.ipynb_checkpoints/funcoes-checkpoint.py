Precos = [1500, 1000, 800, 2000]



def calculoImposto(preco, aliq1=0.1, aliq2=0.15): # Estrutura basica de função, entre parenteses podem ser colocados parametros e podemos definir um valor padrão para os parametros
        
        ImpostoAcumulado = 0
        porcentagemImposto = 0
        if preco <= 1000:
            valor_imposto = preco * aliq1

            ImpostoAcumulado = ImpostoAcumulado + valor_imposto
            porcentagemImposto = porcentagemImposto + aliq1
            novo_valor = preco + valor_imposto
            print(f"Valor do produto: R${preco: .2F}, valor do imposto: R${valor_imposto: .2F}, Valor final do produto: R${novo_valor: .2F}, imposto acumumulado: R${ImpostoAcumulado: .2F}\n")
        elif preco >= 1000:
            valor_imposto = preco * aliq2

            ImpostoAcumulado = ImpostoAcumulado + valor_imposto
            porcentagemImposto = porcentagemImposto + aliq2
            novo_valor = preco + valor_imposto
            print(f"Valor do produto: R${preco: .2F}, valor do imposto: R${valor_imposto: .2F}, Valor final do produto: R${novo_valor: .2F}, imposto acumumulado: R${ImpostoAcumulado: .2F}\n")
        
        # print("O imposto acumulado foi de: ", ImpostoAcumulado)
        # print(f"A porcentagem de imposto acumulado foi de: {porcentagemImposto}%")
        return ImpostoAcumulado, porcentagemImposto # Se o return for passado desta forma, serão retornados os valores entre parenteses como uma tupla

for preco in Precos:
    calculoImposto(preco, aliq1=0.5, aliq2= 0.25) # Mesmo com valores pré definidos, é possivel alterar os valores dos parametros na chamada da função. Se deixar vazio, serão utilizados os parametros padrão

resultado = calculoImposto(10000)
print(resultado) # ao printar o resultado recebemos a tupla (1500.0, 0.15)