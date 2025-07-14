# from typing import Union
from fastapi import FastAPI, Request, Form, File, UploadFile # importação dos módoulos para a construção da API, requisição e consumo de informações vindas de um formulario, sejam elas de texto ou arquivos
from fastapi.templating import Jinja2Templates as j2t # Importação do módulo para acessar a página HTML como template
from fastapi.responses import HTMLResponse # Importação do módulo que trata da resposta da API como HTML

# inicialização da API e pasta onde esta a pagina HTML
app = FastAPI() 
temp = j2t(directory= 'templates')

# Captura e renderização da página HTML
@app.get('/', response_class=HTMLResponse) # Na página 'raiz' receba uma requisição GET
def read_name(request: Request):
    return temp.TemplateResponse('main.html', {'request': request}) # Acesse o caminho onde esta o HTML e a partir da requisição(request) renderize e exiba a página

# Ação após o preenchimetno do formulário
@app.post('/enviar') # Na pagina 'enviar' receba uma rerquisição POST
def exibir(Nome: str = Form(...), Imagem: UploadFile = File(...)): # receba na função o nome e arquivos do formulario.(Importante que as variaveis tenham os mesmo nome dos elementos do formulario, pois a API os localiza pelo nome)
    return {'nome': Nome, 'Arquivo': Imagem.filename, 'Tipo de Dado': Imagem.content_type, 'tamanho do arquivo': Imagem.size} # Exiba como JSON o nome do usuario, o nome do arquivo, o tipo do arquivo, etc..







# vendas = {
#     1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
#     2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
#     3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
#     4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
#     5: {"item": "garrafão", "preco_unitario": 10, "quantidade": 3}
# }

# app.get('/')
# def root():
#     return 'API de teste'

# @app.get('/item/{item_id}')
# def item(item_id: int):
#     return vendas[item_id]

# @app.get('/all')
# def todos_itens():
#     count =0
#     while True:
#         count = count + 1
#         if count == len(vendas):
#             break
#         else:
#             return vendas