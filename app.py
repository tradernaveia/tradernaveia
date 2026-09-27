
import streamlit as st

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
    st.sidebar.markdown("Painel de Estudos & Simulação")
    st.sidebar.markdown("---")
    
    ativo_selecionado = st.sidebar.selectbox(
        "Selecione o Ativo:",
        ["Mini Índice (WIN)", "Mini Dólar (WDO)", "Ouro", "Bitcoin (BTC)", "S&P 500 (US500)", "Nasdaq (UT100)", "Nikkei (JP225)", "Hang Seng (HK50)"]
    )
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Sair da Plataforma", use_container_width=True):
        st.session_state["autenticado"] = False
        st.rerun()

    st.title(f"📊 Ambiente de Estudos: {ativo_selecionado}")
    st.markdown("Foco total no operacional, leitura de fluxo, price action e validação de alvos.")
    
    tab1, tab2, tab3 = st.tabs(["Painel Operacional", "Registro de Setups (Backtest)", "Anotações do Dia"])
    
    with tab1:
        st.subheader("Configuração de Gráficos e Dinâmica")
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("📌 Gráfico Temporal (Ex: 2 min / Setups de Corzinha)\n\nMonitoramento de gatilhos rápidos e rompimentos imediatos.")
        with col_b:
            st.success("🎯 Gráfico de Pontos (Ex: 10P)\n\nLeitura limpa de agressão, blocos de pontuação e alvos fixos.")
            
        st.markdown("### Resumo do Ativo Atual")
        st.metric(label="Status do Módulo", value="Ativo & Sincronizado", delta="Pronto para simulação")

    with tab2:
        st.subheader("Diário de Validação de Alvos")
        with st.form("form_backtest"):
            col1, col2, col3 = st.columns(3)
            with col1:
                pontos = st.number_input("Pontos Alvo / Realizados", value=500, step=50)
            with col2:
                contratos = st.number_input("Qtd Contratos", value=1, step=1)
            with col3:
                resultado = st.selectbox("Resultado do Estudo", ["Gain", "Loss", "Empate / Fora do Alvo"])
                
            observacao = st.text_area("Observações sobre o Tape Reading / Rompimento:")
            salvar_registro = st.form_submit_button("Salvar Registro de Estudo")
            
            if salvar_registro:
                st.success(f"Registro salvo com sucesso! Alvo de {pontos} pontos catalogado para {ativo_selecionado}.")

    with tab3:
        st.subheader("Bloco de Notas Estratégicas")
        st.text_area("Anote aqui os pontos de suporte, resistência e regiões de briga institucional do dia:", height=200)

if not st.session_state["autenticado"]:
    tela_login()
else:
    plataforma_estudos()
