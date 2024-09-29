import streamlit as st
from datetime import datetime, time
from pydantic import ValidationError
from modules.database import salvar_no_banco
from modules.venda import Venda

def main():

    st.title("Sistema de CRM e Vendas da ZapFlow = Frontend Simples")
    nome = st.text_input("Nome do usuário")
    genero = st.chat_input("Genero")
    email = st.text_input("Email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9,0))
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de produtos", min_value=1, step=1)
    produto  = st.selectbox("Campo de seleção para escolher o produto vendido.", ["Camisa", "Calça", "Meia", "Cueca", "Bone"])

    if st.button("Salvar"):

        try:
            data_hora = datetime.combine(data, hora)

            venda = Venda(
                nome = nome,
                genero = genero,
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
            )
            st.write(venda)
            salvar_no_banco(venda)
        except ValidationError as e:
            st.error(f"Deu erro {e}")

if __name__=="__main__":
    main()