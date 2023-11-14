import streamlit as st;
import controllers.ClienteController as ccon
import pandas as pd
import models.recebedor as recebedor
import models.doador as doador
import pages.pcadastroDoador as pageCadastroDoador

st.header("Alterar Doador")

with st.container():
    ###################################
    ############  Doador ##############
    ###################################

    doadorRecuperado = ccon.consultarDoadoresbyCpf(st.text_input(label="CPF do doador"))

    with st.form(key="cadastrar_doador", clear_on_submit=True):
            if doadorRecuperado is None:
                st.warning("Digite um CPF válido")

            else:
                input_nome= st.text_input(label="Nome do doador", value = doadorRecuperado.nome)
                input_cpf = st.text_input(label = "CPF", value = doadorRecuperado.cpf)
                input_idade = st.text_input(label = "Idade", value = doadorRecuperado.idade)
                input_data_nascimento = st.date_input(label = "Data de nascimento",min_value = None, format="DD/MM/YYYY")
                input_sexo = st.selectbox(label="Sexo", options=["Feminino", "Masculino"])
                input_peso = st.number_input(label="Peso", format="%f")
                input_tipo_sanguineo = st.selectbox(label="Tipo Sanguineo", options=["A+", "A-", "B+", "B-", "AB+", 
                                                                                        "AB-", "O+", "O-"])
                input_profissional = st.text_input(label="Profissional responsável", value=doadorRecuperado.exames_biomedico_crbm)
                input_exames = st.selectbox(label = "Resultado da triagem", options=["Reprovado", "Aprovado"])
            input_button = st.form_submit_button("Enviar")
                 

    if input_button:
            doador.nome = input_nome
            doador.cpf = input_cpf
            doador.idade = input_idade
            doador.data_nascimento = input_data_nascimento

            if input_sexo == "Masculino":
                input_sexo = "M"
            else: input_sexo = "F"
            doador.sexo = input_sexo
            doador.peso = input_peso
            doador.tipo_sanguineo = input_tipo_sanguineo
            doador.exames_biomedico_crbm = input_profissional

            if input_exames == "Reprovado":
                input_exames = 0
            else:input_exames = 1
            doador.exames_resultado = input_exames

            if doadorRecuperado is None:
                 print("came from here")
                 ccon.incluirD(doador)
                 st.success("Doador cadastrado com sucesso!")
            else:
                    print("came from here")
                    ccon.alterarD(doador)
                    st.success("Cadastro de doador atualizado com sucesso!")


st.header("Alterar Recebedor")
with st.container():
    ###################################
    ############ Recebedor ############
    ###################################

    recebedorRecuperado = ccon.consultarRecebedorbyCpf(st.text_input(label="CPF do recebedor"))

    with st.form(key="cadastrar_recebedor", clear_on_submit=True):
            if recebedorRecuperado is None:
                st.warning("Digite um CPF válido")
            else:
                input_nome= st.text_input(label="Nome do doador", value = recebedorRecuperado.nome)
                input_cpf = st.text_input(label = "CPF", value = recebedorRecuperado.cpf)
                input_idade = st.text_input(label = "Idade", value = recebedorRecuperado.idade)
                input_data_nascimento = st.date_input(label = "Data de nascimento",min_value = None, format="DD/MM/YYYY")
                input_sexo = st.selectbox(label="Sexo", options=["Feminino", "Masculino"])
                input_peso = st.number_input(label="Peso", format="%f")
                input_tipo_sanguineo = st.selectbox(label="Tipo Sanguineo", options=["A+", "A-", "B+", "B-", "AB+", 
                                                                                        "AB-", "O+", "O-"])
                input_profissional = st.text_input(label="Profissional responsável", value=recebedorRecuperado.enfermagem_coren)
                input_telefone = st.text_input(label = "Telefone", value = recebedorRecuperado.telefone)
                input_matricula = st.text_input(label = "Matrícula", value = recebedorRecuperado.adm_hospital_matricula)
            input_button = st.form_submit_button("Enviar")
                 

    if input_button:
            recebedor.nome = input_nome
            recebedor.cpf = input_cpf
            recebedor.idade = input_idade
            recebedor.data_nascimento = input_data_nascimento

            if input_sexo == "Masculino":
                input_sexo = "M"
            else: input_sexo = "F"
            recebedor.sexo = input_sexo
            recebedor.peso = input_peso
            recebedor.tipo_sanguineo = input_tipo_sanguineo
            recebedor.enfermagem_coren = input_profissional
            recebedor.adm_hospital_matricula = input_matricula
            recebedor.telefone = input_telefone

            if recebedorRecuperado is None:
                 ccon.incluirR(recebedor)
                 st.success("Doador cadastrado com sucesso!")
            else:
                    ccon.alterarR(recebedor)
                    st.success("Cadastro de doador atualizado com sucesso!")


