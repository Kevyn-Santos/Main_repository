from fastapi import FastAPI
import indb

app = FastAPI()
produto = indb.gerarProdutos()

@app.get('/')
def mostrarProduto():
    return {'produtos cadastrados': produto}