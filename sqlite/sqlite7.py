import sqlite3

def cadastrar_turma(nome_turma, id_serie, id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT NOT NULL,
            id_serie INTEGER NOT NULL,
            id_professor INTEGER NOT NULL,
            FOREIGN KEY (id_serie) REFERENCES series(id),
            FOREIGN KEY (id_professor) REFERENCES professores(id)
        )
    """)

    try:
        cursor.execute(
    f"INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES ('{nome_turma}', {id_serie}, {id_prof})"
)
        conexao.commit()
        print("Turma cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Professor ou série não existe.")

    finally:
        conexao.close()


nome_turma = input("Nome da turma: ")
id_serie = int(input("ID da série: "))
id_prof = int(input("ID do professor: "))

cadastrar_turma(nome_turma, id_serie, id_prof)


# Tava sem o try, sem except e finally, coloquei o IntegrityError pq é o erro q dá no terminal quando a serie n exixte


    