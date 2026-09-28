point_values = np.cumsum(np.random.randn(25) * 40 + 15)
            
            fig_points = go.Figure(data=[go.Scatter(
                y=point_values, mode='lines+markers',
                line=dict(color='#29B6F6', width=3),
                marker=dict(size=8, color='#FFD54F')
            )])
            fig_points.update_layout(
                title=f"Gráfico de Pontos ({tamanho_bloco} pts) - Alvo: {alvo_pontos} pts",
                plot_bgcolor="#0e1117", paper_bgcolor="#0e1117",
                font_color="white", height=420,
                xaxis_title="Passos Operacionais", yaxis_title="Pontuação"
            )
            st.plotly_chart(fig_points, use_container_width=True)

    with t3:
        st.subheader("Registo de Alvos e Backtest")
        with st.form("form_backtest"):
            col1, col2, col3 = st.columns(3)
            with col1:
                pts = st.number_input("Pontos Alvo / Realizados", value=500, step=50)
            with col2:
                contratos = st.number_input("Contratos", value=1, step=1)
            with col3:
                res = st.selectbox("Resultado", ["Gain", "Loss", "Fora do Alvo"])
                
            obs = st.text_area("Observações do Tape Reading / Setup:")
            if st.form_submit_button("Guardar Registo"):
                st.success(f"Registo de {pts} pontos guardado com sucesso para {ativo}!")
            
    with t4:
        st.subheader("Bloco de Notas Estratégicas")
        st.text_area("Anote os pontos de suporte, resistência e regiões institucionais do dia:", height=200)
