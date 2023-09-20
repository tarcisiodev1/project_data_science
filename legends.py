import pandas as pd

# URL do CSV
url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"

# Carregar os dados do CSV em um DataFrame
df = pd.read_csv(url)

# Criar uma lista para armazenar as legendas
legendas_list = []

# Obter as legendas para cada coluna
for coluna in df.columns:
    legendas = df[coluna].unique()
    legendas_list.append(
        {'Coluna': coluna, 'Legendas': ', '.join(map(str, legendas))})

# Criar um DataFrame a partir da lista
legendas_df = pd.DataFrame(legendas_list)

# Exportar para CSV
caminho_csv_legendas = "legendas_anatel_bandalarga.csv"
legendas_df.to_csv(caminho_csv_legendas, index=False)
print(f'Legendas exportadas para: {caminho_csv_legendas}')
