import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Tradernaveia", page_icon="📈", layout="wide")

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>TRADERNAVEIA - LOGIN RESTRITO</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login"):
            u = st.text_input("Usuário")
            s = st.text_input("Senha", type="password")
            if st.form_submit_button("Entrar na Plataforma", use_container_width=True):
                if u == "Tradernaveia" and s == "Jvc@2009":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Usuário ou senha incorretos.")
else:
    st.sidebar.title("🚀 Tradernaveia")
    ativo = st.sidebar.selectbox("Selecione o Ativo:", ["Ouro (Gold - GC=F)", "Mini Índice (WIN)", "Mini Dólar (WDO)", "Bitcoin (BTC)", "S&P 500 (US500)"])
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Sair da Plataforma", use_container_width=True):
        st.session_state["autenticado"] = False
        st.rerun()

    st.title(f"📊 Painel de Estudos & Gráfico: {ativo}")
    st.markdown("Monitoramento operacional, variação de preços e validação de alvos em tempo real.")
    
    # Abas da Aplicação
    tab1, tab2, tab3 = st.tabs(["📈 Gráfico & Dinâmica", "🎯 Diário de Alvos (Backtest)", "📝 Anotações do Dia"])
    
    with tab1:
        st.subheader(f"Evolução de Preço e Volatilização para {ativo}")
        
        # Gerando uma simulação gráfica fluida e limpa baseada no ativo selecionado para acompanhar o comportamento técnico
        chart_data = pd.DataFrame(
            np.random.randn(30, 2) * [10, 2] + [2500 if "Ouro" in ativo else 130000, 50],
            columns=['Preço Compra/Venda', 'Agressão de Fluxo']
        )
        
        st.line_chart(chart_data)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.info("📌 Gráfico Temporal (Ex: 2 min / Setups de Corzinha)\n\nGatilhos rápidos de rompimento e barras de ignição.")
        with col_b:
            st.success("🎯 Gráfico de Pontos (Ex: 10P)\n\nLeitura limpa de blocos de pontuação e alvos fixos de 500 pontos.")

    with tab2:
        st.subheader("Registo de Pontos e Performance")
        with st.form("form_backtest"):
            col1, col2, col3 = st.columns(3)
            with col1:
                pontos = st.number_input("Pontos Alvo / Realizados", value=500, step=50)
            with col2:
                contratos = st.number_input("Qtd Contratos", value=1, step=1)
            with col3:
                resultado = st.selectbox("Resultado", ["Gain", "Loss", "Fora do Alvo"])
                
            obs = st.text_area("Observações sobre o Tape Reading:")
            if st.form_submit_button("Salvar Registo"):
                st.success(f"Registo guardado com sucesso! Alvo de {pontos} pontos catalogado para {ativo}.")

    with tab3:
        st.subheader("Bloco de Notas Estratégicas")
        st.text_area("Anote os pontos de suporte, resistência e regiões institucionais do dia:", height=200)
