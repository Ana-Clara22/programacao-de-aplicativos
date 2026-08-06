import sqlite3

def buscar_professor(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT nome FROM professores WHERE id = ?", (id_prof,))
    resultado = cursor.fetchone()

    if resultado:
        print("Professor:", resultado[0])
    else:
        print("Professor não encontrado.")

    conexao.close()

id_prof = int(input("Digite o ID do professor: "))
buscar_professor(id_prof)

# Tinha que colocar uma virgula depois do ((id_prof)), por causa do erro de sintaxe
