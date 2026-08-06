import sqlite3 
 
def cadastrar_escola_manual(): 

    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor()
    try:
        id_escola = int(input("Digite o ID para a nova escola: ")) 
        nome = input("Nome da escola: ") 


        cursor.execute("INSERT INTO escolas (id, nome) VALUES (?, ?)", (id_escola, nome)) 
        
        conexao.commit() 
    except sqlite3.IntegrityError as e:
        print("Erro no sistema, ", e)
    
    finally:
        conexao.close()

cadastrar_escola_manual()


#quando usamos chaves primaria precisamos usar a integrityError para evitar de ter 2 ID's iguais


