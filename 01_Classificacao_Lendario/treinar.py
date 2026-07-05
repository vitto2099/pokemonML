import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
print('Carregando bases...')
X = pd.read_csv('../../pokemonNormalizado.csv')
df_original = pd.read_csv('../../pokemon.csv')
y = df_original['is_legendary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)
print(f'Base original dividida: {len(X_train)} para treino, {len(X_test)} para teste.')
smote = SMOTE()
X_train, y_train = smote.fit_resample(X_train, y_train)
print(f'Após o SMOTE, a base de treino ficou com {len(X_train)} registros (balanceada).')
resultados = {}
print('\n--- Treinando KNN ---')
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
acc_knn = accuracy_score(y_test, y_pred_knn)
resultados['KNN'] = acc_knn
print(f'Acurácia KNN: {acc_knn:.4f}')
with open('knn_lendario.pkl', 'wb') as f:
    pickle.dump(knn, f)
print('\n--- Treinando Naive Bayes ---')
nb = GaussianNB()
nb.fit(X_train, y_train)
y_pred_nb = nb.predict(X_test)
acc_nb = accuracy_score(y_test, y_pred_nb)
resultados['Naive Bayes'] = acc_nb
print(f'Acurácia Naive Bayes: {acc_nb:.4f}')
with open('naive_bayes_lendario.pkl', 'wb') as f:
    pickle.dump(nb, f)
print('\n--- Treinando Rede Neural ---')
mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000)
mlp.fit(X_train, y_train)
y_pred_mlp = mlp.predict(X_test)
acc_mlp = accuracy_score(y_test, y_pred_mlp)
resultados['Rede Neural'] = acc_mlp
print(f'Acurácia Rede Neural: {acc_mlp:.4f}')
with open('mlp_lendario.pkl', 'wb') as f:
    pickle.dump(mlp, f)
print('\n=== RESUMO DAS MÉTRICAS ===')
print('KNN Classification Report:')
print(classification_report(y_test, y_pred_knn))
print('Naive Bayes Classification Report:')
print(classification_report(y_test, y_pred_nb))
print('Rede Neural Classification Report:')
print(classification_report(y_test, y_pred_mlp))
print('Finalizado e arquivos .pkl gerados com sucesso!')
