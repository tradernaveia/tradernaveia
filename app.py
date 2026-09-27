import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(
    page_title="Tradernaveia - Plataforma de Estudos",
    page_icon="📈",
    layout="wide"
)

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

def tela_login():
    st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>TRADERNAVEIA - ACESSO RESTRITO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Insira suas credenciais para acessar o ambiente de estudos.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("form_login"):
            usuario = st.text_input("Usuário")
            senha = st.text_input("Senha", type="password")
            botao_entrar = st.form_submit_button("Entrar na Plataforma", use_container_width=True)
            
            if botao_entrar:
                if usuario == "Tradernaveia" and senha == "Jvc@2009":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos. Tente novamente.")

def plataforma_estudos():
    st.sidebar.title("🚀 Tradernaveia")
    st.sidebar.markdown("Painel de Estudos & Simulação ao Vivo")
    st.sidebar.markdown("---")
    
    ativos_dict = {
        "Ouro (Gold)": "GC=F",
        "Bitcoin (BTC)": "BTC-USD",
        "S&P 500 (US500)": "^GSPC",
        "Nasdaq (UT100)": "^IXIC",
        "Mini Índice (Proxy EWZ)": "EWZ",
        "Mini Dólar (Proxy USDBRL)": "USDBRL=X"
    }
    
    ativo_escolhido = st.sidebar.selectbox("Selecione o Ativo:", list(ativos_dict.keys()))
    ticker_simbolo = ativos_dict[ativo_escolhido]
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Sair da Plataforma", use_container_width=True):
        st.session_state["autenticado"] = False
        st.rerun()

    st.title(f"📊 Cotação Online: {ativo_escolhido}")
    st.markdown(f"A monitorizar o ativo {ticker_simbolo} em tempo real para validação de setups e price action.")
    
    try:
        dados = yf.Ticker(ticker_simbolo)
        hist = dados.history(period="5d", interval="1h")
        
        if not hist.empty:
            ultimo_preco = hist['Close'].iloc[-1]
            preco_anterior = hist['Close'].iloc[-2]
            variacao = ((ultimo_preco - preco_anterior) / preco_anterior) * 100
            
            col_m1, col_m2 = st.columns(2)
            col_m1.metric(label="Último Preço Registado", value=f"{ultimo_preco:,.2f}", delta=f"{variacao:.2f}%")
            col_m2.success("Ligação à Fonte de Dados Online Ativa")
            
            st.subheader("Gráfico de Variação Recente")
            st.line_chart(hist['Close'])
        else:
            st.warning("A aguardar atualização de cotação para este símbolo.")
    except Exception as e:
        st.error(f"Erro ao carregar dados online: {e}")
    
    tab1, tab2, tab3 = st.tabs(["Painel Operacional", "Registro de Setups (Backtest)", "Anotações do Dia"])
    
    with tab1:
        st.subheader("Dinâmica e Setups")
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("📌 Gráfico Temporal (Ex: 2 min / Setups de Corzinha)\n\nMonitoramento de gatilhos rápidos e rompimentos imediatos.")
        with col_b:
            st.success("🎯 Gráfico de Pontos (Ex: 10P)\n\nLeitura limpa de agressão, blocos de pontuação e alvos fixos.")

    with tab2:
        st.subheader("Diário de Validação de Alvos")
        with st.form("form_backtest"):
            col1, col2, col3 = st.columns(3)
            with col1:
                pontos = st.number_input("Pontos Alvo / Realizados", value=500, step=50)
            with col2:
                contratos = st.number_input("Qtd Contratos", value=1, step=1)
