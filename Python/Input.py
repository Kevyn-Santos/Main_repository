Nome = input("Digite seu nome: ") # Para que uma informação seja dada diretamente pelo usuario, usamos a função Input
Email = input("Digite seu E-mail: ") # Quando algo for digitado pelo usuario ele virá como string, ou seja, se for digitado um numero ele deverá ser formatado utilizando Int() ou float()

Vendas = input("Digite as Vendas do dia: ")
Vendas = float(Vendas)

Bonus = Vendas * 0.01
Rendimento = Vendas + Bonus

Nome = Nome.lower().title().strip() #Strip() para tirar espaços extras
Email = Email.lower().capitalize()

posição = Email.find("@")
print(Email[posição +1: ])

# Extrair o 1º nome do usuario

posicaoEspaco = Nome.find(" ")
PrimeiroNome = Nome[:posicaoEspaco]
print(PrimeiroNome)

# Construir uma mensagem de cadastro

print(f"Usuario {PrimeiroNome} cadastrado com sucesso com o e-mail {Email}")

# Construir uma mensagem de envio de e-mail com asteristico

emailpos = Email[2: posição] # Extraia todo o texto entre a segunda posição e o @ e armazene a parte extraida na variavel
emailSubs = Email.replace(emailpos, "***") # armazene todo o e-mail substituindo a parte extraida por ***
print(f"Foi enviado um e-mail de confirmação para {emailSubs}") # mostre o e-mail armazenado que foi substituido 

print(f"{Nome} seu Bonus para as vendas são de: R${Bonus: .2F}, somando um rendimento de: R${Rendimento: .2F}")