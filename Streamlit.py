import pandas as pd
import streamlit as st
import plotly.express as px

# ID do arquivo no Google Drive (substitua pelo seu ID)
file_id = '1-4VsPhqBBiq4gClop2pm6dDn3UqOphIz'

# Gerar a URL de download do Google Drive
url_projetos = f'https://drive.google.com/uc?export=download&id={file_id}'

# Carregar os dados da tabela Projetos diretamente do Google Drive
projetos = pd.read_csv(url_projetos, encoding='latin1', sep=";")

# Contar a quantidade de projetos por cliente
projetos_por_cliente = projetos.groupby('Cliente').size().reset_index(name='TotalProjetos')

# Título da página
st.title("Gráfico: Quantidade de Projetos por Cliente")

# Criar o gráfico de barras usando Plotly
fig = px.bar(projetos_por_cliente, x='Cliente', y='TotalProjetos',
             title="Quantidade de Projetos por Cliente",
             labels={'Cliente': 'Cliente', 'TotalProjetos': 'Total de Projetos'},
             color='TotalProjetos',
             height=600)

# Exibir o gráfico no Streamlit
st.plotly_chart(fig)

# Exibir a tabela com a contagem de projetos por cliente
st.dataframe(projetos_por_cliente)
