import pandas as pd
import pickle
from mlxtend.frequent_patterns import apriori, association_rules
print('Carregando base normalizada...')
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
print('\n--- Gerando Regras de Associação (Apriori) ---')
frequent_itemsets = apriori(df_tipos, min_support=0.01, use_colnames=True)
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.2)
rules = rules.sort_values(by='lift', ascending=False)
print('\n=== TOP 10 REGRAS DE ASSOCIAÇÃO (Ordenadas por Lift) ===')
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))
with open('regras_associacao.pkl', 'wb') as f:
    pickle.dump(rules, f)
print('\nRegras salvas como regras_associacao.pkl')
