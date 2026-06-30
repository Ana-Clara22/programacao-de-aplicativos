import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema escola.db')
    cursor = conexao.cursor()

    # O python reclama de "Incorrect number of bindings".
    # Estamos passando a variavel, por que ocorre o erro?

    # 

    cursor.esecute("SELECT nome FROM professores WHWRW id = ?", (id_prof))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close()