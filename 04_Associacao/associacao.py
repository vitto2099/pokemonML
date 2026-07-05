import pandas as pd
import pickle
from mlxtend.frequent_patterns import apriori, association_rules

print("Carregando base normalizada...")
df_norm = pd.read_csv('../pokemonNormalizado.csv')

# Obter a lista de tipos disponíveis (baseado nas colunas type1_)
tipos = [col.replace('type1_', '') for col in df_norm.columns if col.startswith('type1_')]

# Criar um novo DataFrame unificando os tipos (independente se é type1 ou type2)
df_tipos = pd.DataFrame()
for t in tipos:
    col1 = f'type1_{t}'
    col2 = f'type2_{t}'
    
    # Se o Pokémon tiver o tipo como primário OU secundário, marca como True
    if col2 in df_norm.columns:
        df_tipos[t] = df_norm[col1].astype(bool) | df_norm[col2].astype(bool)
    else:
        df_tipos[t] = df_norm[col1].astype(bool)

print("\n--- Gerando Regras de Associação (Apriori) ---")
# Fase 1: Encontrar conjuntos de itens frequentes (Suporte mínimo = 0.01 ou 1%)
frequent_itemsets = apriori(df_tipos, min_support=0.01, use_colnames=True)

# Fase 2: Gerar as regras (Confiança mínima = 0.20 ou 20%)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.20)

# Ordenar as regras com Lift mais alto
rules = rules.sort_values(by='lift', ascending=False)

# Exibir as 10 melhores regras
print("\n=== TOP 10 REGRAS DE ASSOCIAÇÃO (Ordenadas por Lift) ===")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))

# Salvar as regras geradas
with open('regras_associacao.pkl', 'wb') as f:
    pickle.dump(rules, f)

print("\nRegras salvas como regras_associacao.pkl")
