import sqlite3

def cadastrar_turma(nome, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    try:
        cursor.execute("INSERT INTO turmas (nome_turma,id_serie,id_professor) VALUES (?,?,?)"), (nome , id_serie , id_prof)
        conexao.commit()
    except sqlite3.IntegrityError:
        ("Professor ou série não existe.")
    finally:
        conexao.close()

    # Se o id_prof não existir, ocorre um IntegrityError.
    # Se o erro acontecer, o que ocorre com a linha conexao.close()?

#R) pode dar erro por que não existe o id prof entao colocamos os try, except junto com o erro que ai aparece. Se acontecer o erro tanto o commit tanto o close não é executado
    