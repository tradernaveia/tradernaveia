with col3:
                resultado = st.selectbox("Resultado do Estudo", ["Gain", "Loss", "Empate / Fora do Alvo"])
                
            observacao = st.text_area("Observações sobre o Tape Reading / Rompimento:")
            salvar_registro = st.form_submit_button("Salvar Registro de Estudo")
            
            if salvar_registro:
                st.success(f"Registro salvo com sucesso! Alvo de {pontos} pontos catalogado para {ativo_escolhido}.")

    with tab3:
        st.subheader("Bloco de Notas Estratégicas")
        st.text_area("Anote aqui os pontos de suporte, resistência e regiões de briga institucional do dia:", height=200)

if not st.session_state["autenticado"]:
    tela_login()
else:
    plataforma_estudos()
