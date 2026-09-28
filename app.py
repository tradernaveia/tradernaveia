import streamlit as st
import streamlit.components.v1 as components

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
    
    symbols = {
        "Ouro (Gold)": "COMEX:GC1!",
        "Mini Índice": "BMFBOVESPA:WIN1!",
        "Mini Dólar": "BMFBOVESPA:WDO1!",
        "Bitcoin": "BINANCE:BTCUSDT"
    }
    sym = symbols.get(ativo, "COMEX:GC1!")
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Sair"):
        st.session_state["autenticado"] = False
        st.rerun()

    st.title(f"📊 Painel Operacional: {ativo}")
    
    t1, t2, t3 = st.tabs(["📈 Gráfico Profissional", "🎯 Diário de Alvos", "📝 Anotações"])
    
    with t1:
        html_code = f"""
        <div style="height:530px;width:100%">
          <div id="tv_chart" style="height:100%;width:100%"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget({{
            "width": "100%", "height": "530", "symbol": "{sym}",
            "interval": "3", "timezone": "America/Sao_Paulo",
            "theme": "dark", "style": "1", "locale": "br", "container_id": "tv_chart"
          }});
          </script>
        </div>
        """
        components.html(html_code, height=550)
        
    with t2:
        st.subheader("Registo de Alvos")
        pts = st.number_input("Pontos Alvo", value=500, step=50)
        if st.button("Salvar Registo"):
            st.success(f"Alvo de {pts} pontos guardado para {ativo}!")
            
    with t3:
        st.subheader("Bloco de Notas")
        st.text_area("Anotações estratégicas do dia:", height=200)
