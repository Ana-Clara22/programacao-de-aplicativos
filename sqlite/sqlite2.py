import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conxao = sqlite3.connect('sistema_esola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # O aluno tenta cadastraruma série com id_escola = 999 (qual não existe).
    # O sqlite aceita o cadastrar mesmo assim. O que está faltando ativar.

#R) motivo de o id_escola = 999 estar sendo aceito é que falta ativar as chaves estrangeiras com PRAGMA foreign_keys = ON.

    try:
        cursor.exeute("INSERT INTO series (nome_serie, id_escola)VALUES (?, ?))", (nome_serie, id_escola))

        conexao.commit()
    except sqlite3.IntergrityError
        print("escola inexistente!")
    finally:
        conexao.close()


