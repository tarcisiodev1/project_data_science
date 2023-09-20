import pandas as pd
import matplotlib.pyplot as plt

# URL do CSV
url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"

# Carregar os dados do CSV em um DataFrame
df = pd.read_csv(url)

# Escolhendo uma tecnologia e os portes de empresa específicos (exemplo: Fibra, Grande e Pequeno Porte)
tecnologia_escolhida = 'Fibra'
portes_empresas_escolhidos = ['Grande Porte', 'Pequeno Porte']

# Filtrar os dados para a tecnologia e portes de empresa escolhidos
dados_filtrados = df[(df['transmissao'] == tecnologia_escolhida) & (
    df['porte_empresa'].isin(portes_empresas_escolhidos))]

# Filtrar os dados para o intervalo de anos de 2018 a 2022
dados_filtrados_2018_2022 = dados_filtrados[dados_filtrados['ano'].between(
    2018, 2022)]

# Agrupar os dados por ano e porte de empresa, e somar os acessos
acessos_por_ano_porte = dados_filtrados_2018_2022.groupby(
    ['ano', 'porte_empresa'])['acessos'].sum().reset_index()

# Separar os dados por porte de empresa
dados_grande_porte = acessos_por_ano_porte[acessos_por_ano_porte['porte_empresa'] == 'Grande Porte']
dados_pequeno_porte = acessos_por_ano_porte[acessos_por_ano_porte['porte_empresa']
                                            == 'Pequeno Porte']

# Gráfico para visualizar a evolução dos acessos ao longo dos anos
plt.figure(figsize=(10, 6))
plt.plot(dados_grande_porte['ano'], dados_grande_porte['acessos'] /
         1e6, label='Grande Porte', marker='o')
plt.plot(dados_pequeno_porte['ano'], dados_pequeno_porte['acessos'] /
         1e6, label='Pequeno Porte', marker='o')
plt.xlabel('Ano')
plt.ylabel('Número de Acessos (em milhões)')
plt.title(
    f'Evolução dos Acessos para {tecnologia_escolhida} por Porte da Empresa (2018 a 2022)')
plt.legend(title='Tipo de Transmissão', loc='upper left')
plt.grid(True)
plt.xticks(range(2018, 2023))  # Configura os ticks para mostrar anos inteiros
plt.show()
