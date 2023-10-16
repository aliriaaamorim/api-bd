import streamlit as st;
import controllers.ClienteController as ccon
import pandas as pd
import models.recebedor as recebedor
import models.doador as doador

st.header("Excluir Doador")
with st.container():
    ###################################
    ######## Excluir Doador ###########
    ###################################

    input_cpf = st.text_input(label="Digite o CPF do Doador:")
    button_alterar = st.button("Excluir Doador", use_container_width=True)
    if button_alterar:
        ccon.excluirD(input_cpf)
        st.success("Doador excluído com sucesso!")

st.header("Exclui Recebedor")
with st.container():
    ###################################
    ####### Excluir Recebedor #########
    ###################################

    input_cpf = st.text_input(label="Digite o CPF do Paciente:")
    button_alterar = st.button("Excluir Paciente", use_container_width=True)
    if button_alterar:
        ccon.excluirR(input_cpf)
        st.success("Paciente excluído com sucesso!")


