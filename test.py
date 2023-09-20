import matplotlib.pyplot as plt
import pandas as pd

# Dados de número de contratos para empresas de Pequeno Porte ao longo dos anos
data = {
    'ano': [2018, 2019, 2020, 2021, 2022],
    'acessos': [831999.0, 1170908.0, 1678990.0, 2691340.0, 2945431.0]
}

# Criar um DataFrame com os dados
df = pd.DataFrame(data)

# Calcular a taxa de crescimento anual média
df['taxa_crescimento'] = df['acessos'].pct_change() * 100  # em percentagem

# Calcular o crescimento acumulado ao longo dos anos
df['crescimento_acumulado'] = df['acessos'].pct_change(
    periods=4) * 100  # em percentagem

# Exibir os resultados
print(df)


# Dados de taxa de crescimento em percentual
# Excluímos o primeiro ano, pois a taxa é indefinida para ele
taxa_crescimento = df['taxa_crescimento'].values[1:]
anos = df['ano'].values[1:]  # Excluímos o primeiro ano

# Gráfico de barras para mostrar a taxa de crescimento em cada ano
plt.figure(figsize=(10, 6))
plt.bar(anos, taxa_crescimento, color='skyblue')
plt.xlabel('Ano')
plt.ylabel('Taxa de Crescimento (%)')
plt.title('Taxa de Crescimento Anual dos Contratos para Empresas de Pequeno Porte (2019 a 2022)')
plt.grid(True)

# Adicionar rótulos com os valores de crescimento em cada barra
for i in range(len(anos)):
    plt.text(anos[i], taxa_crescimento[i] + 0.2,
             f'{taxa_crescimento[i]:.2f}%', ha='center')

plt.show()
