import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
    id_eescola = int(input("Digite o seu id: "))
    nome = input("Digite seu nome: ")
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT,
                id_escola INTEGER,
                FOREIGN KEY (id_escola)REFERENCES escolas (id)
            )
        ''')
    id_serie = int(input("Digite o id da serie: "))
    nome_serie = input("Digite nome da serie: ")
    id_escola = int(input("Digite o id da serie: "))
    conexao.commit()
    conexao.close()

criar_tabelas()

# As tabelas foram feitas em ordem errada, pq a estrangeira tem q vim primeiro