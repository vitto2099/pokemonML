import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import numpy as np

print("Carregando regras de associação...")
rules = pickle.load(open('regras_associacao.pkl', 'rb'))

sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12})

# 1. Gráfico de Dispersão (Support vs Confidence)
plt.figure(figsize=(10, 6))
# Mapear o Lift para o tamanho e cor das bolinhas
sns.scatterplot(
    data=rules, 
    x='support', 
    y='confidence', 
    size='lift',
    hue='lift',
    sizes=(50, 400),
    palette='viridis',
    alpha=0.8
)
plt.title('Regras de Associação: Suporte vs Confiança', fontsize=16, pad=15)
plt.xlabel('Suporte (Frequência da Regra)', fontsize=14)
plt.ylabel('Confiança (Certeza da Regra)', fontsize=14)

# Melhorar a legenda do Lift
plt.legend(title='Lift (Força)', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('grafico_suporte_confianca.png', dpi=300)
plt.close()

# 2. Top 10 Regras por Lift (Gráfico de Barras Horizontal)
top_10_lift = rules.head(10).copy()

# Criar nomes legíveis para o gráfico
def formatar_regra(row):
    ant = list(row['antecedents'])[0].capitalize()
    con = list(row['consequents'])[0].capitalize()
    return f"{ant} -> {con}"

top_10_lift['Regra'] = top_10_lift.apply(formatar_regra, axis=1)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_10_lift,
    x='lift',
    y='Regra',
    hue='Regra',
    palette='magma',
    legend=False
)




plt.title('Top 10 Padrões Mais Fortes (por Lift)\n(Voador/Normal e Venenoso/Grama em destaque)', fontsize=16, pad=15)
plt.xlabel('Valor do Lift (Quão maior a chance de ocorrerem juntos)', fontsize=14)
plt.ylabel('Regra (Se X -> Então Y)', fontsize=14)
plt.tight_layout()
plt.savefig('grafico_top10_lift.png', dpi=300)
plt.close()

# 3. Heatmap de Co-ocorrência (para achar as lacunas, ex: Fogo e Água)
print("Gerando matriz de co-ocorrência de tipos...")
df_norm = pd.read_csv('../pokemonNormalizado.csv')

tipos = [col.replace('type1_', '') for col in df_norm.columns if col.startswith('type1_')]

df_tipos = pd.DataFrame()
for t in tipos:
    col1 = f'type1_{t}'
    col2 = f'type2_{t}'
    if col2 in df_norm.columns:
        df_tipos[t] = df_norm[col1].astype(bool) | df_norm[col2].astype(bool)
    else:
        df_tipos[t] = df_norm[col1].astype(bool)

co_matrix = df_tipos.astype(int).T.dot(df_tipos.astype(int))
for t in co_matrix.columns:
    co_matrix.loc[t, t] = 0 # Zerar a diagonal para focar nos cruzamentos

plt.figure(figsize=(12, 10))
sns.heatmap(
    co_matrix, 
    cmap='Blues', 
    annot=True, 
    fmt="d",
    linewidths=.5,
    cbar_kws={'label': 'Número de Pokémons com ambos os tipos'}
)
plt.title('Mapa de Calor: Cruzamento de Tipos\n(Identificando Lacunas e Combinações Raras - ex: Fogo e Água)', fontsize=16, pad=15)
plt.xlabel('Tipo', fontsize=14)
plt.ylabel('Tipo', fontsize=14)
plt.tight_layout()
plt.savefig('grafico_heatmap_lacunas.png', dpi=300)
plt.close()

print("Gráficos de associação gerados com sucesso!")
