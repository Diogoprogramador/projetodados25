1. Gráfico de dispersão - Preço versus número de quartos
Este gráfico de dispersão mostra a relação entre o preço do imóvel e o número de quartos. Ele usa cor (matiz) para representar diferentes regiões.
plt.figure(figsize=(10,6))
sns.scatterplot(x='Rooms', y='Price', data=df, hue='Regionname', palette='viridis')
plt.title('Preço vs Número de Quartos')
plt.xlabel('Número de Quartos')
plt.ylabel('Preço')
plt.tight_layout()
plt.show()

3. Gráfico de barras - Preço médio por subúrbio (10 principais)
Este gráfico de barras mostra os 10 principais subúrbios com os preços médios de imóveis mais altos.
plt.figure(figsize=(10,6))
mean_price_per_suburb = df.groupby('Suburb')['Price'].mean().sort_values(ascending=False).head(10)
mean_price_per_suburb.plot(kind='bar', color='c')
plt.title('Preço Médio por Subúrbio (Top 10)')
plt.xlabel('Subúrbio')
plt.ylabel('Preço Médio')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

3. Gráfico de dispersão - Preço versus tamanho do terreno
Este gráfico de dispersão ilustra a correlação entre o tamanho do terreno da propriedade e o seu preço.
plt.figure(figsize=(10,6))
sns.scatterplot(x='Landsize', y='Price', data=df, color='b', alpha=0.6)
plt.title('Preço vs Tamanho do Terreno')
plt.xlabel('Tamanho do Terreno (m²)')
plt.ylabel('Preço')
plt.tight_layout()
plt.show()

4. Gráfico de Linhas - Preço Médio ao Longo do Tempo
Este gráfico de linhas rastreia o preço médio da propriedade ao longo do tempo. O formato da data é ajustado para caber no conjunto de dados.
plt.figure(figsize=(10,6))
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df.set_index('Date', inplace=True)
df['Price'].resample('M').mean().plot(kind='line', color='r')
plt.title('Preço Médio de Imóveis ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço Médio')
plt.tight_layout()
plt.show()

Requisitos.
Python 3.x
Libraries: matplotlib, seaborn, pandas

Você pode instalar as bibliotecas necessárias usando o seguinte:
pip install matplotlib seaborn pandas

