import sqlite3


def inserir_escola(nome): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
    cursor.execute(f"INSERT INTO escolas (nome) VALUES {nome}")
    conexao.commit() 

nome = input("Digite o nome da escola: ")
inserir_escola(nome)

#a conexao e o cursor tem que ser criados e encerrados dentro da função