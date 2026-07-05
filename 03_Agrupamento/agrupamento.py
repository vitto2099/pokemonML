import pandas as pd
import numpy as np
import pickle
from sklearn.cluster import KMeans

# Carregar os dados processados e normalizados
print("Carregando base...")
df_original = pd.read_csv('../pokemon.csv')
df_norm = pd.read_csv('../pokemonNormalizado.csv')

# Selecionar os atributos físicos e de combate (contínuos)
# Estas são as colunas normalizadas que representam as características físicas
atributos_fisicos = ['attack', 'defense', 'height_m', 'hp', 'sp_attack', 'sp_defense', 'speed', 'weight_kg']
X_cluster = df_norm[atributos_fisicos]

# Como tem valores nulos preenchidos anteriormente (se houver algum que não foi tratado), remover ou preencher
X_cluster = X_cluster.fillna(X_cluster.mean())

# Treinar o K-Means++
# Escolhemos k=4 como um exemplo equilibrado para ver diferentes perfis de Pokémon
print("\n--- Treinando K-Means (k=4) ---")
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=151, n_init=10)
kmeans.fit(X_cluster)

# Adicionar a coluna de cluster no dataframe original para análise
df_original['Cluster'] = kmeans.labels_

# Salvar o modelo em PKL
with open('kmeans_agrupamento.pkl', 'wb') as f:
    pickle.dump(kmeans, f)
print("Modelo K-Means salvo como kmeans_agrupamento.pkl")

# Salvar a base final com a classificação do cluster em pkl (conforme pedido no slide 27)
df_original.to_pickle('pokemon_com_clusters.pkl')
print("Base com clusters salva como pokemon_com_clusters.pkl")

# --- Interpretação dos Grupos ---
print("\n=== INTERPRETAÇÃO DOS GRUPOS (Média dos status originais por cluster) ===")
# Pegar a média das características de combate na base ORIGINAL para interpretação
analise_cols = ['attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed', 'weight_kg']
analise = df_original.groupby('Cluster')[analise_cols].mean().round(2)
analise['Quantidade'] = df_original['Cluster'].value_counts()
print(analise)

print("\nConcluído!")
