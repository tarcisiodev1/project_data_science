import pandas as pd
import matplotlib.pyplot as plt

# URL do CSV
url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"

# Carregar os dados do CSV em um DataFrame
df = pd.read_csv(url)

# Escolher os dados mais recentes (ano 2022)
dados_mais_recentes = df[df['ano'] == 2022]

# Agrupar os dados por tecnologia e contar os acessos
dados_distribuicao_atual = dados_mais_recentes.groupby(
    'tecnologia')['acessos'].sum().reset_index()

# Ordenar as tecnologias pelo número de acessos
dados_distribuicao_atual = dados_distribuicao_atual.sort_values(
    by='acessos', ascending=False)

# Pegar as 6 principais tecnologias
principais_tecnologias = dados_distribuicao_atual.head(6)

# Somar os acessos das demais tecnologias
outros_acessos = dados_distribuicao_atual.iloc[6:]['acessos'].sum()

# Criar uma nova linha para representar as demais tecnologias
outros_tecnologias = pd.DataFrame(
    {'tecnologia': ['Outras Tecnologias'], 'acessos': [outros_acessos]})

# Juntar as 6 principais tecnologias com a linha das demais
dados_final = pd.concat([principais_tecnologias, outros_tecnologias])

# Gráfico para visualizar a distribuição atual de banda larga
plt.figure(figsize=(8, 8))
plt.pie(dados_final['acessos'], labels=dados_final['tecnologia'],
        autopct='%1.1f%%', startangle=140)
plt.title('Distribuição Atual de Banda Larga')
# Escrever os dados gerados para um arquivo CSV
dados_final.to_csv('dados_gerados.csv', index=False)

plt.show()
