def calcularImposto(preco, ir=0.275, csll=0.035, iss=0.05):
    impostoIR = preco * ir
    impostoCSLL = preco * csll
    impostoISS = preco * iss

    return impostoISS, impostoCSLL, impostoIR # As tuplas sçao criadas se forem passados varios retornos de uma vez para uma função

resposta = calcularImposto(1000)
# print(resposta) # Imutavel e Informatavel
# print(resposta[0])
# print(f"{resposta[1]:.2F}") # Imutavel mas formatavel
# print(resposta[2])

# (500.0, 350.00000000000006, 2750.0) -> lista imutavel de resultados. 
# Segue as mesmas propriedades de uma lista, porem seus valores não podem ser editados
# é possivel formatar um valor de uma tupla, mas não a tupla completamente, sendo assim, é necessario pegar o valor de um indice primeiro antes de trabalhar com ele


# Unpacking -:> este é o prcesso de segmentar os valores de uma tupla em variaveis diferentes

ir, csll, iss = resposta # As variaveis são criadas de uma vez, e os valores atribuidos são correspondente a ordem da tupla, 
# ou seja, 1º valor -> 1ª variavel, 2º valor -> 2ª variavel, 3º valor -> 3ª variavel


print(ir, csll, iss, sep="\n") # Obs: sep= define um separador para cada instancia do print, neste caso é a quebra de linha (\n)
print(f"{ir},\n{csll:.2F},\n{iss}") # Após a atribuição ás variaveis, é possivel formatar os valores

tamanhoTela = (800, 500) # Uma tupla pode ser criada utilizando vaores entre parenteses
Padrao = ("Valor", "Padrao") # a tupla pode ser de strings tambem

print(Padrao[0])
print(Padrao[1])
print(tamanhoTela[0])
print(tamanhoTela[1])

