# 🧬 PI_TG — A Evolução de um Cientista de Dados

> **Portfólio Integrador do Trabalho de Graduação (TG)**
> *Uma jornada evolutiva na prática através dos seis Projetos Integradores do curso de Ciência de Dados para Negócios.*

![Fatec Votorantim](https://img.shields.io/badge/Fatec-Votorantim-B20000)
![Curso](https://img.shields.io/badge/CST-Ci%C3%AAncia%20de%20Dados%20para%20Neg%C3%B3cios-blue)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-MLOps-FF3621?logo=databricks&logoColor=white)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-success)

---

## 📋 Sobre o Repositório

Este repositório reúne as evidências do **Trabalho de Graduação** de **Michel Cirilo de Oliveira**, apresentado à **Faculdade de Tecnologia de Votorantim – Benedito Pagliato (Fatec Votorantim / CEETEPS)**, como requisito para obter o grau de **Tecnólogo em Ciência de Dados para Negócios**.

O TG segue o formato de um **Portfólio Integrador aplicado**. Em vez de partir de um projeto novo, ele organiza e analisa criticamente os seis Projetos Integradores (PI1 a PI6) desenvolvidos ao longo da graduação. A narrativa usa a **metáfora da evolução humana** (Harari, 2015): cada semestre representa um salto adaptativo, das ferramentas clássicas de gestão até o MLOps em nuvem.

- 📄 **Documento consolidado do TG:** [trabalho-de-graduacao-consolidado-v7.docx](trabalho-de-graduacao-consolidado-v7.docx)
- 🎓 **Orientador:** Prof. Me. Hélio Rubens Jacintho Pereira Junior
- 📍 **Votorantim – SP, 2026**

---

## 🗺️ Jornada Evolutiva

```mermaid
flowchart LR
    PI1["🦴 PI1<br/>Reconhecimento e<br/>Sobrevivência Estratégica"] --> PI2["🎨 PI2<br/>Arte Rupestre<br/>Empatia e MVP"]
    PI2 --> PI3["📜 PI3<br/>Invenção da Escrita<br/>Engenharia de Dados"]
    PI3 --> PI4["🧮 PI4<br/>Marco dos Números<br/>Automação e ELT"]
    PI4 --> PI5["⚙️ PI5<br/>Revolução Industrial<br/>ML Preditivo"]
    PI5 --> PI6["🚀 PI6<br/>Revolução Tecnológica<br/>Databricks e MLOps"]
```

| Semestre | Projeto | Marco Evolutivo | Parceiro / Contexto | Foco Principal |
|:-:|---|---|---|---|
| 1º | [PI1 – Negócios](PI1_Negocios) | Reconhecimento e sobrevivência | Yara Cosméticos (fictícia) | Modelagem de negócios e gestão estratégica |
| 2º | [PI2 – Visualização](PI2_Visualizacao) | Arte rupestre e empatia | Yara Cosméticos (fictícia) | Design Thinking, MVP e Power BI |
| 3º | [PI3 – Engenharia de Dados](PI3_Engenharia_Dados) | Invenção da escrita | Regional 11 – Centro Paula Souza | ETL com OCR, modelo Snowflake e Streamlit |
| 4º | [PI4 – Automação Contábil](PI4_Automacao_Contabil) | Marco dos números | Berto Ferramentas | Arquitetura ELT e BI em Qlik Sense |
| 5º | [PI5 – Recomendação](PI5_Recomendacao) | Revolução Industrial | Berto Ferramentas | PLN, Fuzzy Match e FP-Growth |
| 6º | [PI6 – Databricks & MLOps](PI6_Databricks_MLOps) | Revolução Tecnológica | Berto Ferramentas | PySpark, MLflow, PyTorch e Streamlit |

---

## 📂 Estrutura do Repositório

```
PI_TG/
├── README.md                                   # Este arquivo
├── trabalho-de-graduacao-consolidado-v7.docx   # Documento final do TG
│
├── PI1_Negocios/              # 1º Sem – Yara Cosméticos (planejamento estratégico)
│   ├── VendasYara.ipynb       # Dados sintéticos de vendas (Faker, Pandas, Plotly)
│   ├── BMV Yara Corrigido.pdf # Business Model / Canvas
│   ├── CronogramaProjectYara.pdf, pmc.pdf
│   ├── Semiotica Yara.pdf, Pandas.pdf
│   └── Yara Entrega Final.pdf
│
├── PI2_Visualizacao/          # 2º Sem – Design Thinking, MVP e Power BI
│   ├── VendasYara.pbix        # Dashboard Power BI
│   ├── PI 2_YARA FINAL.pptx
│   └── PI2_Relatorio YARA FINAL.pdf
│
├── PI3_Engenharia_Dados/      # 3º Sem – ETL/OCR dos PGAs das Fatecs
│   └── PI3_Relatorio_Final_PCA.pdf
│
├── PI4_Automacao_Contabil/    # 4º Sem – Faturômetro (Qlik Sense / ELT)
│   ├── PI4_RelatorioFinal.pdf
│   └── Video Project.mp4
│
├── PI5_Recomendacao/          # 5º Sem – Sistema de Recomendação por Afinidade
│   ├── RecVendasv3.ipynb      # Pipeline completo + API FastAPI
│   ├── EDA/                   # Análise exploratória e versão ML completa
│   ├── Imagens/
│   ├── Base de Dados.txt      # Documentação da conexão HFSQL
│   ├── Read.md                # README detalhado do PI5
│   └── Relatório, Manual do Usuário, Deploy Guide, apresentações (PDF)
│
└── PI6_Databricks_MLOps/      # 6º Sem – Migração para Databricks
    ├── SRC/                   # 1_Catalogo / 2_Sistema_Recomendacao_Clean
    ├── EDA/                   # EDAs comparativas PI5 x PI6
    ├── TEST/                  # Benchmark Apriori x FP-Growth
    ├── APP/                   # Aplicação Streamlit (app.py + requirements.txt)
    └── Guia de Implantação, Manual do Usuário, Propriedade Intelectual (PDF)
```

---

## 🦴 PI1 — Reconhecimento e Sobrevivência Estratégica
**📁 [PI1_Negocios](PI1_Negocios) · Yara Cosméticos Ltda. (empresa fictícia)**

**Problema:** criar um modelo de negócios viável para uma marca de cosméticos **vegana e cruelty-free**, capaz de sustentar custos de produção de 8% a 15% maiores por causa dos ingredientes naturais. O público-alvo são mulheres de 26 a 35 anos, com ensino superior, da região Sudeste.

**Soluções e técnicas:**
- **Estratégia:** Análise SWOT, Balanced Scorecard (BSC), Business Model Canvas
- **Gestão de projetos (PMBOK):** Project Model Canvas e WBS/cronograma no MS Project
- **Comportamento organizacional:** estrutura funcional e "salas temáticas" de descompressão
- **Produto:** duas fragrâncias em frascos âmbar sustentáveis
- **Programação:** Python (Google Colab) com **Faker** para dados sintéticos, **Pandas**, **Matplotlib** e mapas coropléticos com **Plotly Express**
- **Matemática:** Teoria dos Conjuntos (Venn e Produto Cartesiano) aplicada ao CRM
- **Marketing:** análise semiótica da campanha (planos de expressão e de conteúdo)

**Artefatos:** [VendasYara.ipynb](PI1_Negocios/VendasYara.ipynb) · [Yara Entrega Final.pdf](<PI1_Negocios/Yara Entrega Final.pdf>) · [BMV Yara Corrigido.pdf](<PI1_Negocios/BMV Yara Corrigido.pdf>) · [Semiotica Yara.pdf](<PI1_Negocios/Semiotica Yara.pdf>) · [CronogramaProjectYara.pdf](PI1_Negocios/CronogramaProjectYara.pdf)

---

## 🎨 PI2 — Arte Rupestre, Empatia e o MVP
**📁 [PI2_Visualizacao](PI2_Visualizacao) · Yara Cosméticos Ltda.**

**Problema:** validar o modelo de negócios da Yara com clientes de forma rápida e barata, mesmo com poucos dados disponíveis.

**Soluções e técnicas:**
- **Design Thinking** em quatro etapas: imersão, ideação, prototipação e validação
- **Persona e Mapa de Empatia** (*Camila Freitas*): dores, necessidades e motivações
- **MVP:** catálogo cíclico, amostras grátis em feiras e coleta de aceitação por formulários
- **Estatística:** dados sintéticos com distribuição normal gerados em **Python e R**
- **Visualização:** dashboard de aceitação das fragrâncias em **Power BI**
- **Viabilidade financeira:** preço médio, CAC, ticket médio, faturamento e ROI

**Artefatos:** [VendasYara.pbix](PI2_Visualizacao/VendasYara.pbix) · [PI2_Relatorio YARA FINAL.pdf](<PI2_Visualizacao/PI2_Relatorio YARA FINAL.pdf>) · [PI 2_YARA FINAL.pptx](<PI2_Visualizacao/PI 2_YARA FINAL.pptx>)

---

## 📜 PI3 — Invenção da Escrita e Engenharia de Dados
**📁 [PI3_Engenharia_Dados](PI3_Engenharia_Dados) · Regional 11 de Sorocaba – Centro Paula Souza**

**Problema:** a análise dos **Planos de Gestão Anual (PGA)** das sete Fatecs da regional (Sorocaba, Itu, Botucatu, Tatuí, Votorantim, São Roque e Itapetininga) era lenta e manual. As informações ficavam presas em PDFs escaneados e sem estrutura.

**Soluções e técnicas:**
- **Pipeline ETL em Python:** extração com `PyMuPDF` e `pdfplumber`, OCR com `pytesseract`, limpeza com Regex e Pandas
- **Modelagem dimensional Snowflake** com ORM **SQLAlchemy** (1 tabela Fato + 14 Dimensões)
- **BI interativo em Streamlit** com Plotly e mapas Folium: carga horária por projeto, matriz de priorização, drill-down regional e alertas de inconsistências cadastrais

**Artefatos:** [PI3_Relatorio_Final_PCA.pdf](PI3_Engenharia_Dados/PI3_Relatorio_Final_PCA.pdf)

---

## 🧮 PI4 — O Marco dos Números, Automação Contábil e Paradigma ELT
**📁 [PI4_Automacao_Contabil](PI4_Automacao_Contabil) · Berto Ferramentas (Sorocaba – SP)**

**Problema:** os relatórios financeiros e de faturamento eram feitos à mão, em um único computador da loja. O processo levava dias e impedia que os gestores acompanhassem os números remotamente.

**Soluções e técnicas:**
- **Gestão ágil:** Scrum, Trello e GitHub
- **Diagnóstico administrativo:** SWOT, metas SMART, BSC e plano 5W2H
- **"Faturômetro"**, arquitetura **ELT em 3 camadas no Qlik Sense** com arquivos `.QVD`:
  1. **Extração:** dados brutos do ERP via OneDrive (`extract_data_Berto_Ferramentas.qvd`)
  2. **Transformação:** limpeza de nulos e formatação de moeda (`Transform_Data.qvd`)
  3. **Apresentação:** painel *Faturômetro – Berto Ferramentas* na nuvem

**Resultado:** a geração de relatórios caiu de **2 dias para minutos**.

**Artefatos:** [PI4_RelatorioFinal.pdf](PI4_Automacao_Contabil/PI4_RelatorioFinal.pdf) · [Video Project.mp4](<PI4_Automacao_Contabil/Video Project.mp4>)

---

## ⚙️ PI5 — Revolução Industrial: Sistema de Recomendação por Afinidade
**📁 [PI5_Recomendacao](PI5_Recomendacao) · Berto Ferramentas** — 📖 [README detalhado](PI5_Recomendacao/Read.md)

**Problema:** a sugestão de itens complementares no balcão (*cross-selling*, por exemplo trincha e aguarrás junto com tinta) dependia só da memória do vendedor. Com isso, vendas se perdiam e o atendimento ficava mais lento.

**Pipeline end-to-end:**

```
HFSQL (PDV) ──► pypyodbc/ODBC ──► Pandas (ETL/EDA) ──► Regex + RapidFuzz ──► "Produto Mestre"
                                                                                 │
           Interface do Vendedor ◄── API FastAPI/Uvicorn ◄── Regras FP-Growth ◄──┘
```

- **Ingestão:** tabelas `TAB_VENDA_ITEM`, `TAB_VENDA` e `TAB_PRODUTO` do banco legado **HFSQL**, lidas via ODBC
- **Saneamento:** exclusão de vendas inválidas e canceladas e de cestas com um único item
- **Funil de PLN:** Regex para remover unidades de medida e **RapidFuzz** (`token_sort_ratio`) para agrupar variações de grafia em um "Produto Mestre"
- **Modelagem:** o **Apriori** estourou a memória (`MemoryError`, ~10 GiB) e foi substituído pelo **FP-Growth** (MLxtend)
- **Métricas:** Suporte, Confiança e Lift
- **Deploy:** microsserviço **FastAPI** assíncrono com busca *fuzzy* (`/api/busca`, `/api/recomendar`)

**Resultados:**

| Indicador | Valor |
|---|---|
| SKUs originais → Produtos Mestres | **5.051 → 1.938** (−61,63%) |
| Transações multi-item usadas no treino | **8.625** |
| Regras de associação geradas | **2.004** |
| Esparsidade original da matriz | **99,94%** |

**Artefatos:** [RecVendasv3.ipynb](PI5_Recomendacao/RecVendasv3.ipynb) · [EDA.ipynb](PI5_Recomendacao/EDA/EDA.ipynb) · [RecVendasv4_ML_Completo.ipynb](PI5_Recomendacao/EDA/RecVendasv4_ML_Completo.ipynb) · [Base de Dados.txt](<PI5_Recomendacao/Base de Dados.txt>) · [Deploy Guide.pdf](<PI5_Recomendacao/Deploy Guide.pdf>) · Relatório Final, Manual do Usuário e apresentações (PDF na pasta)

---

## 🚀 PI6 — Revolução Tecnológica: Databricks, MLOps e Streamlit
**📁 [PI6_Databricks_MLOps](PI6_Databricks_MLOps) · Berto Ferramentas**

**Problema:** o motor do PI5 funcionava em notebooks isolados, sem governança centralizada dos dados e sem registro dos experimentos.

**Soluções e técnicas:**
- **Engenharia de dados distribuída:** **PySpark** com tabelas gerenciadas no **Unity Catalog / Hive Metastore** ([1_Catalogo.ipynb](PI6_Databricks_MLOps/SRC/1_Catalogo.ipynb))
- **MLOps com MLflow:** Tracking e Model Registry. A execução `Treinamento_Recomendador` é parametrizada com suporte e lift mínimos, e as regras ficam salvas no Unity Catalog ([2_Sistema_Recomendacao_Clean.ipynb](PI6_Databricks_MLOps/SRC/2_Sistema_Recomendacao_Clean.ipynb))
- **Benchmark registrado:** experimento `Comparativo_Apriori_vs_FPGrowth`, com tempo de execução e pico de memória medidos via `tracemalloc` ([Apriori _FpGrowth PI6.ipynb](<PI6_Databricks_MLOps/TEST/Apriori _FpGrowth PI6.ipynb>))
- **Deep Learning:** Filtragem Colaborativa Neural (**NCF**) com **PyTorch**
- **Aplicação Streamlit** ([app.py](PI6_Databricks_MLOps/APP/app.py)), "Inteligência de Venda" v3.2:
  - Copia automaticamente os artefatos do Workspace Databricks (`db_conhecimento.parquet`, `catalogo_busca.parquet`, `catalogo_detalhado.pkl`, `metadata.json`). Se a cópia falhar, continua com os arquivos locais, então o app funciona offline
  - Mantém o catálogo em RAM com `@st.cache_resource`
  - Oferece duas abas de busca: **Busca Rápida (Autocomplete)** e **Digitação Livre**
  - Mostra as **4 melhores recomendações** ordenadas por confiança e lift, com as opções em estoque (SKUs) de cada Produto Mestre

**Como executar o app:**

```bash
cd PI6_Databricks_MLOps/APP
pip install -r requirements.txt   # streamlit~=1.38.0, pandas~=2.2.3
streamlit run app.py
```

> [!NOTE]
> O app espera encontrar na pasta `APP/data/` o arquivo `LOGO.PNG` e os artefatos gerados pelos notebooks de `SRC/`. Esses arquivos não estão versionados.

**Artefatos:** notebooks em [SRC](PI6_Databricks_MLOps/SRC), [EDA](PI6_Databricks_MLOps/EDA) e [TEST](PI6_Databricks_MLOps/TEST) · Guia de Implantação, Manual do Usuário e Propriedade Intelectual (PDF na pasta)

---

## 📈 Radar de Maturidade por Competência

| Eixo / Competência | PI1 | PI2 | PI3 | PI4 | PI5 | PI6 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|
| **Visão de Negócios & Estratégia** | Avançado | Especialista | Especialista | Especialista | Especialista | Especialista |
| **Engenharia de Dados (ETL/ELT)** | Básico | Intermediário | Avançado | Especialista | Especialista | Especialista |
| **Modelagem Analítica & ML** | — | Básico | — | — | Especialista | Especialista |
| **Processamento de Texto (PLN)** | — | — | Intermediário | — | Especialista | Especialista |
| **Deploy & MLOps** | — | — | Intermediário | Avançado | Especialista | Especialista |

---

## 🛠️ Stack Tecnológica Consolidada

| Categoria | Ferramentas |
|---|---|
| **Linguagens** | Python, R, SQL |
| **Manipulação e Análise** | Pandas, NumPy, Faker |
| **Visualização / BI** | Matplotlib, Plotly, Folium, Power BI, Qlik Sense, Streamlit |
| **Engenharia de Dados** | PyMuPDF, pdfplumber, pytesseract (OCR), SQLAlchemy, pypyodbc (HFSQL), PySpark |
| **PLN** | Regex, RapidFuzz |
| **Machine Learning / DL** | MLxtend (Apriori, FP-Growth), PyTorch (NCF) |
| **MLOps / Plataforma** | Databricks, Unity Catalog, MLflow (Tracking & Registry) |
| **Deploy** | FastAPI, Uvicorn, Streamlit |
| **Gestão** | PMBOK, MS Project, Scrum, Trello, JIRA, Confluence, GitHub |
| **Negócios** | SWOT, BSC, Business Model Canvas, Project Model Canvas, Design Thinking, 5W2H, SMART |

---

## 👤 Autor

**Michel Cirilo de Oliveira**
Tecnólogo em Ciência de Dados para Negócios — Fatec Votorantim
🔗 [github.com/MichelCirilo](https://github.com/MichelCirilo)

### Agradecimentos
- **Prof. Me. Hélio Rubens Jacintho Pereira Junior**, orientador
- **Berto Ferramentas** (Eric Berto, Product Owner), empresa parceira dos PIs 4, 5 e 6
- **Regional 11 – Centro Paula Souza**, parceira do PI3
- Corpo docente e colegas de equipe do curso de Ciência de Dados para Negócios

### Publicação
OLIVEIRA, M. C.; PIVA JUNIOR, D.; NUNES, R. H.; PEREIRA JUNIOR, H. R. J. *A evolução de um cientista de dados: uma jornada evolutiva na prática através de portfólio integrador.* In: **I Simpósio de Ciência de Dados das Fatecs**, Santos: Fatec Rubens Lara, 2026.

---

## 📄 Licença e Observações

- Projeto acadêmico desenvolvido na **Fatec Votorantim (CEETEPS)**.
- Os dados, códigos e artefatos dos PIs 4, 5 e 6 pertencem à **Berto Ferramentas**, e seu uso depende de autorização da empresa.
- 🔐 Credenciais, bases de dados brutas e informações sensíveis **não** estão neste repositório.

---

<p align="center"><i>"nós somos máquinas de sentimentos, e é justamente essa biologia que desperta a nossa consciência e as nossas emoções; em contrapartida, a Inteligência Artificial opera no espectro oposto: são máquinas frias de pensamento que, desprovidas de emoções e baseadas apenas em processamento de dados, tentam simular o sentir."</i></p>
