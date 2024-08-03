# Projeto de Web Scraping - Pipeline MercadoLivre
## Usando as bibliotecas Scrapy e Pandas para realizar o ETL
----
# Conceito

O conceito do projeto é passar por todas as etapas de ETL (Extract, Transform and Load), e para este projeto usei como exemplo o projeto do Professor <a href="https://www.linkedin.com/in/lucianovasconcelosf/"> Luciano Filho</a>, da isntituição Jornada de Dados, mostrando como utilizar as bibliotecas "Scrapy" e "Streamlit". </br>
O Scrapy por sua facilidade em executar uma pequena linha de código para extrair informações de sites, contendo request, midleware entre outros processos para uma boa extração. já o Streamlit por sua facilidade em criar um dashboard e mostrar as principais métricas de negócio.

## Passos
<div align="center">
  <img src="https://github.com/user-attachments/assets/1bcb6f08-3200-4482-9e95-ad34cd54b5f8"</img>
</div>
- Scrapy: Buscar as informações sobnre as pagína de promoções de celulares (mercadolivre.py) </br> 
<div class="warning">
   <em><b>"Para rodar:"</b> scrapy run mercadolivre -o ../data/jsonl</em>
</div>
- Pandas: Realizar a retirada de ruídos e realizar a formatação dos dados, upar em uma banco de dados (Neste caso utilizei o SQLite3 que já vem como padrão, mas em um projeto de larga escala poderia realizar uma automação salvando por dia em parquet e subi-lo no AWS S3)  (main.py) </br>
<div class="warning">
   <em><b>"Para rodar:"</b> python tranformacao/main.py</em>
</div>
- Streamlit: Realizar um dashboard básico (sem filtros), mostrando as principais métricas. (app.py) </br>
<div class="warning">
   <em><b>"Para rodar:"</b> streamlit run dashboard/app,py</em>
</div>

## Bibliotecas
Scrapy,
Pandas,
SQLite3,
Ploty,
Datetime e
OS.

## Banco de Dados
<div align="center">
  <img src="https://github.com/user-attachments/assets/117f8456-c929-4d31-b402-99ed3d559516"</img>
</div>
<div class="warning">
   <em>Utilizado o DBeaver para conectar ao banco de daods SQlite3 e realizar as consultas </em>
</div>
</br>

## DataViz

<div align="center">
  <img src="https://github.com/user-attachments/assets/4f925e6e-4cf3-4b01-a62e-2ea572caa329"</img>
</div>
<div align="center">
  <img src="https://github.com/user-attachments/assets/9b0284b8-8af0-4547-b924-b14326860f36"</img>
</div>
<div class="warning">
   <em>Utilizado o stremlit para realizar os cards e gráfico de barra, mas para o gráfico de torta foi realizado no ploty.</em>
</div>

---
Não pude publicar o aplicativo por um erro no meu IP, mas estou trabalhando para fazer a liberação. 
