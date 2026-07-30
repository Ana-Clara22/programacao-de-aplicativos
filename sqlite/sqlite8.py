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
    
#R) O erro era por que o cpf não estava unique e ele so pode ser unico 
#R) Entao para não dar erro tem que colocar unique no cpf


