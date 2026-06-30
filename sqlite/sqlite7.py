import sqlite3

def cadastrar_turma(norma, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Se o id_prof não existir, ocorre um IntegrityError.
    # Se o erro acontecer, o que ocorre com a linha conexao.close()?

    cursor.execute("INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES (?,?,?)", (nome, id_serie, id_prof))
    conexao.commit()
    conexao.close()
    