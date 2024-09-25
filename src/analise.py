import pandas as pd
import matplotlib.pyplot as plt

# Passo 1: Coletar Dados
sus_data = pd.read_excel('dados.xlsx')
mortalidade_data = pd.read_excel('mortalidade_infantil.xlsx')

# Normalizar nomes das colunas
sus_data.columns = sus_data.columns.str.strip()
mortalidade_data.columns = mortalidade_data.columns.str.strip()

# Renomear coluna 'Local' para 'MUNICÍPIO' em mortalidade_data
mortalidade_data.rename(columns={'Local': 'MUNICÍPIO'}, inplace=True)

# Passo 2: Unir os Dados
merged_data = pd.merge(sus_data, mortalidade_data, on='MUNICÍPIO', how='left')

# Passo 3: Definir Indicadores alternativos
# Calcular o número de atendimentos por município
atendimentos_por_municipio = sus_data.groupby('MUNICÍPIO').size()

# Passo 4: Visualização
# Agora vamos plotar diretamente do objeto Series gerado pelo groupby
plt.figure(figsize=(10, 6))
# Certifique-se de que o index (MUNICÍPIO) e os valores (count) estão corretos
atendimentos_por_municipio.plot(kind='bar', color='blue', label='Atendimentos no SUS')
plt.xticks(rotation=45)
plt.ylabel('Número de Atendimentos')
plt.title('Número de Atendimentos pelo SUS por Município')
plt.legend()
plt.tight_layout()
plt.show()
