# 🐉 Trabalho Final: Machine Learning em Pokémon

Este repositório contém a entrega completa do trabalho final da disciplina, onde exploramos técnicas preditivas e descritivas de *Machine Learning* aplicadas a uma base de dados da franquia Pokémon. O foco é interpretar os resultados da IA e gerar aplicações de negócio/design focadas no desenvolvimento e balanço do jogo.

---

## 📁 Estrutura do Projeto

A organização das etapas segue uma ordem lógica no repositório:

- **`01_Processamento/`**
  - Contém o notebook ou scripts originais de limpeza de dados e geração do arquivo `.csv` normalizado.
- **`01_Classificacao_Lendario/`**
  - **Objetivo:** Treinar IA para prever se o Pokémon é Lendário (`1`) ou não (`0`).
  - Modelos exportados `.pkl` (Redes Neurais, KNN, Naive Bayes) e análise métrica em Markdown.
- **`02_Classificacao_Geracao/`**
  - **Objetivo:** Advinhar a Geração (1 a 7) do Pokémon (experimento de prova de balanceamento estático do jogo).
  - Modelos exportados `.pkl` e interpretação da ineficiência linear nas gerações.
- **`03_Agrupamento/`**
  - **Objetivo:** Segmentar Pokémon através do **K-Means++** (em 4 clusters/classes) baseado unicamente em atributos numéricos de combate e físicos.
  - Script para agrupar e script (`gerar_graficos.py`) para desenhar belos gráficos de dispersão `x` e `y` separados por cor.
- **`04_Associacao/`**
  - **Objetivo:** Encontrados (*Tipos Casados*) usando o algoritmo **Apriori** com foco no fator *Lift*. Ex: Pokémon Venenosos costumam estar fortemente associados ao Tipo Grama, e os do tipo Normal ao Voador.
  - Contém a lista de regras exportada `.pkl` e um gerador de gráficos de barras para a Apresentação.

### 📄 Relatórios 
Na raiz você encontrará:
- **`Relatorio_Final.md`**: O relatório acadêmico completo contando exatamente as etapas, os dados coletados e as interpretações valiosas que extraímos do ML.
- **`Roteiro_Apresentacao.md`**: Documento pronto para apresentação nos Slides com notas diretas para a oratória/apresentador.

---

## ⚙️ Pré-requisitos e Instalação

Para que você, ou o professor, possa executar os scripts de treinamento, agrupamento, associação ou para (re)gerar os gráficos, você precisará do **Python** instalado na sua máquina (versão 3.8 ou superior) e das seguintes bibliotecas:

Abra o terminal (Prompt de Comando ou PowerShell) e execute o seguinte comando:

```bash
pip install pandas numpy scikit-learn imbalanced-learn mlxtend matplotlib seaborn
```

**Resumo das bibliotecas utilizadas:**
- `pandas` e `numpy`: Manipulação do dataset (`.csv`).
- `scikit-learn`: Modelos de Classificação (KNN, GaussianNB, MLP) e Agrupamento (KMeans).
- `imbalanced-learn`: Responsável pelo **SMOTE** (balanceamento sintético dos dados para resolver a minoria da classe dos Lendários).
- `mlxtend`: Para gerar as regras de Associação com os métodos `apriori` e `association_rules`.
- `matplotlib` e `seaborn`: Para a plotagem e coloração dos gráficos `.png` inclusos nas pastas.

---

## 🚀 Como Executar

1. Navegue pelo terminal até a pasta do algoritmo que deseja testar. 
   Por exemplo, para gerar o agrupamento:
   ```bash
   cd 03_Agrupamento
   python agrupamento.py
   ```
2. Para gerar/atualizar os gráficos da pasta, basta executar:
   ```bash
   python gerar_graficos.py
   ```
*(Nota: No Windows, pode ser que você deva usar `py` ao invés de `python` dependendo de como a instalação está mapeada nas variáveis de ambiente).*
