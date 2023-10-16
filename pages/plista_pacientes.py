import streamlit as st;
import controllers.ClienteController as ccon
import pandas as pd
import models.recebedor as recebedor
import models.doador as doador

listaDoadores = []
listaRecebedores = []


st.header("Consulta de Doadores")
for item in ccon.consultarDoadores():
    listaDoadores.append([item.nome, item.cpf, item.data_nascimento, item.tipo_sanguineo, item.idade])

frameD = pd.DataFrame(listaDoadores,columns=['CPF','Nome', 'Idade', 'Tipo Sanguineo', 'Sexo'])
st.table(frameD)

with st.container():

    st.header("Consulta de Recebedores")
    for item in ccon.consultarPacientes():
        listaRecebedores.append([item.nome, item.cpf, item.idade, item.tipo_sanguineo, item.sexo])

    frameR = pd.DataFrame(listaRecebedores, columns=['CPF','Nome', 'Idade', 'Tipo Sanguineo', 'Sexo'])

    st.table(frameR)



def AlterarPaciente():
    cpf = st.text_input("Digite o CPF do Paciente:")
    nome = st.text_input("Digite o nome do Paciente:")
    data_nascimento = st.text_input("Digite a data de nascimento do Paciente:")
    tipo_sanguineo = st.text_input("Digite o tipo sanguineo do Paciente:")
    sexo = st.text_input("Digite o sexo do Paciente:")
    peso = st.text_input("Digite o peso do Paciente:")
    if st.button("Alterar Paciente"):
        ccon.alterarPaciente(cpf, nome, data_nascimento, tipo_sanguineo, sexo, peso)
        st.success("Paciente alterado com sucesso!")