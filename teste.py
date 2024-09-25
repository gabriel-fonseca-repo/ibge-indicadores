import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
dados_sus = pd.read_csv("contagem_moradores_por_cidade.csv")  # Arquivo CSV com os dados de atendimento do SUS
dados_mortalidade = pd.read_csv("mortalidade_infantil.csv")  # Arquivo CSV com os dados de mortalidade infantil

# Padronizar os nomes dos municípios, se necessário
dados_sus['MUNICÍPIO'] = dados_sus['MUNICÍPIO'].str.upper()
dados_mortalidade['Local'] = dados_mortalidade['Local'].str.upper()

# Mesclar os dados
dados_mergidos = pd.merge(dados_sus, dados_mortalidade, left_on="MUNICÍPIO", right_on="Local", how="left")

# Limpar dados de mortalidade infantil e converter para float
dados_mergidos['Mortalidade Infantil'] = pd.to_numeric(dados_mergidos['Mortalidade Infantil'], errors='coerce')

# Calcular os indicadores
# Taxa de Mortalidade Infantil por 1000 moradores
dados_mergidos['Taxa Mortalidade Infantil por 1000'] = (dados_mergidos['Mortalidade Infantil'] / dados_mergidos['TOTAL_MORADORES']) * 1000
# Proporção de Mortalidade Infantil
dados_mergidos['Proporção Mortalidade'] = (dados_mergidos['Mortalidade Infantil'] / dados_mergidos['TOTAL_MORADORES']) * 100

# Ordenar os dados pela taxa de mortalidade e selecionar os top 10 municípios
dados_top10 = dados_mergidos.nlargest(10, 'Taxa Mortalidade Infantil por 1000')

# Plotar os dados
fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# Gráfico da Taxa de Mortalidade Infantil por 1000 Moradores
axes[0].bar(dados_top10['MUNICÍPIO'], dados_top10['Taxa Mortalidade Infantil por 1000'], color='skyblue')
axes[0].set_xlabel('Município')
axes[0].set_ylabel('Taxa de Mortalidade Infantil por 1000 Moradores')
axes[0].set_title('Top 10 Municípios com Maior Taxa de Mortalidade Infantil por 1000 Moradores')
axes[0].tick_params(axis='x', rotation=45)

# Gráfico da Proporção de Mortalidade Infantil
axes[1].bar(dados_top10['MUNICÍPIO'], dados_top10['Proporção Mortalidade'], color='lightgreen')
axes[1].set_xlabel('Município')
axes[1].set_ylabel('Proporção de Mortalidade Infantil (%)')
axes[1].set_title('Proporção de Mortalidade Infantil nos Top 10 Municípios com Maior Taxa')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
