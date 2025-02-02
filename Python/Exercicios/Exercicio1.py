Nome = "João Paulo Lira"
Email= "joãoFalso@gmail.com"
# Descobrir o servidor do e-mail

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
print(emailSubs) # mostre o e-mail armazenado que foi substituido 