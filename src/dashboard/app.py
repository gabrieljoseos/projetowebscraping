import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3
import os

# ler os dados do SQLite3
db_file = os.path.join(os.path.dirname(__file__), '../../data/quotes.db') #Diretório do Banco de Dados Salvo
conn = sqlite3.connect(db_file) # Abrir conexão
df = pd.read_sql_query("SELECT * FROM mercadolivre_cel", conn)
conn.close() # Fechar conexão

# Configuração de página
st.set_page_config(page_title='Promoção Celular - ML', layout='wide', menu_items={"about": "https//www.linkedin.com/in/gabrieljos"})
# Tituto Streamlit
st.header("Dashboard - Celulares Promo 02/08/2024", divider='blue')
st.subheader("Principais KPIs", divider='grey')

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
mean_price = df['new_price'].mean().round(2)
col3.metric(label='Média de Preço', value=mean_price)
###########

# Análises por vendedor
st.subheader("Análises por Vendedores", divider='grey')
# Quais os vendedores mais encontrados em todas as páginas
st.subheader('Quais os vendedores mais encontrados em todas as páginas')
col1, col2 = st.columns([4, 2])  # Colar gráfico entra as colunas um e dois
# Cálculo da distribuição de vendedores
vendor_distribution = df['seller'].value_counts().reset_index()
vendor_distribution.columns = ['Seller', 'Count']
# Agrupar os menores valores em "Outros"
threshold = 5  # Define o número mínimo de itens para não ser agrupado como "Outros"
top_vendors = vendor_distribution[vendor_distribution['Count'] > threshold]
other_vendors = vendor_distribution[vendor_distribution['Count'] <= threshold]
if not other_vendors.empty:
    other_count = other_vendors['Count'].sum()
    other_df = pd.DataFrame({'Seller': ['Outros'], 'Count': [other_count]})
    top_vendors = pd.concat([top_vendors, other_df], ignore_index=True)
# Criar o gráfico de pizza usando Plotly
fig = px.pie(top_vendors, names='Seller', values='Count', title='Distribuição de Produtos por Vendedor')
# Gráficos nas colunas
sellers_count = df['seller'].value_counts().sort_values(ascending=False)
col1.bar_chart(sellers_count, horizontal=True, color="#ff7f0e")
col2.plotly_chart(fig)

# Média de preço por vendedor
st.subheader('Média de preço por vendedor')
col1,col2 = st.columns([4, 2]) # Colar gráfico entra as colunas um e dois
df_non_zero_prices = df[df['new_price'] > 0.1]
meanprice_by_seller = df_non_zero_prices.groupby('seller')['new_price'].mean().sort_values(ascending=False)
# Gráficos nas colunas
col1.bar_chart(meanprice_by_seller)
col2.write(meanprice_by_seller)

# Média de desconto 
col1,col2 = st.columns([4, 2])
col1.subheader('Melhores descontos aplicados por vendedor')
df2 = df[['seller','discount']]
df2 = df2 = df2[df2['discount'] != 'Sem desconto']
df2['discount'] = df2['discount'].str.replace(r'%', '', regex=True).astype(float)
bests_discount = df2.groupby('seller')['discount'].max().sort_values(ascending=False)
# Gráficos nas colunas
col1.bar_chart(bests_discount, horizontal=True)
col2.write(bests_discount)

##########################
# Análise de Produtos Populares
st.subheader('Análise de Produtos Populares', divider='grey')

# Contar a frequência de produtos
product_counts = df['name'].value_counts()
most_popular_products = product_counts.head(10)
# Filtrar DataFrame para produtos populares
popular_products_df = df[df['name'].isin(most_popular_products.index)]
# Calcular média de descontos e preços para produtos populares
# Remover caracteres não numéricos e converter para float
popular_products_df['discount'] = popular_products_df['discount'].replace('Sem desconto', '0%')
popular_products_df['discount'] = popular_products_df['discount'].str.extract(r'(\d+)', expand=False)  # Extrair apenas números
popular_products_df['discount'] = pd.to_numeric(popular_products_df['discount'], errors='coerce')  # Converter para float, forçando erros a NaN
average_discounts = popular_products_df.groupby('name')['discount'].mean()
average_prices = popular_products_df.groupby('name')['new_price'].mean()
# Gráficos nas colunas
col1, col2 = st.columns([4, 2])
col1.subheader('Produtos Mais Populares')
col1.bar_chart(most_popular_products, horizontal=True, color=["#ff7f0e"])
col2.write(most_popular_products)

# Exibir média de descontos para produtos populares
col1.subheader('Média de Descontos para Produtos Populares')
# Gráficos nas colunas
col1.bar_chart(average_discounts)
col2.subheader('Média de desconto')
col2.write(average_discounts) # Mostrar tabelas de média de descontos e preços
