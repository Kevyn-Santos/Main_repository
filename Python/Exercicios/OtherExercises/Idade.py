from datetime import datetime

Nome = str(input("informe seu nome: "))
Idade = int(input("Informe sua idade: "))
NumeroRepeticoes = int(input("Digite quantas vezes deseja ver a mensagem: "))

DataAtual = datetime.today().year
NovaData = (100 - Idade) + DataAtual

print( NumeroRepeticoes * f"Olá {Nome}, você fará cem anos em {NovaData} !\n")

