# O bloco de trtamento de erros é o try..except
# as palavras chaves principais são:
#  Try -> enta executar um bloco de código
# Except -> captura um erro especifico que ocorre num bloco de código e faz algo se o erro ocorrer
# Else -> faz algo se não houver o erro
# Finally -> executa um bloco de codigo independente se houver ou não erros
# raise -> força a aparição de um erro em determibado pedaço do código

def divisao(x: int, y: int):
    return round(x / y, 2)



try: # o bloco try vai tentar capturar dois numeros digitados pelo usuario e fazer a divisão deles
    while True:
        num1 = int(input("Digite um numero: "))
        num2 = int(input("Digite outro numero: "))
        resultado = divisao(num1, num2)
        break
except ZeroDivisionError: # caso seja feita a divisão pro zero, a mensagem dentro do except vai ser lançada
    print("Não é possivel dividir por zero.")
except ValueError: # è possivel colocar mais de um except no mesmo bloco try
     print(f"Houve um problema na leitura dos valores. O primeiro ou segundo valor não são numeros inteiros")
else: # se não houver erros, a mensgaem informando o resultado vai ser lançada
    print(f"A divisão de {num1} por {num2} é igual a {resultado}")
finally: # A mensagem de fim de código será sempre executada independente dos erros estarem la ou não
    print("\nFim do código")

