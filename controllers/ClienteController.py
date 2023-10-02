import services.database as db;
import models.recebedor as recebedor;

def Inserir(cliente):
    count = db.cursor.execute("""
        INSERT INTO bdsangue.doador(nome, cpf, idade, sexo, data_nascimento, tipo_sanguineo, peso) VALUES(?,?,?,?,?,?,?)""", 
        cliente.nome, cliente.cpf, cliente.idade, cliente.sexo, cliente.data_nascimento, cliente.tipo_sanguineo, cliente.peso).rowcount
    db.cnxn.commit()

def ConsultarPacientes():
    db.cursor("SELECT * FROM recebedor")
    listaPacientes = []

    for row in db.cursor.fetchall():
        listaPacientes.append(recebedor.Cliente(row[0], row[1], row[2], row[3], row[4], row[5], row[6])) 