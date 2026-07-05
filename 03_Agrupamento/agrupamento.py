import pandas as pd
import numpy as np
import pickle
from sklearn.cluster import KMeans
print('Carregando base...')
df_original = pd.read_csv('../pokemon.csv')
df_norm = pd.read_csv('../pokemonNormalizado.csv')
atributos_fisicos = ['attack', 'defense', 'height_m', 'hp', 'sp_attack', 'sp_defense', 'speed', 'weight_kg']
X_cluster = df_norm[atributos_fisicos]
X_cluster = X_cluster.fillna(X_cluster.mean())
print('\n--- Treinando K-Means (k=4) ---')
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=151, n_init=10)
kmeans.fit(X_cluster)
df_original['Cluster'] = kmeans.labels_
with open('kmeans_agrupamento.pkl', 'wb') as f:
    pickle.dump(kmeans, f)
print('Modelo K-Means salvo como kmeans_agrupamento.pkl')
df_original.to_pickle('pokemon_com_clusters.pkl')
print('Base com clusters salva como pokemon_com_clusters.pkl')
print('\n=== INTERPRETAÇÃO DOS GRUPOS (Média dos status originais por cluster) ===')
analise_cols = ['attack', 'defense', 'hp', 'sp_attack', 'sp_defense', 'speed', 'weight_kg']
analise = df_original.groupby('Cluster')[analise_cols].mean().round(2)
analise['Quantidade'] = df_original['Cluster'].value_counts()
print(analise)
print('\nConcluído!')
