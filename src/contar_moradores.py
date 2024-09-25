import pandas as pd

# Carregar os dados do arquivo CSV
dados = pd.read_excel('dados.xlsx')

# Contar o número de moradores por município
contagem_moradores = dados['MUNICÍPIO'].value_counts().reset_index()
contagem_moradores.columns = ['MUNICÍPIO', 'TOTAL_MORADORES']

# Salvar o resultado em um novo arquivo CSV
contagem_moradores.to_csv('contagem_moradores_por_cidade.csv', index=False)

print("A contagem de moradores por cidade foi salva em 'contagem_moradores_por_cidade.csv'.")
