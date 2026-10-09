
import os
import shutil
import pickle
import pandas as pd
import json
import streamlit as st
from PIL import Image

# Monta o caminho exato usando o diretório atual do app.py + pasta data + nome do arquivo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_logo = os.path.join(diretorio_atual, "data", "LOGO.PNG")

logo = Image.open(caminho_logo)

# ============================================================
# 1. AUTO-SETUP: COPIA DOS ARQUIVOS DO WORKSPACE PARA O APP
# ============================================================
CAMINHO_ORIGEM = "/Workspace/Users/michelcirilo@hotmail.com/sistema_recomendacao"
CAMINHO_DESTINO_LOCAL = "./data"

os.makedirs(CAMINHO_DESTINO_LOCAL, exist_ok=True)

arquivos_para_copiar = [
    "db_conhecimento.parquet",
    "catalogo_busca.parquet",
    "catalogo_detalhado.pkl",
    "metadata.json"
]

for arquivo in arquivos_para_copiar:
    origem = os.path.join(CAMINHO_ORIGEM, arquivo)
    destino = os.path.join(CAMINHO_DESTINO_LOCAL, arquivo)
    if os.path.exists(origem):
        try:
            shutil.copy(origem, destino)
        except Exception:
            pass

# ============================================================
# 2. CONFIGURAÇÃO DA PÁGINA (TELA CHEIA E COMPACTA)
# ============================================================
st.set_page_config(
    page_title="Inteligência de Venda",
    page_icon=logo, # Aqui a logo vai para a aba do navegador
    layout="wide"
)

# CSS injetado para reduzir margens nativas do Streamlit e economizar espaço vertical
st.markdown("""
    <style>
        .block-container { padding-top: 2rem !important; padding-bottom: 1rem !important; }
        div.stButton > button { width: 100%; padding: 4px 10px; }
        .stTabs [data-baseweb="tab-list"] { gap: 10px; }
        .stTabs [data-baseweb="tab"] { padding: 6px 16px; }
    </style>
""", unsafe_allow_html=True)

# ============================================================
# 3. CARREGAMENTO DOS DADOS COM CACHE
# ============================================================
@st.cache_resource
def carregar_dados_locais():
    caminho_conhecimento = os.path.join(CAMINHO_DESTINO_LOCAL, "db_conhecimento.parquet")
    caminho_busca = os.path.join(CAMINHO_DESTINO_LOCAL, "catalogo_busca.parquet")
    caminho_detalhado = os.path.join(CAMINHO_DESTINO_LOCAL, "catalogo_detalhado.pkl")
    caminho_metadata = os.path.join(CAMINHO_DESTINO_LOCAL, "metadata.json")
    
    if not (os.path.exists(caminho_conhecimento) and os.path.exists(caminho_busca) and os.path.exists(caminho_detalhado)):
        st.error("⚠️ Arquivos de dados ausentes no diretório local do App.")
        st.stop()
            
    db_conhecimento = pd.read_parquet(caminho_conhecimento)
    catalogo_busca = pd.read_parquet(caminho_busca)
    
    with open(caminho_detalhado, 'rb') as f:
        catalogo_detalhado = pickle.load(f)
    
    # Carrega metadados (se existir)
    metadata = None
    if os.path.exists(caminho_metadata):
        with open(caminho_metadata, 'r') as f:
            metadata = json.load(f)
        
    return db_conhecimento, catalogo_busca, catalogo_detalhado, metadata

db_conhecimento, catalogo_busca, catalogo_detalhado, metadata = carregar_dados_locais()
catalogo_busca_limpo = catalogo_busca.dropna(subset=['nome', 'mestre'])

# ============================================================
# 4. ÁREA SUPERIOR: BUSCA (LARGURA TOTAL)
# ============================================================
col_logo, col_titulo = st.columns([1, 15]) 

with col_logo:
    # Exibe a logo na tela (ajuste o width se achar que ficou muito grande ou pequena)
    st.image(logo, width=50) 

with col_titulo:
    # Título alinhado à esquerda para acompanhar a logo
    st.markdown("<h2 style='text-align: left; margin-top: -15px; margin-bottom: 0px;'>Sistema de Recomendação</h2>", unsafe_allow_html=True)

# O subtítulo continua embaixo, também alinhado à esquerda
if metadata:
    data_atualizacao = metadata.get('data_atualizacao', 'Não disponível')
    st.markdown(f"<p style='text-align: left; color: gray; margin-bottom: 20px;'>FP-Growth · Recomendações de Associação v3.2 | 📅 Última atualização: {data_atualizacao}</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='text-align: left; color: gray; margin-bottom: 20px;'>FP-Growth · Recomendações de Associação v3.2</p>", unsafe_allow_html=True)

# Container de Busca bem compacto no topo
with st.container(border=True):
    tab_auto, tab_livre = st.tabs(["⚡ Busca Rápida (Autocomplete)", "📝 Digitação Livre"])
    
    with tab_auto:
        opcoes_produtos = sorted(catalogo_busca_limpo['nome'].unique().tolist())
        produto_escolhido = st.selectbox(
            "Selecione ou digite o nome do produto:",
            options=opcoes_produtos,
            index=None,
            placeholder="Comece a digitar... (Ex: Chave, Parafuso, Filtro)",
            label_visibility="collapsed",
            key="busca_auto"
        )
        
        if produto_escolhido:
            linhas_filtradas = catalogo_busca_limpo[catalogo_busca_limpo['nome'] == produto_escolhido]
            if not linhas_filtradas.empty:
                # CORREÇÃO DA INDEXAÇÃO: Uso correto do .iloc[0] para obter a linha correta
                st.session_state['produto_selecionado'] = linhas_filtradas['mestre'].iloc[0]
                st.session_state['nome_exibicao'] = linhas_filtradas['nome'].iloc[0]
            
    with tab_livre:
        # CORREÇÃO DA LINHA 102: Passando a proporção [2, 1] explicitamente para as colunas
        col_input, col_info = st.columns([2, 1])
        with col_input:
            termo_busca = st.text_input(
                "Digite parte do nome:",
                placeholder="Ex: trena, oleo, fita...",
                label_visibility="collapsed",
                key="busca_texto"
            )
        
        if len(termo_busca) >= 2:
            resultados = catalogo_busca_limpo[
                catalogo_busca_limpo['nome'].str.lower().str.contains(termo_busca.lower(), na=False)
            ].head(8)
            
            if not resultados.empty:
                with col_info:
                    st.caption("Resultados sugeridos:")
                # Exibe pequenos botões lado a lado para economizar espaço vertical
                cols_botoes = st.columns(4)
                for i, (_, row) in enumerate(resultados.iterrows()):
                    col_idx = i % 4
                    with cols_botoes[col_idx]:
                        if st.button(f"📌 {row['nome'][:20]}...", key=f"btn_prod_{i}", help=row['nome']):
                            st.session_state['produto_selecionado'] = row['mestre']
                            st.session_state['nome_exibicao'] = row['nome']
                            st.rerun()
            else:
                st.warning("Nenhum produto correspondente.")

# ============================================================
# 5. ÁREA INFERIOR: PAINEL DE RESULTADOS (GRID HORIZONTAL)
# ============================================================
st.write("") 

if 'produto_selecionado' in st.session_state:
    mestre = st.session_state['produto_selecionado']
    nome_exibicao = st.session_state['nome_exibicao']
    
    st.success(f"Análise ativa para o item selecionado: **{nome_exibicao}**")
    
    regras_filtradas = db_conhecimento[db_conhecimento['busca'] == mestre]
    
    if not regras_filtradas.empty:
        recomendacoes = regras_filtradas.sort_values(
            ['confianca_num', 'lift'], ascending=False
        ).head(4) # Limitado a 4 para caber perfeitamente lado a lado na tela
        
        st.markdown("### 💡 Itens frequentemente comprados juntos (Venda Casada):")
        
        # Cria colunas horizontais baseadas na quantidade de recomendações
        colunas_grid = st.columns(len(recomendacoes))
        
        for idx, (col_bucket, (_, rec)) in enumerate(zip(colunas_grid, recomendacoes.iterrows())):
            recomendado = rec['recomendado']
            confianca = int(rec['confianca_num'] * 100)
            lift = float(rec['lift'])
            
            with col_bucket:
                # Container individual compacto para cada recomendação
                with st.container(border=True):
                    st.markdown(f"**🎁 {recomendado[:25]}**", help=recomendado)
                    
                    # Exibe métricas de confiança e lift de forma compacta
                    st.metric(label="Confiança", value=f"{confianca}%", delta=f"Lift: {lift:.2f}")
                    
                    # Lista de estoque expansível: mostra a quantidade exata no título do botão
                    itens_possiveis = catalogo_detalhado.get(recomendado, [])
                    if itens_possiveis:
                        with st.expander(f"📦 Opções em Estoque ({len(itens_possiveis)})", expanded=False):
                            for item in itens_possiveis:
                                st.caption(f"• {item}")
    else:
        st.warning("Nenhuma regra de associação forte foi mapeada para este item nos dados históricos.")
else:
    st.info("💡 Escolha um produto no painel de busca acima para visualizar as sugestões de venda casada.") 
    
 