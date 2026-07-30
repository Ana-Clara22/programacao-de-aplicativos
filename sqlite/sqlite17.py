import sqlite3 
 
def inserir_professor(nome, materia, cpf): 
    try: 
        conexao = sqlite3.connect('sistema_escola.db') 
        cursor = conexao.cursor() 
        cursor.execute("INSERT INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf)) 
        conexao.commit() 
    except sqlite3.Error: 
        print("Erro: Este CPF já está cadastrado no sistema!") 
    finally: 
        conexao.close() 

#R) No trexo cursor.execute("INSERTO INTO professores " O insert está escrito errado 
#R) O except não captura o erro de sintaxe por que ele é especifico do codigo inteiro, teria que criar um novo except apenas para erro de sintaxe


