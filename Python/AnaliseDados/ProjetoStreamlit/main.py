# Para executer o arquivo é necessario usar o comando streamlit run <nome do arquivo>
# Se isso não funcionar use, python -m streamlit run <nome do arquivo>
# A função write()escreve um texto na tela
# os graficos possuem funções proprias, e eles não ficam dentro da função wrrite()
# O carregamento de dados deve ser feito em funções, pois assim é possivel utilizar armazenamento em cache para agilizar a amostragem de dados
# É possivel intregrar o streaamlit com ferramentas de gráficos como matplotlib e ploty.express, mas os gráficos devem ser montados a parte e apenas exibidos com funções proproias do streamlit
# para o matplotlib a função é pyplot, para o plotly.express é plotly_chart
# A função multiselect cria uma caixa de seleção para varios itens, é necessario passar um texto e os dados que podem ser selecionados

#importação

import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf

# funções de carregamento de dados
# acao = st.text_input("Digite uma ação que deseja verificar: ")

@st.cache_data # Esse decorador(@st.cache_data), atribui um cache para a fuinção logo abaixo, fazendo o armazenamento das informações dentro desse cache, permitindo assim uma otimização
def carregarDados(empresas):
    texto_tickers = " ".join(empresas) # Estou juntando a lista de empresas em uma unica string e as separando com um espaço
    dadosAcao = yf.Tickers(texto_tickers) # Falando especificamente da biblioteca yfinance, ela pega os dados de investimento considerando os EUA, portanto para passar algum dado brasileiro é necessario passar: (o nome da ação.SA), pois isso indica a ação feita em São Paulo
    cotacoesAcao = dadosAcao.history(period="1d", start="2010-01-01", end="2024-07-01") # a função history() coleta as ações de uma dada empresa em um certo periodo dentro de um intervalo de tempo
    cotacoesAcao = cotacoesAcao["Close"] # Seleciona apenas a coluna "close" utilizando o pandas 
    return cotacoesAcao


acao = ["ITUB4.SA", "PETR4.SA", "MGlU3.SA", "VALE3.SA"]
#Visualização dos dados

resultadoAcao = carregarDados(acao)
listaDeAcoes = st.multiselect("Selecione as ações desejadas: ", resultadoAcao.columns)
print(listaDeAcoes)

if listaDeAcoes: # Se a lista de ações estiver com um aseleção
    resultadoAcao = resultadoAcao[listaDeAcoes] # O resultado da coleta dos dados == a ação selecionada da lista
    if len(listaDeAcoes) == 1: #Se nhouver apenas um dado selecionado na lista
        acao_unica = listaDeAcoes[0] # capture o indice zero e coloque na variavel
        resultadoAcao = resultadoAcao.rename(columns= {acao_unica: "Close"}) #Renomeie esse indice para "Close"
       

st.write(f""" 
O gráfico abaixo mostra os dados das ações: {listaDeAcoes} entre os anos de 2010 á 2024
""") # é possivel formatar textos como mardown no streamlit


st.line_chart(resultadoAcao) # Passando apenas o parametro data o streamlit tenta alocar os eixos automaticamente

st.dataframe(resultadoAcao)
