# Roteiro de Apresentação (Slides) - Machine Learning em Pokémon

Este documento foi preparado para você copiar e colar o texto nos slides e saber exatamente o que falar na hora de apresentar o trabalho. O conteúdo foi expandido para dar mais segurança técnica durante a apresentação e impressionar os avaliadores.

---

## Slide 1: Capa
- **Título:** Análise de Machine Learning: Base de Dados Pokémon
- **Subtítulo:** Classificação, Agrupamento e Regras de Associação aplicadas a Game Design
- **Integrantes:** [Nome dos Alunos]

**🗣️ [O que falar]**
*"Olá a todos, bom dia/boa noite. Nosso trabalho aplica as principais técnicas de Machine Learning — Classificação, Agrupamento e Regras de Associação — em uma base de dados da franquia Pokémon. O nosso objetivo não foi apenas rodar algoritmos, mas sim extrair 'business insights', ou seja, como a Inteligência Artificial pode orientar decisões de Game Design e balanceamento de produtos."*

---

## Slide 2: A Base de Dados e Pré-Processamento
**[Texto no Slide]**
* **Base:** `pokemon.csv` (801 registros cobrindo 7 gerações).
* **Limpeza de Dados:** Tratamento de valores ausentes (NaN) nas variáveis de peso e altura para evitar falhas nos modelos.
* **Transformações (Feature Engineering):**
  * **Normalização (Min-Max Scaler):** Padronização dos atributos de combate (HP, Ataque, Defesa, Velocidade).
  * **One-Hot Encoding:** Transformação das variáveis categóricas de Tipos (Fogo, Água, etc.) em variáveis binárias independentes.
* **Balanceamento (SMOTE):** Geração de dados sintéticos para resolver o grave desbalanceamento de classes (ex: apenas 10% da base é composta por Pokémon Lendários).

**🗣️ [O que falar]**
*"Nossa base engloba 801 Pokémon. Antes de qualquer análise, o pré-processamento foi crucial. Tivemos que limpar dados nulos e, mais importante, normalizar os atributos de combate para uma escala de 0 a 1. Isso é obrigatório porque algoritmos baseados em distância, como o KNN, seriam enviesados por grandezas diferentes. Além disso, aplicamos o One-Hot Encoding para separar os tipos elementais em colunas binárias. Por fim, usamos a técnica SMOTE nas bases de treino. Como temos poucos Pokémon lendários (cerca de 10%), os modelos tenderiam a ignorá-los. O SMOTE cria exemplos sintéticos de lendários para equilibrar o aprendizado da IA."*

---

## Slide 3: Classificação I - Predição de Lendários (Modelagem)
**[Texto no Slide]**
* **Objetivo:** Prever se um Pokémon é Lendário (1) ou Comum (0) baseando-se apenas em seus status de combate.
* **Desafio:** Lidar com a classe minoritária.
* **Redes Neurais (MLP):** Acurácia de 93% (Melhor equilíbrio entre Precisão e Recall).
* **KNN (K=5):** Acurácia de 91% (Excelente adaptação graças ao balancemento prévio).
* **Naive Bayes:** Acurácia de 26% (Baixa precisão, mas altíssimo Recall de 86%).

**🗣️ [O que falar]**
*"Na nossa primeira tarefa de classificação, o desafio era fazer a máquina descobrir se um Pokémon é lendário ou não apenas olhando seus números. A Rede Neural Multi-Layer Perceptron foi a vencedora com 93% de acurácia, mantendo um ótimo equilíbrio: quando ela diz que é lendário, ela costuma acertar (Precisão), e ela consegue encontrar a maioria dos lendários da base (Recall). O Naive Bayes teve uma acurácia baixíssima de 26%, pois sua abordagem probabilística acabou classificando quase todo mundo como lendário. Mas o verdadeiro herói dessa etapa foi o balanceamento de dados..."*

---

## Slide 4: Classificação I - Interpretação e Impacto do SMOTE
**[Texto no Slide]**
* **O Padrão dos Lendários:** A IA comprova que existe uma "fórmula" matemática (status muito superiores e bem distribuídos) que define a raridade.
* **A Importância Crítica do SMOTE:**
  * **Sem SMOTE (O Paradoxo da Acurácia):** Algoritmos batiam 90% de acurácia simplesmente "chutando" que **nenhum** Pokémon era lendário (já que 90% são comuns). O modelo era inútil.
  * **Com SMOTE:** Forçamos o KNN e a Rede Neural a de fato aprenderem as fronteiras de decisão e as distâncias reais entre as classes.

**🗣️ [O que falar]**
*"O insight mais técnico e valioso dessa etapa é o impacto do SMOTE. Se rodássemos o KNN na base original, ele atingia 90% de acurácia. Parece ótimo, certo? Errado. Ele atingia isso simplesmente apostando que nenhum Pokémon era lendário, ignorando a classe minoritária. Ao introduzir o SMOTE, nós forçamos o modelo a aprender a distância euclidiana e os padrões reais. A conclusão de negócio aqui é que fraudes, ou anomalias (como um lendário super forte), possuem uma assinatura matemática clara que a IA consegue isolar perfeitamente se ensinada corretamente."*

---

## Slide 5: Classificação II - Predição da Geração
**[Texto no Slide]**
* **Objetivo:** Adivinhar a Geração de lançamento (1 a 7) de um Pokémon através de seus status de combate.
* **Resultados dos Modelos:**
  * **Redes Neurais (MLP):** Acurácia de 32%.
  * **KNN (K=5):** Acurácia de 27%.
  * **Naive Bayes:** Acurácia de 24%.
* **Veredito:** Falha preditiva generalizada. Os modelos não conseguiram generalizar padrões por geração.

**🗣️ [O que falar]**
*"Como segundo problema de classificação, fomos mais ambiciosos: será que a máquina consegue adivinhar a geração de um Pokémon, ou seja, o ano em que ele foi criado, apenas pelos seus números de combate? O resultado foi um fracasso preditivo total. Todos os modelos beiraram a aleatoriedade, errando a grande maioria das previsões. Mas, em Ciência de Dados, uma falha do modelo pode ser o nosso maior insight..."*

---

## Slide 6: Classificação II - Interpretação (Por que falhou?)
**[Texto no Slide]**
* **O Fracasso do Modelo é o Sucesso do Game Design:** A franquia mantém seus status padronizados e rigorosamente balanceados desde 1996.
* **Falta de Separação Linear:** Um Pokémon fraco do primeiro jogo tem uma distribuição matemática quase idêntica a um Pokémon fraco do sétimo jogo.
* **Conclusão Analítica:** A IA prova empiricamente que não houve "Power Creep" (inflação de poder) generalizado nos status base ao longo das décadas. Variáveis externas (Design, Cor) seriam necessárias.

**🗣️ [O que falar]**
*"Por que a Rede Neural e o KNN falharam? Porque não há padrão a ser encontrado! A Game Freak, desenvolvedora do jogo, mantém a distribuição matemática extremamente rigorosa e idêntica entre as gerações. Um rato fraco da geração 1 tem status praticamente idênticos a um rato da geração 7. Em termos de Game Design, a Inteligência artificial nos forneceu uma prova empírica de que o jogo é perfeitamente balanceado através das décadas, não sofrendo com inflação de poder nos status base. Os números não denunciam a idade do personagem."*

---

## Slide 7: Agrupamento (K-Means++)
**[Texto no Slide]**
*(Insira as imagens geradas: gráfico de dispersão dos clusters ou PCA)*

* **Objetivo:** Aprendizado Não-Supervisionado. Segmentar Pokémon de forma autônoma pedindo 4 grupos (K=4), usando apenas dados contínuos.
* **Os 4 Perfis Descobertos:**
  * **Grupo 1: "Estágios Iniciais" (313 registros):** Maioria da base. Leves (~16kg) e com status baixos (bebês).
  * **Grupo 2: "Atacantes Rápidos" (244 registros):** Alta velocidade média (~89) e ataque, mas defesa baixa (Glass Cannons).
  * **Grupo 3: "Tanques Defensivos" (166 registros):** Alta defesa (~104), pesados, porém muito lentos.
  * **Grupo 4: "Pesos-Pesados / Lendários" (78 registros):** Monstros com ataque absurdo (~126) e peso colossal (~197kg).

**🗣️ [O que falar]**
*"Saindo da Classificação, fomos para o Aprendizado Não-Supervisionado com o algoritmo K-Means. Pedimos para ele dividir nossa base em 4 grupos, sem dar nenhum rótulo prévio. Ele apenas calculou as distâncias entre os pontos. O resultado foi incrível: a matemática pura recriou os arquétipos clássicos de RPG. O Grupo 1 agrupou os bebês; o Grupo 2 juntou os 'Glass Cannons', que são rápidos e batem forte mas têm pouca vida; o Grupo 3 isolou os 'Tanques', lentos e cheios de armadura; e o Grupo 4 filtrou a elite, os gigantes e lendários do jogo."*

---

## Slide 8: Agrupamento - Aplicação Prática no Mercado
**[Texto no Slide]**
* **Interpretação e Uso em Produção:**
  * **Organização de Tiers:** Formação natural de categorias competitivas.
  * **Sistema de Matchmaking Justo:** Utilizar os centróides da IA para pareamento em servidores online.
  * **Segmentação Autônoma:** Semelhante a como empresas agrupam perfis de clientes (Novatos, Intermediários, Premium).

**🗣️ [O que falar]**
*"Para que isso serve no mundo real? Num ambiente de desenvolvimento de jogos, usaríamos esses clusters para criar um sistema de 'Matchmaking' (pareamento) automático e justo. Se o sistema detecta que um jogador escolheu personagens cujos status o colocam no Grupo 1, a IA do servidor vai pareá-lo com outro jogador do Grupo 1, evitando que um novato seja esmagado por alguém usando Pokémon do Grupo 4. É exatamente a mesma lógica que o varejo usa para segmentar clientes Ouro, Prata e Bronze."*

---

## Slide 9: Regras de Associação (Algoritmo Apriori)
**[Texto no Slide]**
*(Insira o gráfico de top 10 regras de associação / Lift)*

* **Objetivo:** Mineração de Padrões Frequentes. Descobrir quais Tipos Elementais (`Type 1` e `Type 2`) possuem forte correlação e costumam "ser vendidos juntos".
* **Principais Regras Encontradas:**
  * **Regra 1:** Se `Voador`, então `Normal` (e vice-versa) (Lift = 1.95).
  * **Regra 2:** Se `Venenoso`, então `Grama` (Lift = 1.80).
* *(Nota: Lift > 1 indica que a ocorrência conjunta é maior do que o esperado pelo acaso).*

**🗣️ [O que falar]**
*"Para finalizar, rodamos o algoritmo Apriori, muito usado em sistemas de recomendação de supermercados e Netflix, para achar 'vendas casadas'. Queríamos ver quais Tipos Elementais andam sempre juntos independentemente da ordem primária ou secundária. A métrica 'Lift' nos diz a força dessa regra. Descobrimos uma relação clássica entre Voador e Normal (os famosos passarinhos de início de jogo), e vimos também que se um Pokémon tem o tipo Venenoso, a probabilidade dele também ser de Grama é quase o dobro do normal."*

---

## Slide 10: Associação - Inovação e Design de Produto
**[Texto no Slide]**
* **Significado:** A IA mapeou a biologia do jogo e expôs os "clichês" da franquia.
  * *Ex: Plantas e insetos venenosos da vida real.*
  * *Ex: Os clássicos passarinhos normais de todo começo de jogo.*
* **Aplicação Estratégica (Direção de Arte):** 
  * Analisar esses dados revela os nichos saturados.
  * Orientar as equipes de criação a desenvolverem produtos Inovadores, forçando tipagens inéditas (Fogo/Água, Elétrico/Gelo) baseando-se nos "buracos" deixados pelas regras de associação.

**🗣️ [O que falar]**
*"A máquina percebeu as vendas casadas baseadas na biologia do mundo real, como plantas venenosas ou pássaros normais. O grande poder dessa informação para uma diretoria de produto é enxergar a saturação do próprio catálogo. Ao invés de criar mais um Pokémon Grama/Venenoso que já é um clichê de 20 anos, o Apriori mostra exatamente onde estão as lacunas. A empresa pode forçar os designers a criarem combinações raras ou inexistentes, como Fogo com Água, gerando inovação real e interesse renovado do público."*

---

## Slide 11: Conclusão
**[Texto no Slide]**
* O poder da Ciência de Dados além dos números:
  1. **Classificação:** Permitiu detectar anomalias e provar o balanço longitudinal do jogo ao longo das décadas.
  2. **Agrupamento:** Segmentou entidades organicamente, viabilizando sistemas de pareamento justo e classificação de níveis.
  3. **Associação:** Mapeou as características saturadas do produto, fornecendo um roteiro claro para a inovação e design de novas criaturas.
* **Veredito Final:** As técnicas de Machine Learning são ferramentas essenciais para tomadas de decisão estratégicas, independentemente do domínio dos dados.

**🗣️ [O que falar]**
*"Para concluir, provamos que as técnicas da nossa disciplina são ferramentas de tomada de decisão. Nós usamos as mesmas lógicas de detecção de fraude de bancos, segmentação de mercado de grandes varejistas e motores de recomendação de streaming, para analisar uma base de dados da cultura pop. Conseguimos extrair insights que orientariam todo um modelo de negócios, o balanceamento de software e o design de futuros jogos. Muito obrigado!"*
