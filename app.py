import streamlit as st
import streamlit.components.v1 as components

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
    ativo = st.sidebar.selectbox("Selecione o Ativo:", ["Ouro (Gold)", "Mini Índice (WIN)", "Mini Dólar (WDO)", "Bitcoin (BTC)", "S&P 500 (US500)"])
    
    # Mapeamento dos símbolos profissionais para o gráfico
    tv_symbols = {
        "Ouro (Gold)": "COMEX:GC1!",
        "Mini Índice (WIN)": "BMFBOVESPA:WIN1!",
        "Mini Dólar (WDO)": "BMFBOVESPA:WDO1!",
        "Bitcoin (BTC)": "BINANCE:BTCUSDT",
        "S&P 500 (US500)": "SP:SPX"
    }
    symbol = tv_symbols.get(ativo, "COMEX:GC1!")
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Sair da Plataforma", use_container_width=True):
        st.session_state["autenticado"] = False
        st.rerun()

    st.title(f"📊 Painel Operacional & Gráfico: {ativo}")
    
    tab1, tab2, tab3 = st.tabs(["📈 Gráfico Profissional", "🎯 Diário de Alvos (Backtest)", "📝 Anotações do Dia"])
    
    with tab1:
        # Incorporando o gráfico profissional avançado do TradingView
        tradingview_html = f"""
        <div class="tradingview-widget-container" style="height:550px;width:100%">
          <div id="tradingview_chart" style="height:100%;width:100%"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget(
          {{
            "width": "100%",
            "height": "550",
            "symbol": "{symbol}",
            "interval": "D",
            "timezone": "America/Sao_Paulo",
            "theme": "dark",
            "style": "1",
            "locale": "br",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "allow_symbol_change": true,
            "container_id": "tradingview_chart"
          }});
          </script>
        </div>
        """
        components.html(tradingview_html, height=570)
        
        st.markdown("<br>", unsafe_allow_html=True)
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
                pontos = st.number_input("Pontos Alvo / Realizados", value=500, step50=50) if hasattr(st, 'number_input') else st.number_input("Pontos Alvo / Realizados", value=500, step=50)
            with col2:
                contratos = st.number_input("Qtd Contratos", value=1, step=1)
            with col3:
                resultado = st.selectbox("Resultado", ["Gain", "Loss", "Fora do Alvo"])
                
            obs = st.text_area("Observações sobre o Tape Reading:")
            if st.form_submit_button("Salvar Registo"):
                st.success(f"Registo guardado com sucesso! Alvo catalogado para {ativo}.")
