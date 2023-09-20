# questao3.py
import pandas as pd
import matplotlib.pyplot as plt

# URL do CSV
url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"

# Carregar os dados do CSV em um DataFrame
df = pd.read_csv(url)

# Agrupar os dados por empresa, porte da empresa e somar os contratos
dados_contratos = df.groupby(['nome_empresa', 'porte_empresa'])[
    'acessos'].sum().reset_index()

# Escolher as empresas com maior número de contratos para cada porte
empresas_maior_contrato_pequeno = dados_contratos[dados_contratos['porte_empresa'] == 'Pequeno Porte'].nlargest(
    3, 'acessos')
empresas_maior_contrato_grande = dados_contratos[dados_contratos['porte_empresa'] == 'Grande Porte'].nlargest(
    3, 'acessos')

# Gráfico para visualizar o número de contratos por empresa e porte
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].bar(empresas_maior_contrato_pequeno['nome_empresa'],
            empresas_maior_contrato_pequeno['acessos'])
axes[0].set_xlabel('Empresas (Pequeno Porte)')
axes[0].set_ylabel('Número de Contratos')
axes[0].set_title('Empresas com Maior Número de Contratos (Pequeno Porte)')

axes[1].bar(empresas_maior_contrato_grande['nome_empresa'],
            empresas_maior_contrato_grande['acessos'], color='orange')
axes[1].set_xlabel('Empresas (Grande Porte)')
axes[1].set_ylabel('Número de Contratos')
axes[1].set_title('Empresas com Maior Número de Contratos (Grande Porte)')

plt.tight_layout()
plt.show()
