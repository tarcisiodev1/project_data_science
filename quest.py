import pandas as pd
import matplotlib.pyplot as plt

# URL do CSV
url = "https://gist.githubusercontent.com/adolfoguimaraes/7202a4b356d485ded9e5ce9df953c936/raw/f01e392bdc9af84a501f895abfb36092505f7231/anatel_bandalarga_capitais.csv"

# Carregar os dados do CSV em um DataFrame
df = pd.read_csv(url)

# Agrupar os dados por tecnologia e porte da empresa, somando os acessos
dados_distribuicao_acessos = df.groupby(['tecnologia', 'porte_empresa'])[
    'acessos'].sum().reset_index()

# Gráfico para visualizar a distribuição dos acessos
plt.figure(figsize=(12, 6))
for i, (tech, group) in enumerate(dados_distribuicao_acessos.groupby('tecnologia')):
    plt.bar(group['porte_empresa'], group['acessos'], label=tech)

plt.xlabel('Porte da Empresa')
plt.ylabel('Número de Acessos')
plt.title('Distribuição de Acessos por Tecnologia e Porte da Empresa')
plt.legend()
plt.show()

# ----------------------------------- segunda pergunta ---------------------
# Escolhendo uma tecnologia e um porte de empresa específicos (exemplo: Fibra e Grande Porte)
tecnologia_escolhida = 'Fibra'
porte_empresa_escolhido = 'Grande Porte'

# Filtrar os dados para a tecnologia e porte de empresa escolhidos
dados_filtrados = df[(df['tecnologia'] == tecnologia_escolhida) & (
    df['porte_empresa'] == porte_empresa_escolhido)]

# Agrupar os dados por ano e somar os acessos
acessos_por_ano = dados_filtrados.groupby('ano')['acessos'].sum().reset_index()

# Gráfico para visualizar a evolução dos acessos ao longo dos anos
plt.figure(figsize=(10, 6))
plt.plot(acessos_por_ano['ano'], acessos_por_ano['acessos'], marker='o')
plt.xlabel('Ano')
plt.ylabel('Número de Acessos')
plt.title(
    f'Evolução dos Acessos para {tecnologia_escolhida} e {porte_empresa_escolhido} ao Longo dos Anos')
plt.grid(True)
plt.show()
# ----------------------------------- terceira pergunta ---------------------
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

# ----------------------------------- quarta pergunta ---------------------

# Escolher um porte de empresa específico (exemplo: Grande Porte)
porte_empresa_escolhido = 'Grande Porte'

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

# ----------------------------------- quinta pergunta ---------------------
# Escolher os dados mais recentes (ano 2022)
dados_mais_recentes = df[df['ano'] == 2022]

# Agrupar os dados por tecnologia e contar os acessos
dados_distribuicao_atual = dados_mais_recentes.groupby(
    'tecnologia')['acessos'].sum().reset_index()

# Gráfico para visualizar a distribuição atual de banda larga
plt.figure(figsize=(8, 8))
plt.pie(dados_distribuicao_atual['acessos'],
        labels=dados_distribuicao_atual['tecnologia'], autopct='%1.1f%%', startangle=140)
plt.title('Distribuição Atual de Banda Larga')
plt.show()
