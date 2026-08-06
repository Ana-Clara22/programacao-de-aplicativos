import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('''
                            CREATE TABLE IF NOT EXISTS serie (
                        id_escola INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_serie TEXT NOT NULL
        )
    ''')

    try:
        cursor.execute(f'''INSERT INTO serie (nome_serie, id_escola)
                        VALUES ('{nome_serie}', '{id_escola}')
                        '''
        )
        
        conexao.commit()
        print("Série cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()

nome_serie = input("Nome da série: ")
id_escola = int(input("ID da escola: "))

cadastrar_serie(nome_serie, id_escola)


#Faltou o pragma, ele deixa ativar a chave estrangeira ai ele reconhece se a estrangeira existe


