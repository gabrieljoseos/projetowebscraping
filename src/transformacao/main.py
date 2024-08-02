import pandas as pd
import sqlite3
from datetime import datetime
import os

# Caminho relativo dos arquivos
jsonl_file = os.path.join(os.path.dirname(__file__), '../../data/data.jsonl')
db_file = os.path.join(os.path.dirname(__file__), '../../data/quotes.db')

# Verificar se o arquivo JSONL existe
if not os.path.exists(jsonl_file):
    raise FileNotFoundError(f"O arquivo {jsonl_file} não foi encontrado.")

# ler o dado extraído
df = pd.read_json(jsonl_file, lines=True)

# Setar todas as colunas para aparecer
pd.options.display.max_columns = None

# Adicionar a coluna _soruce com valor fixo
df['_source'] = 'https://www.mercadolivre.com.br/ofertas?container_id=MLB779535-1'

# Adiconar a coluna data da coleta
df['date_scraping'] = datetime.now()

# Transformar dados
df['old_price'] = df['old_price'].fillna(0).astype(float)
df['new_price'] = df['new_price'].fillna(0).astype(float)

# Retirar o "Por" em seller e tirar tudo após % em desconto
df['seller'] = df['seller'].str.replace(r'^Por\s+', '', regex=True)
df['discount'] = df['discount'].str.replace(r'%.*', '%', regex=True)

# Seller nulo colocar MercadoLivre User e Discount nulo colocar Sem desconto
df['seller'] = df['seller'].fillna('MercadoLivre User')
df['discount'] = df['discount'].fillna('Sem desconto')

# Reordenar as colunas
new_order = ['name','seller','old_price','discount','new_price','_source','date_scraping']
df = df[new_order]

# Conectar BD
conn = sqlite3.connect(db_file)

# Salvar dataframe no banco de dados
df.to_sql('mercadolivre_cel', conn, if_exists='replace', index=False)

# Fechar conexção com o BD
conn.close()

# Imprimir DF
print(df.head())