# Variaveis não precisam de palavra chave para declaração, e são fracamente tipadas, mas seu tipo pode mudar
# Os tipos basicos de dados são Int, Float, String, Bool
# Os operadores principais são Soma(+), Subtração(-), Multiplicação(*), Divisão(/), Módulo(Resto(%))
# Para mostrar os dados usa-se a função Print()



faturamento = 1000 #Primeira declaração de uma variavel
custo = 700
novas_Vendas = 300

faturamento = faturamento + novas_Vendas # segunda declaração de uma variavel, agoar seu valor não é mais mil, mas sim 1300. ou seja, as variaveis em python não são constantes, mas sim mutaveis.

imposto = faturamento * 0.1 # 1 = 100% de algo, sendo assim, 0.1 = 10% de algo. O separador de decimais é o ponto (.)
lucro = faturamento - custo - imposto
margem_de_lucro = (lucro / faturamento) * 100

""" print("O faturamento é de", faturamento)
print("O imposto é de", imposto)
print("O lucro é de", lucro)
print("A margem lucro é de", margem_de_lucro, "%") """

