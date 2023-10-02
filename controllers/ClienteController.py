import services.database as db;

def Inserir(cliente):
    count = db.cursor.execute("""
        INSERT INTO bdsangue.doador(nome, cpf, idade, sexo, data_nascimento, tipo_sanguineo, peso) VALUES(?,?,?,?,?,?,?)""", 
        cliente.nome, cliente.cpf, cliente.idade, cliente.sexo, cliente.data_nascimento, cliente.tipo_sanguineo, cliente.peso).rowcount
    db.cnxn.commit()