import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('../pokemon.csv')

# 1. Remover colunas irrelevantes e os alvos (is_legendary e generation)
cols_to_drop = [col for col in df.columns if col.startswith('against_')]
cols_to_drop.extend([
    'is_legendary', 'japanese_name', 'name', 'pokedex_number', 'classfication', 
    'abilities', 'base_egg_steps', 'base_total', 'base_happiness', 'capture_rate', 
    'percentage_male', 'experience_growth', 'generation'
])
df = df.drop(columns=cols_to_drop)

# 2. Tratamento de Valores Ausentes 
if 'height_m' in df.columns:
    df['height_m'] = df['height_m'].fillna(df['height_m'].median())
if 'weight_kg' in df.columns:
    df['weight_kg'] = df['weight_kg'].fillna(df['weight_kg'].median())
if 'type2' in df.columns:
    df['type2'] = df['type2'].fillna('None')

# 3. Codificação de Variáveis Categóricas (One-Hot Encoding)
# Transforma as variáveis categóricas nominais (type1 e type2) em numéricas binárias (0 e 1)
df = pd.get_dummies(df, columns=['type1', 'type2'])

# 4. Normalização de Escala (Normalization / Min-Max)
# Como ensinado nos slides, algoritmos baseados em instâncias (KNN) precisam das variáveis na mesma escala
colunas_numericas = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'height_m', 'weight_kg']
scaler = MinMaxScaler()
df[colunas_numericas] = scaler.fit_transform(df[colunas_numericas])

df.to_csv('pokemonNormalizado.csv', index=False)
print("Engenharia de dados concluída! Arquivo salvo em 'pokemonNormalizado.csv'")
