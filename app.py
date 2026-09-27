import streamlit as st

st.set_page_config(page_title="Tradernaveia", page_icon="📈", layout="wide")

if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>TRADERNAVEIA - LOGIN</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("login"):
            u = st.text_input("Usuário")
            s = st.text_input("Senha", type="password")
            if st.form_submit_button("Entrar", use_container_width=True):
                if u == "Tradernaveia" and s == "Jvc@2009":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("Dados incorretos.")
else:
    st.sidebar.title("🚀 Tradernaveia")
    ativo = st.sidebar.selectbox("Ativo:", ["Ouro (Gold)", "Mini Índice", "Mini Dólar", "Bitcoin"])
    if st.sidebar.button("Sair"):
        st.session_state["autenticado"] = False
        st.rerun()

    st.title(f"📊 Painel Operacional: {ativo}")
    st.info("Plataforma ativa e sincronizada para estudos e validação de alvos.")
    
    tab1, tab2 = st.tabs(["Painel de Alvos", "Notas"])
    with tab1:
        st.subheader("Registo de Pontos")
        p = st.number_input("Pontos Alvo", value=500, step=50)
        if st.button("Salvar Alvo"):
            st.success(f"Alvo de {p} pontos registado para {ativo}!")
    with tab2:
        st.text_area("Anotações do dia:", height=150)
