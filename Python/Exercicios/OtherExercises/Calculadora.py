Numero1 = float(input("Insira o primeiro numero: ")) # Conversão de dados junto de input
Numero2 = float(input("Insira o segundo numero: "))
Operacao = int(input("Selecione a operação: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Módulo \n"))


def Soma(num1, num2): # funções simles com dois parametros
    return print(f"A soma de {num1} e {num2} é {num1 + num2}") # retorno da função

def Sub(num1, num2):
    return print(f"A Subtração de {num1} e {num2} é {num1 - num2}")

def Mult(num1, num2):
    return print(f"A multiplicação de {num1} e {num2} é {num1 * num2}")

def Div(num1, num2):
    return print(f"A divisão de {num1} e {num2} é {num1 / num2}")

def Mod(num1, num2):
    return print(f"O resto da divisão de {num1} e {num2} é {num1 % num2}")



"""match Operacao: # Match case => switch case
    case 1:
        Soma(Numero1, Numero2)
    case 2:
        Sub(Numero1, Numero2)
    case 3:
        Mult(Numero1, Numero2)
    case 4:
        Div(Numero1, Numero2)
    case 5:
       Mod(Numero1, Numero2)"""

if Operacao == 1: #laço condicional 
    Soma(Numero1, Numero2) #Função dependendo do laço
elif Operacao == 2:
    Sub(Numero1, Numero2)
elif Operacao == 3:
    Mult(Numero1, Numero2)
elif Operacao == 4:
    Div(Numero1, Numero2)
elif Operacao == 5:
    Mod(Numero1, Numero2)
else:
    print("Nenhuma operação valida selecionada")




""" print(f"A soma dos dois numeros é: {Numero1 + Numero2}")
print(f"A multiplicação dos dois numeros é: {Numero1 * Numero2}")
print(f"A subtração dos dois numeros é: {Numero1 - Numero2}")
print(f"A divisão dos dois numeros é: {Numero1 / Numero2}")
print(f"o resto da divisão dos dois numeros é: {Numero1 % Numero2}") """