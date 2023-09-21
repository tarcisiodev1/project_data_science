import pandas as pd
import matplotlib.pyplot as plt

# URL do CSV
url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"

# Carregar os dados do CSV em um DataFrame
df = pd.read_csv(url)

# Ajuste dos valores para acessos por milhão
df['acessos_por_milhao'] = df['acessos'] / 1000000  # Convertendo para milhões

# Agrupar os dados por tecnologia e porte da empresa, somando os acessos por milhão
dados_distribuicao_acessos = df.groupby(['tecnologia', 'porte_empresa'])[
    'acessos_por_milhao'].sum().reset_index()

# Filtrar as 4 maiores tecnologias de cada porte
maiores_tecnologias = dados_distribuicao_acessos.groupby('porte_empresa').apply(
    lambda x: x.nlargest(4, 'acessos_por_milhao')).reset_index(drop=True)

# Gráfico para visualizar a distribuição dos acessos por tecnologia e porte da empresa
plt.figure(figsize=(12, 6))
cores = plt.cm.tab20.colors
for i, (tech, group) in enumerate(maiores_tecnologias.groupby('tecnologia')):
    plt.bar(group['porte_empresa'], group['acessos_por_milhao'],
            label=tech, color=cores[i])

plt.xlabel('Porte da Empresa')
plt.ylabel('Acessos por Milhão')
plt.title('Distribuição de Acessos por Tecnologia e Porte da Empresa')
plt.legend()
plt.show()
