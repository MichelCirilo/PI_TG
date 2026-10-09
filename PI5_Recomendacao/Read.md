# Projeto Integrador V: Sistema de Recomendação Inteligente (Berto Ferramentas)

> Solução end-to-end de Ciência de Dados para automatizar a sugestão de itens complementares (*cross-selling*) durante a criação de orçamentos, visando o aumento do *ticket* médio.

---

## 📋 Visão Geral

Este projeto tem como objetivo desenvolver uma solução completa de Ciência de Dados, abrangendo todo o ciclo de vida analítico: desde a ingestão e tratamento dos dados de vendas até a construção, avaliação e disponibilização de um modelo de recomendação preditivo.

A solução foi projetada para apoiar a tomada de decisão baseada em dados, utilizando técnicas de Análise de Cesta de Compras (*Market Basket Analysis*), extração de regras de associação e Processamento de Linguagem Natural (Fuzzy Matching) para agilizar o atendimento da equipe de vendas.

---

## 🎯 Problema de Negócio

A Berto Ferramentas precisa evoluir sua capacidade analítica de uma perspectiva focada no passado (Projeto "Faturômetro") para uma visão voltada para o futuro (análise preditiva). Atualmente, a identificação de itens complementares durante uma venda depende exclusivamente da memória e experiência do vendedor, o que leva a falhas por esquecimento e à perda de oportunidades de venda.

### Contexto
- **Cenário:** Processo de elaboração de orçamentos e atendimento ao cliente na Berto Ferramentas (focando em se tornar a referência absoluta na zona oeste de Sorocaba).
- **Impactados:** Equipe de vendas (que ganha uma ferramenta de apoio inteligente) e clientes (que recebem um atendimento mais completo e ágil).
- **Decisão Apoiada:** Quais produtos complementares devem ser oferecidos ao cliente no momento exato em que um item base é adicionado ao orçamento (*cross-selling* ativo).

---

## 💡 Solução Proposta

Desenvolvimento do **"Sistema de Recomendação por Afinidade — v3.0"**, um motor de regras de associação integrado diretamente na interface de vendas.

### Tipo de Solução
Sistema de Recomendação (Regras de Associação / *Market Basket Analysis*)

### Abordagem Técnica
Utilização do algoritmo **FP-Growth** para identificar padrões de compra frequentes com base no histórico de transações, agrupando variações de texto de produtos através de expressões regulares (*Regex*) e correspondência difusa (*Fuzzy Match*).

### Diferenciais da Solução
- ✅ **Substituição do Apriori pelo FP-Growth:** Garantindo maior eficiência e rapidez no processamento de grandes volumes de dados
- ✅ **Integração da biblioteca `RapidFuzz`:** Métrica `token_sort_ratio` para unificar variações tipográficas e ignorar a ordem das palavras, criando um "Produto Mestre"
- ✅ **API com fuzzy match nativo:** Permite que o vendedor pesquise os produtos de forma aproximada, sem exigir a digitação exata
- ✅ **Tolerância a erros:** Sistema robusto que compreende abreviações e erros de digitação

---

## 🏗️ Arquitetura da Solução

```
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────────────┐
│  Banco de Dados │────▶│ Extração &       │────▶│ Agrupamento Semântico    │
│     (HFSQL)     │     │ Tratamento       │     │ (Regex + Fuzzy Match)    │
└─────────────────┘     │   (Pandas)       │     └──────────────────────────┘
                        └──────────────────┘                  │
                                                              ▼
┌─────────────────┐     ┌──────────────────┐     ┌──────────────────────────┐
│ API REST        │◀────│  Motor de Regras │◀────│  Produto Mestre          │
│   (FastAPI)     │     │   (FP-Growth)    │     │                          │
└─────────────────┘     └──────────────────┘     └──────────────────────────┘
        │
        ▼
┌─────────────────┐
│  Interface do   │
│    Vendedor     │
└─────────────────┘
```

---

## 🔄 Pipeline de Dados

### 1. Ingestão e Tratamento (ETL)
- Coleta de dados das tabelas `TAB_VENDA_ITEM`, `TAB_VENDA` e `TAB_PRODUTO` via banco de dados HFSQL
- Limpeza e tratamento de inconsistências (remoção de colunas vazias, variáveis constantes e registros de vendas inválidas ou canceladas)
- Exclusão de transações com valores zerados
- Utilização de blocos `try/finally` para garantir a integridade e o fechamento correto da conexão com o banco de dados

### 2. Análise Exploratória (EDA)
- Análise de frequência de venda por produto (estatísticas descritivas)
- Identificação de padrões de compra em conjunto (transações multi-item)
- Implementação de uma célula de diagnóstico para calibrar o *threshold* (limiar) de suporte antes de executar o motor de regras

### 3. Engenharia de Features
- **Criação do "Produto Mestre":** Aplicação de *Regex* para a limpeza inicial de nomenclaturas e padronização
- **Fuzzy Matching:** Utilização do `RapidFuzz` como *scorer* (focado no `token_sort_ratio`) para unificar produtos idênticos escritos de forma diferente no banco
- Seleção do nome "canônico" (oficial) de cada produto mestre com base na sua frequência no catálogo
- Mapeamento de nomes otimizado via dicionário, garantindo complexidade de busca O(1)

### 4. Modelagem
- **Algoritmo de Machine Learning:** FP-Growth (*Frequent Pattern Growth*)
- Extração de regras de associação (identificação de antecedentes e consequentes completos para regras multi-item)
- Geração da base de conhecimento (catálogo de busca consolidado e as regras de afinidade geradas)

### 5. Avaliação
Em sistemas de recomendação por regras de associação, as métricas de avaliação diferem da classificação tradicional:

- **Suporte (Support):** Frequência com que os itens aparecem juntos no histórico de transações
- **Confiança (Confidence):** Probabilidade de o item B ser comprado, dado que o item A já foi adicionado ao orçamento
- **Lift (Sustentação):** Força da associação entre os itens, indicando o quanto a venda conjunta supera a probabilidade de compra aleatória

### 6. Deploy
- **Arquitetura:** Microsserviço assíncrono
- **Disponibilização:** API REST desenvolvida em **FastAPI** e servida via **Uvicorn** (rodando localmente na porta 8000)
- A interface de vendas consulta a API, que por sua vez utiliza o catálogo indexado para devolver sugestões de *cross-selling* em tempo real

---

## 🛠️ Tecnologias Utilizadas

### Core
- **Linguagem:** Python 3.10+
- **Machine Learning:** FP-Growth (via MLxtend) substituindo o Apriori
- **PLN:** RapidFuzz (correspondência de *strings*) e Regex nativo

### Infraestrutura
- **Banco de Dados:** HFSQL
- **Manipulação de Dados:** Pandas (métodos otimizados como `map()`)
- **API:** FastAPI, Uvicorn, Asyncio
- **Gestão de Projeto:** JIRA (Atlassian)
- **Documentação:** Microsoft PowerPoint (Kickoff), Confluence (Documentação técnica completa)

---

## 📊 Resultados e Insights

### Impacto Técnico
- **Redução de Dimensão:** De 5.051 SKUs originais para 1.938 "Produtos Mestres" (redução de 61,63%)
- **Regras Geradas:** 2.004 regras de associação de alta confiabilidade
- **Transações Processadas:** 8.625 vendas multi-item utilizadas no treinamento
- **Esparsidade Mitigada:** De 99,94% para níveis operacionais através do funil de PLN

### Impacto no Negócio
- **Aumento do Ticket Médio:** Através do estímulo orgânico a compras complementares
- **Otimização Operacional:** Redução do tempo de elaboração de orçamentos e eliminação de erros por esquecimento humano
- **Experiência do Usuário:** Busca difusa permite encontrar produtos rapidamente mesmo com falhas de digitação
- **Catálogo Otimizado:** Mapeamento de "Produtos Mestres" limpou a redundância da base de dados histórica

---

## 📅 Gestão de Projeto com JIRA

O projeto foi gerenciado através da plataforma **JIRA** (Atlassian), garantindo organização, transparência e rastreabilidade de todas as atividades.

### Estrutura no JIRA
- **Projeto:** PI5 - Sistema de Recomendação por Afinidade
- **Metodologia:** Scrum com sprints de 2 semanas
- **Visualizações:** Cronograma (Gantt), Backlog, Quadro Kanban

### Sprints e Principais Issues
- **Sprint 1:** Extração de dados, tratamento e EDA
  - Kick Off do projeto
  - ETL (Extração, Transformação e Carga)
  
- **Sprint 2:** Engenharia de Features e PLN
  - Implementação de Regex e Fuzzy Match
  - Criação do "Produto Mestre"
  
- **Sprint 3:** Treinamento do Modelo
  - Modelo ML (Implementação do FP-Growth)
  
- **Sprint 4:** Deploy e Documentação
  - Deploy e disponibilização da API
  - Documentação técnica e acadêmica
  - Gestão de Projeto

### Benefícios do JIRA
- ✅ Transparência em tempo real do status do projeto
- ✅ Comunicação assíncrona através de comentários nas issues
- ✅ Histórico documentado de todo o ciclo de vida do projeto
- ✅ Acompanhamento facilitado por orientadores e empresa parceira

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.10+ instalado
- Gerenciador de pacotes (pip ou conda)
- Acesso ao banco de dados HFSQL (credenciais configuradas no ambiente)

### Instalação

```bash
# Clonar o repositório
git clone [URL_DO_REPOSITORIO]

# Acessar a pasta do projeto
cd BertoFerramentas_Recomendacao

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Dependências Principais

```txt
rapidfuzz>=3.0.0
mlxtend>=0.23.0
fastapi>=0.104.0
uvicorn>=0.24.0
nest-asyncio>=1.5.8
pandas>=2.0.0
pypyodbc>=1.3.2
```

### Executar a Aplicação (API)

```bash
# Executar o notebook para treinar o modelo e iniciar a API
jupyter notebook RecVendasv3.ipynb

# Ou executar diretamente via Python
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

A API estará disponível em: `http://localhost:8000`

### Endpoints da API

- **GET `/`** - Interface web interativa
- **GET `/api/busca?t={termo}`** - Busca produtos com fuzzy match
- **GET `/api/recomendar?item={produto_mestre}`** - Retorna recomendações para um produto

---

## 📂 Estrutura do Projeto

```
BertoFerramentas_Recomendacao/
├── RecVendasv3.ipynb          # Notebook principal com todo o pipeline
├── README.md                   # Este arquivo
├── requirements.txt            # Dependências do projeto
├── main.py                     # Script principal da API (opcional)
├── data/
│   ├── raw/                    # Dados brutos do HFSQL
│   └── processed/              # Dados processados e catálogos
├── models/
│   ├── catalogo_busca.pkl     # Catálogo de produtos indexados
│   ├── db_conhecimento.pkl    # Base de regras de associação
│   └── catalogo_detalhado.pkl # Mapeamento Mestre → SKUs
└── docs/
    ├── Confluence/             # Links para documentação no Confluence
    └── Kickoff.pptx           # Apresentação inicial do projeto
```

---

## 📖 Documentação

A documentação completa e detalhada do projeto está centralizada no **Confluence**:

- 📌 **Página Principal:**
- 📊 **Análises e EDA:**
- 🤖 **Modelos de Machine Learning (FP-Growth):**
- 🔤 **PLN (Regex e Fuzzy Match):**
- 🏗️ **Arquitetura e Deploy (FastAPI):**
- 📘 **Documentação Técnica / Manual:**

---

## 👥 Equipe

### Desenvolvimento
- **Michel Cirilo de Oliveira** - Analista de Dados / Desenvolvedor Principal
- **Eric Berto** - Sócio Proprietário Berto Ferramentas / Product Owner

### Instituição
- **Fatec Votorantim** - Faculdade de Tecnologia de Votorantim
- **Curso:** Ciência de Dados para Negócios
- **Projeto:** Projeto Integrador V (PI5)

---

## 📝 Observações Importantes

- ⚠️ Este repositório contém apenas o código-fonte (ex: `RecVendasv3.ipynb` e scripts da API) e arquivos essenciais do projeto
- 📚 A documentação completa e detalhada está centralizada no **Confluence**
- 🔒 Alterações estruturais no ERP da empresa ou aquisição de novo *hardware* foram excluídas do escopo inicial deste projeto
- 🔐 Credenciais e informações sensíveis não estão incluídas no repositório

---

## 🔜 Próximos Passos

### Implementação em Produção
1. **Testes Piloto:** Validação da interface com vendedores reais
2. **Calibração do Modelo:** Ajuste fino das métricas (threshold) baseado em feedback
3. **Integração Completa:** Conexão direta com o sistema de PDV da loja
4. **Monitoramento:** Dashboard de acompanhamento de performance das recomendações

### Melhorias Futuras
- 🔄 Retreinamento automático do modelo com novos dados
- 📱 Aplicativo mobile para vendedores externos
- 📈 Dashboard de analytics para gestão
- 🤖 Incorporação de algoritmos de Deep Learning (Redes Neurais)
- 🎯 Personalização de recomendações por perfil de cliente

---

## 📄 Licença

Este projeto é de propriedade da **Berto Ferramentas** e foi desenvolvido em parceria com a **Fatec Votorantim** como parte do Projeto Integrador V do curso de Ciência de Dados para Negócios.

---

## 📞 Contato

Para mais informações sobre o projeto, entre em contato através dos canais institucionais da Fatec Votorantim ou diretamente com a Berto Ferramentas.

---

**Versão:** 3.0  
**Última Atualização:** Maio 2026  
**Status:** ✅ Concluído e em fase de deploy
