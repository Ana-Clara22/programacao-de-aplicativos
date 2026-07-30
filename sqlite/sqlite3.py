import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS escolas (
                   id INTERGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT
                   )''')
    
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS series (
                   id INTERGER PRIMARY KEY AUTOINCREMENT,
                   nome_serie TEXT, 
                   id_escola INTERGER, 
                   FOREIGN KEY (id_escola) REFERENCES escolas(id)
                   )
                   ''')
    

    conexao.commit()
    conexao.close()

#R) Estava dando erro pois o REFERENCES estava buscando uma referencia em uma tabela que não existe