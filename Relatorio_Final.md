# Trabalho Final - Análise de Machine Learning (Pokémon)

## 📌 1. Apresentação da Base e Pré-processamento
A base de dados escolhida contém características detalhadas de todas as gerações de Pokémon (`pokemon.csv`). Ela possui atributos físicos (peso, altura), atributos de combate (HP, Ataque, Defesa, etc.) e variáveis categóricas como os Tipos Elementais.

**Pré-processamento Realizado:**
- Tratamento de valores ausentes (ex: altura e peso).
- Normalização de dados numéricos para a mesma escala (Min-Max Scaler), essencial para algoritmos baseados em distância como o KNN.
- Codificação One-Hot para os Tipos (transformando variáveis categóricas em binárias para o Apriori).
- Na etapa de Classificação, foi aplicado o **SMOTE** (sobreamostragem) nas bases de treino para tratar desbalanceamento de classes, conforme sugerido nos slides da disciplina.

---

## 🤖 2. Classificações Realizadas

Aplicamos os algoritmos ensinados em sala (**KNN** e **Naive Bayes**) e também Redes Neurais para explorar os resultados.

### 🎯 PKL 1: Predição de Lendários
O objetivo foi prever se um Pokémon é Lendário (`1`) ou não (`0`). A base possuía um forte desbalanceamento que foi resolvido pelo SMOTE.

- **Redes Neurais (MLP):** Acurácia Geral de 93%. Foi o melhor algoritmo, conseguindo o melhor equilíbrio entre Precisão (62%) e Recall (36%) na detecção dos lendários.
- **KNN (K=5):** Acurácia de 91%. O SMOTE forçou o KNN a prestar atenção aos Lendários, fazendo com que ele de fato procurasse Pokémons pelas distâncias euclidianas próximas ao invés de chutar que ninguém era lendário.
- **Naive Bayes:** Acurácia de 26%, mas Recall incrivelmente alto (86%). Como ele usa probabilidade pura assumindo independência entre os status, o modelo classifica quase a base inteira como lendária para não deixar ninguém escapar. 

**💡 Interpretação (Lendários):**
Atributos de combate funcionam maravilhosamente bem para detectar lendários. Existe um padrão matemático gritante (status altíssimos) que os modelos exploram com maestria.

### 🎯 PKL 2: Predição da Geração
O objetivo foi tentar adivinhar a Geração (1 a 7) de um Pokémon apenas por seus status e tipagem. Este é um problema Multiclasse muito mais complexo.

- **Redes Neurais (MLP):** Acurácia de 32%. (Melhor cenário)
- **KNN (K=5):** Acurácia de 27%.
- **Naive Bayes:** Acurácia de 24%.

**💡 Interpretação (Geração):**
Foi um fracasso preditivo total! No entanto, **a interpretação disso é valiosa:** Esse experimento prova empiricamente que a franquia Pokémon mantém os seus status e tipos balanceados entre as gerações. Não importa se um Pokémon é do primeiro jogo (1996) ou do último (2016), os status base são distribuídos de maneira muito similar, impossibilitando que a Inteligência Artificial ache um padrão óbvio entre gerações usando puramente números de combate.

---

## 📊 3. Agrupamento (K-Means++)
O objetivo foi segmentar os Pokémon baseando-se apenas em seus atributos físicos e de combate contínuos (Ataque, Defesa, HP, Sp. Atk, Sp. Def, Speed e Peso). Utilizamos o algoritmo K-Means++ com `K=4`.

### Perfis Identificados (Interpretação)
O algoritmo organizou de forma autônoma a base em 4 grandes perfis práticos:
- **Grupo 1: Os "Estágios Iniciais" (313 Pokémon):** É a grande maioria da base. Representam Pokémon pequenos e iniciais. Possuem os status mais baixos de toda a base (Ataque ~53, Velocidade ~49) e são extremamente leves (média de 16kg).
- **Grupo 2: Os "Atacantes Rápidos" (244 Pokémon):** Pokémon focados em combate ágil. Possuem as maiores médias de Velocidade (~89) da base, mas são relativamente leves (~42kg) e não aguentam tanto dano (Defesa ~71).
- **Grupo 3: Os "Tanques Defensivos" (166 Pokémon):** Pokémon robustos e lentos. Possuem a maior média de Defesa (~104), são pesados (~109kg), mas sacrificam a velocidade (~52).
- **Grupo 4: Os "Pesos-Pesados / Lendários" (78 Pokémon):** A elite do mundo Pokémon. Monstros com status astronômicos (Ataque ~126, HP ~94) e um peso colossal (média de ~197kg).

### 💡 O que pode ser feito com essa informação?
Em um jogo ou balanceamento de RPG competitivo, esse agrupamento serve como "Tiers" ou "Classes" naturais. Pode-se criar regras automáticas de matchmaking onde Pokémon do Grupo 4 não podem enfrentar os do Grupo 1, garantindo que o jogo seja mais justo para o usuário.

---

## 🔗 4. Regras de Associação (Apriori)
O algoritmo Apriori foi utilizado para descobrir padrões ocultos na combinação de Tipos Elementais primários (`type1`) e secundários (`type2`). Utilizamos os critérios de Suporte Mínimo e Confiança. 

### Padrões e Regras Encontradas
Analisando as regras geradas com o maior **Lift** (que mede o quão maior é a chance de B acontecer dado que A aconteceu):

1. **`Normal` ➔ `Flying`** e **`Flying` ➔ `Normal`** (Lift: 1.95)
   - **Interpretação:** Um cliente/jogador que possui um Pokémon Voador tem quase o dobro de chance de possuir na verdade um Pokémon Normal/Voador. Esta regra expõe o famoso padrão dos "passarinhos de rota inicial" da franquia. Ambas as tipagens andam intimamente juntas no design do jogo.
2. **`Poison` ➔ `Grass`** (Lift: 1.80)
   - **Interpretação:** Saber que um Pokémon tem o tipo "Veneno" (Poison) aumenta quase em dobro a chance dele ser também do tipo Grama. Biologicamente e conceitualmente, a maioria das plantas desenhadas na franquia original são venenosas (ex: linha evolutiva do Bulbasaur, Oddish, Bellsprout).

### 💡 Possíveis Aplicações
Estas regras podem ser usadas por uma equipe de Game Design para identificar combinações "saturadas" (clichês) de Pokémon e planejar futuras gerações com tipagens mais raras e inovadoras, fugindo da regra de associação batida de Insetos+Venenosos.

---
**Todos os scripts gerados (KNN, Naive Bayes, KMeans, Apriori) e os modelos no formato .pkl estão salvos em suas respectivas pastas no projeto.**
