# Análise dos Modelos - PKL 2 (Prever Geração)

Este documento apresenta a análise comparativa dos três modelos de *Machine Learning* treinados para tentar prever a Geração (1 a 7) de um Pokémon baseando-se em seus atributos (Ataque, Defesa, HP, etc. e Tipos).

## 📊 Resultados e Métricas (Após SMOTE)

A base foi dividida e aplicou-se SMOTE no conjunto de treino para garantir que o modelo não tendesse a focar apenas nas gerações maiores (como a Geração 5 e 1, que possuem mais Pokémon).

| Algoritmo | Acurácia Geral | F1-Score Médio |
| :--- | :--- | :--- |
| **Redes Neurais (MLP)** | 32% | 0.31 |
| **KNN (K=5)** | 27% | 0.25 |
| **Naive Bayes** | 24% | 0.18 |

---

## 🔍 Análise Comparativa e Interpretação

Prever a geração de um Pokémon é um problema de classificação **multiclasse** complexo. O baixo desempenho geral de todos os modelos revela algo fundamental sobre a base de dados: **Não há um padrão claro e linear que diferencie as gerações através de seus status puros**. A Game Freak (desenvolvedora do jogo) mantém a média de status e distribuição de tipos muito parecida de uma geração para outra.

### 1. Redes Neurais (MLP Classifier)
- **Como se saiu:** Foi o melhor modelo com 32% de acurácia. A Rede Neural consegue mapear alguns padrões não lineares extremamente fracos, como certas combinações de tipos que só apareceram nas gerações mais novas.
- **Ponto Positivo:** É o modelo mais flexível para esse cenário caótico.

### 2. K-Nearest Neighbors (KNN)
- **Como se saiu:** Com 27% de acurácia, ele tentou aproximar os Pokémon por atributos parecidos (distância euclidiana), mas acabou falhando porque Pokémon idênticos em status podem pertencer a gerações completamente distintas (ex: o rato pássaro do começo do jogo existe em todas as 7 gerações com status quase iguais).

### 3. Naive Bayes (Gaussian)
- **Como se saiu:** Obteve o pior desempenho (24%). Ao assumir que cada atributo e tipo são completamente independentes, ele perde todo o contexto e confunde as gerações. Chegou a acertar 67% (Recall) da Geração 1 apenas "chutando" a Geração 1 repetidamente, o que zerou sua precisão nas gerações 2 e 7.

## 💡 Conclusão
Ao contrário do **PKL 1** (onde Lendários têm status nitidamente maiores e padrões óbvios que os modelos detectam com mais de 90% de acurácia), tentar prever a geração de um Pokémon através de status de combate é praticamente inviável na vida real sem dados extras (como design, paleta de cores ou data de lançamento). Esse experimento é a prova empírica de que os atributos dos Pokémon se mantiveram balanceados ao longo das 7 gerações.
