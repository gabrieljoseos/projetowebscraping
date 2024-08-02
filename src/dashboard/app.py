import streamlit as st
import pandas as pd
import sqlite3
import os

# ler os dados do SQLite3
db_file = os.path.join(os.path.dirname(__file__), '../../data/quotes.db') #Diretório do Banco de Dados Salvo
conn = sqlite3.connect(db_file) # Abrir conexão
df = pd.read_sql_query("SELECT * FROM mercadolivre_cel", conn)
conn.close() # Fechar conexão

# Tituto Streamlit
st.title("Dashboard - Celulares Promo 01/08/2024")
st.subheader("Principais KPIs")
st.write(df)

# colunas
col1,col2,col3 = st.columns(3)
col4,col5 = st.columns(2)

# Coluna 1,2 e 3
total_prodct = df.shape[0] # Quantidade de produtos a venda
col1.metric(label='Quantidade de produtos à venda', value=total_prodct)

# Quantidade de Vendedores
total_sellers = df['seller'].astype(str).unique()  # Obtém os vendedores únicos
total_sellers_count = len(total_sellers)  # Conta o número de vendedores únicos      
col2.metric(label='Quantidade de vendedores', value=total_sellers_count)

# Média de preço
mean_price = df['new_price'].mean().round(3)
col3.metric(label='Média de Preço', value=mean_price)

# Quais os vendedores mais encontrados em todas as páginas
st.subheader('Quais os vendedores mais encontrados em todas as páginas')
col1,col2 = st.columns([4, 2]) # Colar gráfico entra as colunas um e dois
top_5_sellers = df['seller'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_5_sellers)
col2.write(top_5_sellers)

# Média de preço por vendedor
st.subheader('Média de preço por vendedor')
col1,col2 = st.columns([4, 2]) # Colar gráfico entra as colunas um e dois
meanprice_by_seller = df.groupby('seller')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(meanprice_by_seller)
col2.write(meanprice_by_seller)

# Maior disconto aplicado por 