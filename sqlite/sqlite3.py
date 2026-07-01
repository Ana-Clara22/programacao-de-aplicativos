import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect ('sistema_escola.db')
    cursor = conexao.cursor

    # Este bloco quebra ao rodar pela primeir vez em um banco limpo. Por quê?
#R) estava dando erro porque estava puxando uma referencia de umna tabela que nao existe

    cursor.execute('''
                CREATE TABLE IF NOT EXIST series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT,
                id_escola INTEGER,
                FOREIGN KEY ('id_escola)REFERENCES escola(id)
            )
        ''')

     cursor.execute('''
                CREATE TABLE IF NOT ESIXTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
            )
        ''') 

        conexao.commit()
        conexao.close()
