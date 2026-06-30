import sqlite3

def inicializar_banco():
    conexao=sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursos.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
                )
            ''')
#O banco nã está salvando as alterações. Por quê? 

#R) Estava faltando o commit
    
    conexao.commit()
    conexao.close()
