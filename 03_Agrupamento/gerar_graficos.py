import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
print("Carregando base com clusters...")
df = pd.read_pickle('pokemon_com_clusters.pkl')
# Definir paleta de cores para os clusters
cores = {0: '#E74C3C', 1: '#3498DB', 2: '#2ECC71', 3: '#F1C40F'}
nomes_clusters = {
    0: 'Grupo 4: Pesos-Pesados/Lendários',1: 'Grupo 1: Estágios Iniciais',2: 'Grupo 3: Tanques Defensivos',3: 'Grupo 2: Atacantes Rápidos'
}
# Para fins visuais, vamos mapear pro nome bonito
df['Perfil'] = df['Cluster'].map(nomes_clusters)
# Configurações gerais
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})
# 1. Gráfico de Dispersão (Attack vs Speed)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, x='speed', y='attack', hue='Perfil', palette='deep',alpha=0.7,s=60
)
plt.title('Agrupamento K-Means: Ataque vs Velocidade', fontsize=16, pad=15)
plt.xlabel('Velocidade (Speed)', fontsize=14)
plt.ylabel('Ataque (Attack)', fontsize=14)
plt.legend(title='Perfis Identificados', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('grafico_ataque_velocidade.png', dpi=300)
plt.close()
# 2. Gráfico de Dispersão (Defense vs HP)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df, x='defense', y='hp', hue='Perfil', palette='deep',alpha=0.7,s=60
)
plt.title('Agrupamento K-Means: Defesa vs HP', fontsize=16, pad=15)
plt.xlabel('Defesa (Defense)', fontsize=14)
plt.ylabel('Pontos de Vida (HP)', fontsize=14)
plt.legend(title='Perfis Identificados', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('grafico_defesa_hp.png', dpi=300)
plt.close()
# 3. Gráfico de Contagem de Elementos
plt.figure(figsize=(8, 5))
ax = sns.countplot(data=df, y='Perfil', palette='deep', order=df['Perfil'].value_counts().index)
plt.title('Distribuição de Pokémon por Perfil', fontsize=16, pad=15)
plt.xlabel('Quantidade de Pokémon', fontsize=14)
plt.ylabel('')
# Adicionar números nas barras
for p in ax.patches:
    ax.annotate(f'{int(p.get_width())}', 
                (p.get_width() + 5, p.get_y() + p.get_height() / 2.), 
                ha='left', va='center', fontsize=12)
plt.tight_layout()
plt.savefig('grafico_distribuicao_clusters.png', dpi=300)
plt.close()
print("Gráficos de agrupamento gerados com sucesso!")
