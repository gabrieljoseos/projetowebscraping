import pandas as pd
import sqlite3
from datetime import datetime 

# ler o dado extraído
df = pd.read_json('../../../data/data.jsonl', lines=True)

# Setar todas aas colunas 
pd.options.display.max_columns = None

# Adicionar a coluna _soruce com valor fixo
df['_source'] = 'https://www.mercadolivre.com.br/ofertas?container_id=MLB779535-1'

# Adiconar a coluna data da coleta
df['date_scraping'] = datetime.now()

# Transformar dados
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_cents'] = df['old_price_cents'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_cents'] = df['new_price_cents'].fillna(0).astype(float)


# Adicionar coluna old_price e new_price com real e centavo
df['old_price'] = df['old_price_reais'] + df['old_price_cents'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_cents'] / 100

# Retirar o "Por" em seller
df['seller'] = df['seller'].str.replace(r'^Por\s+', '', regex=True)

# Seller nulo colocar MercadoLivre
df['seller'] = df['seller'].fillna('MercadoLivre User')

# Eliminar colunas indesejadas  
df.drop(columns=['old_price_reais','old_price_cents','new_price_reais','new_price_cents'])

# Reordenar as colunas
new_order = ['name','seller','old_price','discount','new_price','_source','date_scraping']
df = df[new_order]