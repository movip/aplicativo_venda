import psycopg2
from psycopg2 import sql
from modules.venda import Venda
import streamlit as st
from dotenv import load_dotenv
import time
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_NAME = os.getenv("DB_NAME", "venda")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "admin")

def salvar_no_banco(dados: Venda):
    """
    Função para salvar no PostgreSQL com retry
    """
    retries = 5
    delay = 5

    for attempt in range(retries):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            cursor = conn.cursor()

            insert_query = sql.SQL(
                "INSERT INTO venda (nome, email, genero, data, valor, quantidade, produto) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            )
            cursor.execute(insert_query, (
                dados.nome,
                dados.email,
                dados.genero,
                dados.data,
                dados.valor,
                dados.quantidade,
                dados.produto.value
            ))
            conn.commit()
            cursor.close()
            conn.close()
            st.success("Dados salvos com sucesso no banco de dados!")
            break  # Sucesso, sai do loop
        except Exception as e:
            st.error(f"Erro ao salvar no banco de dados: {e}")
            if attempt < retries - 1:
                st.info(f"Repetindo em {delay} segundos...")
                time.sleep(delay)
            else:
                st.error("Falha ao conectar ao banco de dados após várias tentativas.")