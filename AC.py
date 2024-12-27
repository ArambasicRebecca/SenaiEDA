import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Importando base de dados
df = pd.read_csv('sales_data_regional.csv')
print(df.head())
print(df.info())

# Exibir dados estatísticos descritivos
print(df.describe())
print(df.isnull().sum())

# Plotando Histograma
plt.hist(df['Quantidade'], bins=10, alpha=0.7)
plt.title('Distribuição de Quantidade Vendida')
plt.xlabel('Quantidade')
plt.ylabel('Frequência')
plt.show()

# Boxplot para Valores
sns.boxplot(x=df['Valor'])
plt.title('Distribuição de Valores de Venda')
plt.show()

# Correlação entre Quantidade e Valor
print(df[['Quantidade', 'Valor']].corr())

# Gráfico de Dispersão
sns.scatterplot(x='Quantidade', y='Valor', data=df)
plt.title('Relação entre Quantidade e Valor')
plt.show()

# Vendas por Região
vendas_regiao = df.groupby('Região')['Valor'].sum().sort_values(ascending=False)
print(vendas_regiao)

# Gráfico de Barras
vendas_regiao.plot(kind='bar', title='Vendas por Região', ylabel='Valor Total')
plt.show()
