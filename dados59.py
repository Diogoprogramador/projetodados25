import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV
file_path = 'melb_data.csv'  # Substitua pelo caminho do seu arquivo
df = pd.read_csv(file_path)

# Exibir as primeiras linhas do dataframe
print(df.head())

# Definir o estilo dos gráficos
sns.set(style='whitegrid')

# Gráfico de Dispersão - Preço vs Número de Quartos
plt.figure(figsize=(10,6))
sns.scatterplot(x='Rooms', y='Price', data=df, hue='Regionname', palette='viridis')
plt.title('Preço vs Número de Quartos')
plt.xlabel('Número de Quartos')
plt.ylabel('Preço')
plt.tight_layout()
plt.show()

# Gráfico de Barras - Preço Médio por Subúrbio
plt.figure(figsize=(10,6))
mean_price_per_suburb = df.groupby('Suburb')['Price'].mean().sort_values(ascending=False).head(10)
mean_price_per_suburb.plot(kind='bar', color='c')
plt.title('Preço Médio por Subúrbio (Top 10)')
plt.xlabel('Subúrbio')
plt.ylabel('Preço Médio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de Dispersão - Preço vs Tamanho do Terreno
plt.figure(figsize=(10,6))
sns.scatterplot(x='Landsize', y='Price', data=df, color='b', alpha=0.6)
plt.title('Preço vs Tamanho do Terreno')
plt.xlabel('Tamanho do Terreno (m²)')
plt.ylabel('Preço')
plt.tight_layout()
plt.show()

# Gráfico de Linha - Preço Médio ao Longo do Tempo
plt.figure(figsize=(10,6))
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')  # Ajuste o formato da data se necessário
df.set_index('Date', inplace=True)
df['Price'].resample('M').mean().plot(kind='line', color='r')
plt.title('Preço Médio de Imóveis ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço Médio')
plt.tight_layout()
plt.show()


