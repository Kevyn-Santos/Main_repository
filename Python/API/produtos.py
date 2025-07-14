from pydantic import BaseModel

class produto(BaseModel):
    nome: str
    preço: float