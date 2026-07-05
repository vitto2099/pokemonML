import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
df = pd.read_csv('../pokemon.csv')
cols_to_drop = [col for col in df.columns if col.startswith('against_')]
cols_to_drop.extend(['is_legendary', 'japanese_name', 'name', 'pokedex_number', 'classfication', 'abilities', 'base_egg_steps', 'base_total', 'base_happiness', 'capture_rate', 'percentage_male', 'experience_growth', 'generation'])
df = df.drop(columns=cols_to_drop)
if 'height_m' in df.columns:
    df['height_m'] = df['height_m'].fillna(df['height_m'].median())
if 'weight_kg' in df.columns:
    df['weight_kg'] = df['weight_kg'].fillna(df['weight_kg'].median())
if 'type2' in df.columns:
    df['type2'] = df['type2'].fillna('None')
df = pd.get_dummies(df, columns=['type1', 'type2'])
colunas_numericas = ['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'height_m', 'weight_kg']
scaler = MinMaxScaler()
df[colunas_numericas] = scaler.fit_transform(df[colunas_numericas])
df.to_csv('pokemonNormalizado.csv', index=False)
print("Engenharia de dados concluída! Arquivo salvo em 'pokemonNormalizado.csv'")
