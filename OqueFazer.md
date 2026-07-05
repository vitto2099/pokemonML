# Trabalho Final - Análise de Base de Dados (Pokémon)

##  Descrição do Projeto
Os alunos deverão se organizar em grupos de até quatro integrantes para realizar uma
análise completa em uma base de dados. Cada grupo deverá escolher uma base de dados
e realizar todas as etapas necessárias de pré-processamento, como limpeza, tratamento de
valores ausentes, normalização, codificação de variáveis categóricas e seleção de atributos,
garantindo que a base esteja adequada para as técnicas. Em seguida, deverão aplicar os
algoritmos de classificação, de agrupamento e gerar regras de associação, utilizando os
algoritmos estudados em sala. Durante a apresentação, o grupo deverá fazer uma breve
descrição da base utilizada, relatar todas as etapas de pré-processamento realizadas e
apresentar os resultados obtidos nas atividades de classificação, agrupamento e regras de

associação. Mais do que simplesmente mostrar os resultados, o grupo deverá interpretá-
los, por exemplo, ao apresentar que foram gerados quatro grupos em um algoritmo de

agrupamento, é necessário descrever como esses grupos se diferenciam entre si, quais
características predominam em cada um, quais perfis podem ser identificados e o que
pode ser feito com essa informação. A interpretação também deve estar presente nas
atividades de classificação e nas regras de associação (explicando o significado das regras e
suas possíveis aplicações).

##  Base de Dados Escolhida
- **Tema:** Pokémon (`pokemon.csv`)
- **Apresentação:** Fazer uma breve descrição conceitual da base utilizada.

##  Pré-processamento
Garantir que a base esteja adequada para as técnicas de machine learning. Etapas a relatar:
- Limpeza e tratamento de valores ausentes.
- Exclusões realizadas (ex: colunas `against_*`, coluna `is_legendary` e outras irrelevantes/óbvias que não exigirão normalização).
- Normalização e codificação de variáveis categóricas (se aplicável).

## Atividades de Modelagem

### 1. Classificação (Gerar mais de um arquivo PKL)
Algoritmos a serem utilizados: **KNN, Naive Bayes e Redes Neurais**.
- **PKL 1:** Prever se um Pokémon é lendário ou não.
  - *(Nota: A coluna original foi excluída do CSV final para não dar a resposta pronta ao modelo).*
- **PKL 2:** Prever a Geração (1 a 7).
  - *(Nota: A coluna original foi excluída do CSV final para não dar a resposta pronta ao modelo).*

### 2. Agrupamento (Clustering)
Algoritmo a ser utilizado: **K-Means++**
Gerar mais de um agrupamento e interpretar as características predominantes de cada perfil (o número de grupos é livre).
- **Agrupamento 1:** Agrupar Pokémon por atributos físicos e de combate.
- **Agrupamento 2:** Agrupar Pokémon por tipos elementais.

### 3. Regras de Associação
Algoritmo a ser utilizado: **Apriori**
Explicar o significado das regras e suas possíveis aplicações práticas.
- **Regras 1:** Tipos de Pokémon.
- **Regras 2:** Tipos por geração.



##  Apresentação
A apresentação do grupo deve cobrir, de forma interpretativa (o que a informação significa e o que fazer com ela), os seguintes tópicos:
1. Apresentar o conceito da database.
2. Pré-processamento (limpezas, o que não foi preciso normalizar, etc). (usamos a primeira geração pra validar os testes)
3. Resultados da Classificação.
4. Resultados do Agrupamento (como os grupos se diferenciam).
5. Resultados das Regras de Associação.

---

# Plano de Modelagem e Geração dos PKLs

Chegamos na fase de **Machine Learning (Treinamento da Inteligência Artificial)**. Como foi solicitado no documento `OqueFazer.md`, usaremos três algoritmos para a classificação: **KNN, Naive Bayes e Redes Neurais**.

## Estrutura de Pastas e Entregáveis

Para manter a organização do projeto (conforme alinhado), criaremos pastas separadas para cada problema de classificação:

- **Pasta `/PKL1_Lendario`**
  - Conterá os 3 arquivos `.pkl` dos modelos treinados (KNN, Naive Bayes e Neural Network).
  - Conterá um arquivo `README.md` com uma análise comparativa dos modelos (Acurácia, pontos positivos e negativos de cada um para esse problema específico).
- **Pasta `/PKL2_Crescimento`**
  - Conterá os 3 arquivos `.pkl` dos modelos treinados para o segundo problema.
  - Conterá um arquivo `README.md` com a análise comparativa de desempenho.

##  Proposed Changes (O que faremos a seguir)

### 1. Preparar e Treinar o PKL 1 (Lendário)
- **Recuperar o Target:** Extrairemos a coluna `is_legendary` do seu arquivo intacto `pokemon.csv` para servir de gabarito (`Y`) no treinamento.
- **Treinamento:** Usaremos o nosso `2pokemonNormalizado.csv` como as variáveis preditoras (`X`).
- **Treinar e Salvar:** Os três algoritmos serão treinados e exportados para a pasta `/PKL1_Lendario`.
- **Análise:** Avaliaremos qual modelo teve a melhor precisão e escreveremos o `README.md`.

### 2. Preparar e Treinar o PKL 2 (Crescimento Rápido/Devagar)
- **Preparar o Target:** A coluna `experience_growth` original possui valores numéricos contínuos muito altos (ex: 1.000.000). Para transformar isso em uma "Classificação", dividiremos a base ao meio usando a mediana ou a média: Pokémon abaixo do limite serão classe `0` (Upa Devagar) e acima serão classe `1` (Upa Rápido).
- **Treinar e Salvar:** Treinaremos os mesmos 3 modelos para tentar prever essa nova característica e exportaremos para a pasta `/PKL2_Crescimento`.
- **Análise:** Escreveremos o respectivo `README.md` avaliando o desempenho.
