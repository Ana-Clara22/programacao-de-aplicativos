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

    nome_completo = input("Digite o seu nome: ")

    
    comando_inserir = f'''
    INSERT INTO escolas (nome)
    VALUES ('{nome_completo}')
    '''
    cursor.execute(comando_inserir)


    conexao.commit()
    print("cadastro realizado")
    conexao.close() 

inicializar_banco()


# Não tinha conexcao.commit, então os dados nao salva sem isso 

