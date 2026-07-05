#  Explicação dos Gráficos de Agrupamento (K-Means)

Este documento explica detalhadamente como os gráficos desta pasta foram gerados e qual o significado prático por trás de cada visualização.

O objetivo desta etapa foi utilizar o algoritmo **K-Means++** para dividir os Pokémon em 4 grupos (Clusters) utilizando **apenas seus atributos numéricos contínuos de combate e físicos** (Ataque, Defesa, HP, Ataque Especial, Defesa Especial, Velocidade, Altura e Peso). A IA separou a base de dados em 4 perfis distintos sem saber quem era quem, descobrindo padrões naturais da franquia.

---

## 1. Gráfico de Dispersão: Ataque vs Velocidade
**Arquivo:** `grafico_ataque_velocidade.png`

* **Como foi gerado:** Foi utilizado um gráfico de dispersão (*scatter plot*) onde o Eixo X representa a **Velocidade** (Speed) e o Eixo Y representa o **Ataque** (Attack) dos Pokémon. Cada ponto no gráfico é um Pokémon e a cor do ponto indica a qual dos 4 grupos criados pelo K-Means ele pertence.
* **Por que ficou desse jeito (Interpretação):** 
  * O gráfico mostra claramente o **Grupo 2 (Atacantes Rápidos)** dominando a área superior direita (alta velocidade e bom ataque), confirmando o perfil biológico de Pokémon ágeis focados em causar dano (os famosos *Glass Cannons*).
  * No extremo inferior esquerdo, isola-se o **Grupo 1 (Estágios Iniciais)**, mostrando os bebês que são lentos e possuem pouco ataque.
  * O **Grupo 4 (Pesos-Pesados/Lendários)** geralmente aparece no topo (altíssimo ataque), enquanto o **Grupo 3 (Tanques)** se mantém em zonas de velocidade muito baixa, refletindo suas armaduras pesadas.

---

## 2. Gráfico de Dispersão: Defesa vs Pontos de Vida (HP)
**Arquivo:** `grafico_defesa_hp.png`

* **Como foi gerado:** Também um gráfico de dispersão cruzando a **Defesa** (Eixo X) com os **Pontos de Vida / HP** (Eixo Y). Novamente, colorido de acordo com os clusters gerados pela Inteligência Artificial.
* **Por que ficou desse jeito (Interpretação):**
  * Este gráfico evidencia de forma gritante o **Grupo 3 (Tanques Defensivos)**. É possível ver uma nuvem verde esparramada para a direita (alta Defesa) e também os picos no eixo Y, indicando Pokémon muito resistentes a dano.
  * O **Grupo 2 (Atacantes Rápidos)** e o **Grupo 1 (Estágios Iniciais)** se espremem quase todos no canto inferior esquerdo, o que faz todo o sentido, pois são criaturas frágeis e que morrem rápido em combate.
  * O **Grupo 4 (Lendários)** domina as áreas mais altas (alto HP e boa Defesa geral), consolidando seu status como as criaturas supremas do jogo.

---

## 3. Gráfico de Barras: Distribuição dos Clusters
**Arquivo:** `grafico_distribuicao_clusters.png`

* **Como foi gerado:** Trata-se de um *Countplot* (Gráfico de Contagem) exibindo o número exato de Pokémon que caíram em cada um dos 4 clusters descobertos pelo modelo K-Means.
* **Por que ficou desse jeito (Interpretação):**
  * O **Grupo 1 (Estágios Iniciais)** é o maior bloco disparado (cerca de 313 Pokémon). Isso faz muito sentido prático: em qualquer ecossistema (e nos jogos RPG), a imensa maioria dos monstros encontrados na natureza são os elos mais baixos da cadeia alimentar (fracos e pequenos).
  * O **Grupo 4 (Pesos-Pesados / Lendários)** é a menor barra (78 Pokémon). Biológica e mercadologicamente, eles representam a elite do jogo; criaturas raras, monstros gigantes ou divindades mitológicas não devem ser abundantes, caso contrário perderiam seu status de "Chefe".
  * Os **Grupos 2 e 3** (Atacantes Rápidos e Tanques) representam as classes comuns (ou "Tiers" competitivos intermediários) equilibrando o meio termo.
