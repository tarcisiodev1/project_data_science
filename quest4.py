import pandas as pd
import matplotlib.pyplot as plt

# URL do CSV
url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"

# Carregar os dados do CSV em um DataFrame
df = pd.read_csv(url)

# Escolher um porte de empresa específico (exemplo: Pequeno Porte)
porte_empresa_escolhido = 'Pequeno Porte'

# Filtrar os dados para o porte de empresa escolhido
dados_filtrados = df[df['porte_empresa'] == porte_empresa_escolhido]

# Agrupar os dados por ano e somar os acessos
contratos_por_ano = dados_filtrados.groupby(
    'ano')['acessos'].sum().reset_index()

# Gráfico para visualizar a evolução do número de contratos para um porte específico
plt.figure(figsize=(10, 6))
plt.plot(contratos_por_ano['ano'], contratos_por_ano['acessos'], marker='o')
plt.xlabel('Ano')
plt.ylabel('Número de Contratos')
plt.title(
    f'Evolução do Número de Contratos para Empresas de {porte_empresa_escolhido} ao Longo dos Anos')
plt.grid(True)
plt.show()
