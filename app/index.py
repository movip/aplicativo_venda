import streamlit as st
from datetime import datetime, time
from pydantic import ValidationError
from modules.database import salvar_no_banco
from modules.venda import Venda
import pandas as pd

# Dicionário com os valores dos produtos
produtos_valores = {
    "Camisa": 150,
    "Calça": 200,
    "Meia": 50,
    "Cueca": 70,
    "Bone": 175
}

def main():

    st.title("Sistema de CRM e Vendas - Frontend Simples")
    nome = st.text_input("Nome do Cliente")
    genero = st.selectbox("Gênero", ["Masculino", "Feminino"])
    email = st.text_input("Email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9,0))
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    
    # Seleção de produto e valor automaticamente ajustado
    produto = st.selectbox("Escolha o produto vendido", list(produtos_valores.keys()))

    # Pega o valor do produto selecionado no dicionário
    valor = produtos_valores[produto] * quantidade
    
    # Exibe o valor calculado
    st.write(f"Valor total: R$ {valor:.2f}")

    if st.button("Salvar"):
        try:
            data_hora = f'{data} {hora}'
            data_hora = pd.to_datetime(data_hora)

            venda = Venda(
                nome=nome,
                genero=genero,
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto
            )
            st.write(venda)
            salvar_no_banco(venda)
        except ValidationError as e:
            st.error(f"Deu erro: {e}")

if __name__ == "__main__":
    main()