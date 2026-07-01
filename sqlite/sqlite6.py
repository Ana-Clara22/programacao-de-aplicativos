import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema escola.db')
    cursor = conexao.cursor()

    # O python reclama de "Incorrect number of bindings".
    # Estamos passando a variavel, por que ocorre o erro?

#R) É obrigatorio colocar a virgula dps do elemento

    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()
    print(resultado)
    conexao.close
 