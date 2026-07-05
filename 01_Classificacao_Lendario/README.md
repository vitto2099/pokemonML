# Análise dos Modelos - PKL 1 (Prever Lendários)

Este documento apresenta a análise comparativa dos três modelos de *Machine Learning* treinados para prever se um Pokémon é Lendário (`1`) ou Não-Lendário (`0`).

A base de dados possui um forte desbalanceamento: a grande maioria dos Pokémons não são lendários. Isso reflete diretamente nas métricas dos algoritmos.

## 📊 Resultados e Métricas (Após SMOTE)

| Algoritmo | Acurácia Geral | Precisão (Lendários) | Recall (Lendários) |
| :--- | :--- | :--- | :--- |
| **KNN (K=5)** | 91% | 45% | 36% |
| **Redes Neurais (MLP)** | 93% | 62% | 36% |
| **Naive Bayes** | 26% | 9% | 86% |

---

## 🔍 Análise Comparativa (Com Base Balanceada)

Nesta versão final, aplicamos a técnica **SMOTE (Synthetic Minority Over-sampling Technique)**, recomendada no Slide 23/24 do professor, para balancear o número de Pokémons Lendários na base.

> [!IMPORTANT]
> **Por que o SMOTE foi aplicado no script de Treinamento e não na etapa 01 de Processamento?**
> A base de processamento `pokemonNormalizado.csv` servirá para os modelos do **PKL 1 (Lendários)** e **PKL 2 (Geração)**. Se duplicássemos os Lendários lá atrás, iríamos arruinar a distribuição das Gerações para o PKL 2. Além disso, as boas práticas de *Machine Learning* dizem que o balanceamento SMOTE só deve acontecer na **Base de Treino (X_train)**, após a divisão dos dados, para evitar que o modelo "trapaceie" testando em dados duplicados (Data Leakage).

### 1. K-Nearest Neighbors (KNN)
- **Como se saiu:** Com o SMOTE, o KNN parou de "se esconder" na classe majoritária. Sua acurácia geral caiu um pouquinho para 91%, mas ele melhorou absurdamente a detecção real de lendários (Recall subiu de ~15% para 36%).
- **Ponto Positivo:** O SMOTE forçou o KNN a prestar atenção aos Lendários no cálculo da distância euclidiana.
- **Ponto Negativo:** Ao tentar ser mais sensível aos lendários, ele passou a dar alguns alarmes falsos (a Precisão caiu de 100% para 45%).

### 2. Redes Neurais (MLP Classifier)
- **Como se saiu:** Novamente provou ser o modelo mais adaptável. A Rede Neural soube tirar ótimo proveito da base balanceada pelo SMOTE, atingindo uma Acurácia Geral de 93% e conseguindo o melhor equilíbrio entre Precisão (62%) e Recall (36%).
- **Ponto Positivo:** Ao contrário do KNN, a Rede Neural conseguiu manter uma precisão decente mesmo detectando mais lendários.

### 3. Naive Bayes (Gaussian)
- **Como se saiu:** Permanece péssimo com os dados One-Hot Encodados (Acurácia de 26%), mas com o SMOTE o seu Recall saltou para **86%**.
- **Ponto Positivo:** É o modelo que menos deixa passar Pokémons Lendários.
- **Ponto Negativo:** Para não deixar os lendários escaparem, ele chama quase toda a base de lendária (Precisão pífia de 9%). Continuamos descartando ele como o modelo ideal.

## 💡 Conclusão para Apresentação
Ao apresentar este PKL 1, mostre ao professor a importância de não confiar apenas na **Acurácia**. Sem o SMOTE, o KNN batia 93% de acurácia chutando que quase ninguém era Lendário. Com o SMOTE, os modelos ficaram **matematicamente mais justos**, dividindo melhor sua atenção entre as duas classes, resolvendo o problema de desbalanceamento de classes (Slide 23)!
