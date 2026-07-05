# Etapa 01: Normalização e Limpeza dos Dados

Nesta etapa, realizamos o pré-processamento inicial da base de dados original (`pokemon.csv`) para deixá-la pronta para as atividades de machine learning (Classificação e Agrupamento).

## 1. Exclusão de Colunas Irrelevantes
Muitas colunas na base original não agregam valor aos nossos modelos ou dariam a "resposta pronta" para o algoritmo. Por isso, as seguintes colunas foram removidas:

- **`is_legendary`** e **`generation`**: Removidas pois serão os nossos **Alvos (Targets)** para os modelos de classificação PKL 1 e PKL 2, respectivamente (não podemos dar a resposta ao modelo durante o treinamento).
- **Colunas `against_*`**: Todas as 18 colunas de multiplicador de dano (`against_bug`, `against_fire`, etc.) foram removidas para simplificar a base e focar nos status dos Pokémons.
- **`japanese_name`**, **`name`** e **`pokedex_number`**: São apenas identificadores (strings e IDs) e não ajudam a encontrar padrões.
- **`classfication`**, **`abilities`** e **`base_egg_steps`**: Dados de texto soltos ou muito específicos de reprodução que decidimos excluir nesta primeira passagem para simplificar a normalização.
- **`base_total`**: É redundante, pois é a soma de todos os status (HP, Attack, etc.) e pode confundir os algoritmos.
- **`base_happiness`**, **`capture_rate`**, **`percentage_male`**, e **`experience_growth`**: Foram excluídas pois dariam a "resposta" pronta para descobrir se o Pokémon é Lendário. Sem elas, o modelo aprenderá a classificar puramente pelos status e tipos.

## 2. Tratamento de Valores Ausentes e Erros (Limpeza)
Algumas colunas vieram com problemas que precisaram de correção:
- **`height_m` (Altura)** e **`weight_kg` (Peso)**: Pokémons sem esses dados registrados tiveram seus valores preenchidos com a mediana geral para não precisarmos excluir a linha do Pokémon.
- **`type2`**: Pokémons que possuem apenas um tipo tinham essa coluna vazia. Preenchemos com a palavra `"None"` (Nenhum).

## 3. Codificação de Variáveis Categóricas (One-Hot Encoding)
Algoritmos matemáticos (como Redes Neurais e KNN) não entendem textos como "Fire" ou "Water". Para resolver isso, aplicamos a técnica de **One-Hot Encoding** nas colunas `type1` e `type2`. Isso transforma os tipos em várias novas colunas contendo `0` ou `1` (ex: `type1_fire=1`, `type1_grass=0`), permitindo que a IA entenda os tipos do Pokémon.

## 4. Normalização de Escala (MinMaxScaler)
Atributos numéricos possuíam escalas muito diferentes (ex: HP de 150 vs Altura de 1.5m). Se deixados assim, o KNN e a Rede Neural dariam peso desproporcional aos números grandes. Usamos o **MinMaxScaler** para "espremer" todos os valores numéricos (HP, Ataque, Defesa, etc.) em uma escala de **0 a 1**, balanceando o peso de todos os status.

## Resultado
Após a execução do script de normalização, o arquivo resultante gerado é o **`pokemonNormalizado.csv`**, que agora contém apenas números e será utilizado como a base para o treinamento de todos os modelos de Machine Learning.
