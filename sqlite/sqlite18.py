import sqlite3 
 
def cadastrar_lista_alunos(): 
    lista = [("Ana", 1), ("Carlos", 1), ("Beatriz", 2)] 
     
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     

    cursor.executemany("INSERT INTO alunos (nome, turma) VALUES (?, ?)", lista)
     
    conexao.commit() 
    conexao.close() 
cadastrar_lista_alunos()


#inves do executemany adicionar 1 ele repete ele mesmo varias vezes 