with tab3:
        st.subheader("Diário de Validação de Alvos")
        with st.form("form_backtest"):
            col1, col2, col3 = st.columns(3)
            with col1:
                pontos = st.number_input("Pontos Alvo / Realizados", value=500, step=50)
            with col2:
                contratos = st.number_input("Qtd Contratos", value=1, step=1)
            with col3:
                resultado = st.selectbox("Resultado", ["Gain", "Loss", "Fora do Alvo"])
                
            obs = st.text_area("Observações sobre o Tape Reading / Rompimento:")
            if st.form_submit_button("Salvar Registo"):
                st.success(f"Registo guardado com sucesso para {ativo}!")

    with tab4:
        st.subheader("Bloco de Notas Estratégicas")
        st.text_area("Anote os pontos de suporte, resistência e regiões institucionais do dia:", height=200)
