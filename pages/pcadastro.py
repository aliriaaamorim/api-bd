import streamlit as st;
import controllers.ClienteController as ccon
import models.cliente as cliente

st.title(":red[Cadastro de Doador]   ""   :syringe:")

with st.form(key="cadastrar_doador", clear_on_submit=True):
    input_nome= st.text_input(label="Nome do doador")
    input_cpf = st.text_input(label = "CPF")
    input_idade = st.text_input(label = "Idade")
    input_data_nascimento = st.date_input(label = "Data de nascimento", value = None, min_value = None, 
                                          format="DD/MM/YYYY")
    input_sexo = st.selectbox(label="Sexo", options=["Feminino", "Masculino"])
    input_peso = st.number_input(label="Peso", format="%f")
    input_tipo_sanguineo = st.selectbox(label="Tipo Sanguineo", options=["A+", "A-", "B+", "B-", "AB+", 
                                                                         "AB-", "O+", "O-"])
    input_button = st.form_submit_button("Enviar")

    if input_button:
        cliente.nome = input_nome
        cliente.cpf = input_cpf
        cliente.idade = input_idade
        cliente.data_nascimento = input_data_nascimento
        cliente.sexo = input_sexo
        cliente.peso = input_peso
        cliente.tipo_sanguineo = input_tipo_sanguineo
        ccon.Incluir(cliente)
