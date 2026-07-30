
import sqlite3 
 
def criar_tabela_turma(): 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 

        cursor.execute('''
                       CREATE TABLE IF NOT EXISTS escolas (
                       id INTERGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT
                       )
                       ''')
     
        cursor.execute(''' 
    	        CREATE TABLE IF NOT EXISTS series ( 
        	    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome_serie TEXT, 
                id_escola INTERGER,  
        	    FOREIGN KEY (id_escola) REFERENCES escolas(id) 
                ) 
                    ''') 
        

        conexao.commit() 
        conexao.close() 

#R) O REFERENCES puxa uma referencia de uma tabela de uma tabela esta limpa entao não tem o id