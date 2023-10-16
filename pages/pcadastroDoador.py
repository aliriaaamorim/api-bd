import streamlit as st;
import controllers.ClienteController as ccon
import models.doador as doador

def CadastrarDoador():
    idAlterar = st.experimental_get_query_params()
    st.experimental_set_query_params()
    doadorRecuperado = None
    if idAlterar.get("input_cpfD") is not None:
        idAlterar = idAlterar.get("input_cpfD")[0]
        doadorRecuperado = ccon.consultarDoadoresbyCpf(idAlterar)
        st.title(":red[Alterar cadastro de doador]   ""   :syringe:")

    else:
        st.title(":red[Cadastro de Doador]   ""   :syringe:")


    with st.form(key="cadastrar_doador", clear_on_submit=True):
            if doadorRecuperado is None:
                input_nome= st.text_input(label="Nome do doador")
                input_cpf = st.text_input(label = "CPF")
                input_idade = st.text_input(label = "Idade")
                input_data_nascimento = st.date_input(label = "Data de nascimento", value = None, min_value = None, 
                                                    format="DD/MM/YYYY")
                input_sexo = st.selectbox(label="Sexo", options=["Feminino", "Masculino"])
                input_peso = st.number_input(label="Peso", format="%f")
                input_tipo_sanguineo = st.selectbox(label="Tipo Sanguineo", options=["A+", "A-", "B+", "B-", "AB+", 
                                                                                    "AB-", "O+", "O-"])
                input_profissional = st.text_input(label="Profissional responsável")
                input_exames = st.selectbox(label = "Resultado da triagem", options=["Reprovado", "Aprovado"])
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
            print("inside the button")
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

paramId = st.experimental_get_query_params()
if paramId == {}:
    CadastrarDoador()


    
