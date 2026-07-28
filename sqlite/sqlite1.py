import sqlite3 

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL  
            )
        ''')
    conexao.commit() # o banco de dados nao foi criado
    conexao.close() 

#O banco nã está salvando as alterações. Por quê? 

#R) Estava faltando o commit
  
