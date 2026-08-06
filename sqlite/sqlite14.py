import sqlite3 

def cadastrar_serie_seguro(nome, id_escola): 
    conexao = None
    try: 
    	
        conexao = sqlite3.connect('/pasta_protegida/sistema.db') 
        cursor = conexao.cursor() 
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)", (nome, id_escola)) 
        conexao.commit() 
    except sqlite3.Error as e: 
        print("Erro técnico:", e) 
    finally: 
        if conexao:
            conexao.close() 


nome = input("Digite o nome: ")
id_escola = int(input("Digite o id da escola: "))

cadastrar_serie_seguro(nome, id_escola)


# O código tenta salvar a série, avisa se algo der errado e só fecha o banco se ele realmente tiver sido aberto, no caso o if conexao:
