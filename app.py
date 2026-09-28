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
    ativo = st.sidebar.selectbox("Ativo:", ["Ouro (XAUUSD)", "Bitcoin (BTCUSD)", "S&P 500 (SPX)", "Nasdaq (IXIC)"])
    
    symbols = {
        "Ouro (XAUUSD)": "OANDA:XAUUSD",
        "Bitcoin (BTCUSD)": "BINANCE:BTCUSDT",
        "S&P 500 (SPX)": "SP:SPX",
        "Nasdaq (IXIC)": "NASDAQ:IXIC"
    }
    sym = symbols.get(ativo, "OANDA:XAUUSD")
    
    st.sidebar.markdown("---")
    if st.sidebar.button("Sair"):
        st.session_state["autenticado"] = False
        st.rerun()

    st.title(f"📊 Painel Operacional: {ativo}")
    
    # Abas organizadas incluindo os motores de cálculo de Pontos e Renko
    t1, t2, t3, t4 = st.tabs(["📈 Gráfico Profissional", "⚙️ Motor Pontos & Renko", "🎯 Diário de Alvos", "📝 Anotações"])
    
    with t1:
        html_code = f"""
        <div style="width:100%; height:550px;">
          <div id="tradingview_container" style="height:100%;width:100%"></div>
          <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
          <script type="text/javascript">
          new TradingView.widget({{
            "width": "100%",
            "height": "550",
            "symbol": "{sym}",
            "interval": "D",
            "timezone": "America/Sao_Paulo",
            "theme": "dark",
            "style": "1",
            "locale": "br",
            "toolbar_bg": "#f1f3f6",
            "enable_publishing": false,
            "allow_symbol_change": false,
            "container_id": "tradingview_container"
          }});
          </script>
        </div>
        """
        components.html(html_code, height=570)
        
    with t2:
        st.subheader("⚙️ Configuração e Simulação de Parâmetros Operacionais")
        
        col_m1, col_m2 = st.columns(2)
        
        with col_m1:
            st.markdown("### 🎯 Gráfico de Pontos")
            tamanho_bloco = st.number_input("Tamanho do Bloco de Pontos", value=100, step=10)
            alvo_pontos = st.number_input("Alvo Fixo Operacional (Ex: 500)", value=500, step=50)
            
            # Cálculo dinâmico de blocos para o alvo
            blocos_necessarios = alvo_pontos / tamanho_bloco if tamanho_bloco > 0 else 0
            st.info(f"📊 Leitura Ativa: Para atingir o alvo de {alvo_pontos} pontos com blocos de {tamanho_bloco}, serão necessários {blocos_necessarios:.1f} blocos direcionais limpos.")
            
        with col_m2:
            st.markdown("### 🧱 Gráfico Renko")
            brick_size = st.number_input("Tamanho do Tijolo (Brick)", value=10, step=1)
            reversao_bricks = st.selectbox("Regra de Reversão de Caixa", ["2 Bricks", "1 Brick"])
            
            st.success(f"🧱 Regra Ativa: Renko configurado com bricks de {brick_size} unidades e reversão de {reversao_bricks} para filtragem de ruído institucional no ativo {ativo}.")

    with t3:
        st.subheader("Registo de Alvos e Backtest")
streamlit
plotly
pandas
numpy
