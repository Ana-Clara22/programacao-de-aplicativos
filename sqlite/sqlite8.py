import _sqlite3 

def cadastrar_professor (nome, cpf):
    conexao = _sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS professores (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   cpf UNIQUE TEXT
                   )
                   ''')
    
# O erro era por que o cpf não estava com o unique, O UNIQUE garante q os cpfs n se repitam