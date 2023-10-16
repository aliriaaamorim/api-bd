import services.database as db;
import models.recebedor as recebedor;
import models.doador as doador;
import models.doacao as doacao;
import psycopg2.errors

#
###################################
###### Inserir Doador ########
#
def incluirD(cliente):
   
   db.cursor.execute("""
       INSERT INTO bdsangue.doador(nome, cpf, idade, sexo, data_nascimento,
                              tipo_sanguineo, peso, exames_resultado, exames_biomedico_crbm) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
       (cliente.nome, cliente.cpf, cliente.idade, cliente.sexo, cliente.data_nascimento, 
       cliente.tipo_sanguineo, cliente.peso, cliente.exames_resultado, cliente.exames_biomedico_crbm))
   db.cnxn.commit()
#
###################################
###### Inserir Recebedor ########
#
def incluirR(cliente):
    try:
        db.cursor.execute("""
            INSERT INTO bdsangue.recebedor(nome, cpf, idade, sexo, data_nascimento,
                                tipo_sanguineo, peso, telefone, enfermagem_coren, adm_hospital_matricula) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
            (cliente.nome, cliente.cpf, cliente.idade, cliente.sexo, cliente.data_nascimento, 
            cliente.tipo_sanguineo, cliente.peso, cliente.telefone, cliente.enfermagem_coren, cliente.adm_hospital_matricula))
        db.cnxn.commit()
    except psycopg2.errors.InFailedSqlTransaction as e:
        print(f"Error: {e}")
        db.cnxn.rollback()
#
###################################
###### Consultar Doador ########
#
def consultarDoadores():
    db.cursor.execute("SELECT * FROM bdsangue.doador")
    listaDoadores = []

    for row in db.cursor.fetchall():
        listaDoadores.append(doador.Doador(row[0], row[1], row[2], row[3], row[4], 
             								row[5], row[6], row[7], row[8] ))
    return listaDoadores
#
###################################
###### Consultar Doador por CPF ########
#
def consultarDoadoresbyCpf(cpf):
    db.cursor.execute("SELECT * FROM bdsangue.doador WHERE cpf = %s", (cpf,))
    listaDoadores = []

    for row in db.cursor.fetchall():
        listaDoadores.append(doador.Doador(row[1], row[0], row[2], row[3], row[4], 
             								row[5], row[6], row[7], row[8] ))
        
    if listaDoadores == []:
        return None
    else:
        return listaDoadores[0]
#
###################################
###### Consultar Recebedor ########
#

def consultarPacientes():
    try:
        db.cursor.execute("SELECT * FROM bdsangue.recebedor")
        listaPacientes = []

        for row in db.cursor.fetchall():
            listaPacientes.append(recebedor.Recebedor(row[0], row[1], row[5],  row[3], row[4],
                                                    row[2], row[7],  row[6], row[8], row[9]))
        return listaPacientes
    except psycopg2.errors.InFailedSqlTransaction as e:
        print(f"Error: {e}")
        db.cnxn.rollback()
#
###################################
###### Consultar recebedor por CPF ########
#
def consultarRecebedorbyCpf(cpf):
    db.cursor.execute("SELECT * FROM bdsangue.recebedor WHERE cpf = %s", (cpf,))
    listaRecebedores = []

    for row in db.cursor.fetchall():
        listaRecebedores.append(recebedor.Recebedor(row[1], row[0], row[2], row[3], row[4], 
             								row[5], row[6], row[7], row[8], row[9] ))
    if (len(listaRecebedores) == 0):
        return None
    else:
        return listaRecebedores[0]

###################################
######## Excluir Doador ###########
#
def excluirD(cpf):
    try:
        db.cursor.execute("""
            DELETE FROM bdsangue.doador WHERE doador.cpf = %s""", [cpf])
        db.cnxn.commit()
    except psycopg2.errors.InFailedSqlTransaction as e:
        print(f"Error: {e}")
        db.cnxn.rollback()

###################################
######## Excluir Recebedor ###########
#
def excluirR(cpf):
    try:
        db.cursor.execute("""
            DELETE FROM bdsangue.recebedor WHERE recebedor.cpf = %s""", [cpf])
        db.cnxn.commit()
    except psycopg2.errors.InFailedSqlTransaction as e:
        print(f"Error: {e}")
        db.cnxn.rollback()

###################################
####### Cadastrar Doacao ##########
#
def incluirDoacao(doacao):
    try:
        db.cursor.execute("""
            INSERT INTO bdsangue.recebedor(tipo_sanguineo, doacao_direcionada, enfermagem_coren, adm_hospital_matricula,
                          adm_bancodesangue_matricula, volume) VALUES(%s, %s, %s, %s, %s, %s)""", 
            (doacao.tipo_sanguineo, doacao.doacao_direcionada, doacao.enfermagem_coren, 
             doacao.adm_hospital_matricula, doacao.adm_bancodesangue_matricula, doacao.volume))
        db.cnxn.commit()
    except psycopg2.errors.InFailedSqlTransaction as e:
        print(f"Error: {e}")
        db.cnxn.rollback()
#
###################################

###################################
####### Consultar Doacao ##########
#
def incuirDoacao(doacao):
    try:
        db.cursor.execute("""
            INSERT INTO bdsangue.recebedor(tipo_sanguineo, doacao_direcionada, enfermagem_coren, adm_hospital_matricula,
                          adm_bancodesangue_matricula, volume) VALUES(%s, %s, %s, %s, %s, %s)""", 
            (doacao.tipo_sanguineo, doacao.doacao_direcionada, doacao.enfermagem_coren, 
             doacao.adm_hospital_matricula, doacao.adm_bancodesangue_matricula, doacao.volume))
        db.cnxn.commit()
    except psycopg2.errors.InFailedSqlTransaction as e:
        print(f"Error: {e}")
        db.cnxn.rollback()
#
###################################
####### Alterar Doador ##########
#
def alterarD(cliente):
   try:
        db.cursor.execute("""
            UPDATE bdsangue.doador SET nome=%s, cpf=%s, idade=%s, sexo=%s, data_nascimento = %s,
                                    tipo_sanguineo = %s, peso = %s, exames_resultado = %s, exames_biomedico_crbm = %s WHERE cpf = %s""", 
            (cliente.nome, cliente.cpf, cliente.idade, cliente.sexo, cliente.data_nascimento, 
            cliente.tipo_sanguineo, cliente.peso, cliente.exames_resultado, cliente.exames_biomedico_crbm, cliente.cpf))
        db.cnxn.commit()
   except psycopg2.errors.InFailedSqlTransaction as e:
        print(f"Error: {e}")
        db.cnxn.rollback()

#
###################################
####### Alterar Doador ##########
#
def alterarR(cliente):
   try:
        db.cursor.execute("""
            UPDATE bdsangue.recebedor SET nome=%s, cpf=%s, idade=%s, sexo=%s, data_nascimento = %s,
                                    tipo_sanguineo = %s, peso = %s, telefone = %s, adm_hospital_matricula = %s WHERE cpf = %s""", 
            (cliente.nome, cliente.cpf, cliente.idade, cliente.sexo, cliente.data_nascimento, 
            cliente.tipo_sanguineo, cliente.peso, cliente.telefone, cliente.adm_hospital_matricula, cliente.cpf))
        db.cnxn.commit()
   except psycopg2.errors.InFailedSqlTransaction as e:
        print(f"Error: {e}")
        db.cnxn.rollback()

