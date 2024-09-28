from datetime import datetime
from pydantic import BaseModel, PositiveFloat, PositiveInt, EmailStr
from enum import Enum


class ProdutoEnum(str, Enum):
    """
    Modelo de dados para produtos.
    """
    produto1 = "Camisa"
    produto2 = "Calça"
    produto3 = "Meia"
    produto4 = "Cueca"
    produto5 = "Bone"

class Venda(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email: email do comprador
        data: data da compra
        valor: valor da compra
        quantidade: quantidade de produtos
        produto: categoria do produto
    """
    nome: str
    email: EmailStr
    genero: bool
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
    