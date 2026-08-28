import sqlite3
from banco import conectar


def cadastrar_turma(nome_turma, id_escola):
    try:
        assert nome_turma.strip() != "", "O nome da turma não pode ser vazio."
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)",
            (nome_turma, id_escola)
        )

        conexao.commit()
        conexao.close()

        print("Turma cadastrada com sucesso!")

    except AssertionError as erro:
        print(f"Erro de validação: {erro}")

    except sqlite3.Error as erro:
        print("Não foi possível cadastrar a turma.")
        print(f"Erro: {erro}")


def listar_turmas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        conexao.close()

        print("\n--- TURMAS ---")

        if not turmas:
            print("Nenhuma turma cadastrada.")
        else:
            for turma in turmas:
                print(
                    f"ID: {turma[0]} | "
                    f"Nome: {turma[1]} | "
                    f"ID Escola: {turma[2]}"
                )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def alterar_turma(id_turma, nome_turma, id_escola):
    try:
        assert nome_turma.strip() != "", "O nome da turma não pode ser vazio."
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE turmas
            SET nome_turma = ?, id_escola = ?
            WHERE id = ?
            """,
            (nome_turma, id_escola, id_turma)
        )

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            print("Turma alterada com sucesso!")
        conexao.commit()
        conexao.close()

    except AssertionError as erro:
        print(f"Erro de validação: {erro}")

    except sqlite3.Error as erro:
        print("Não foi possível alterar a turma.")
        print(f"Erro: {erro}")

def excluir_turma(id_turma):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM turmas WHERE id = ?",
            (id_turma,)
        )

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            print("Turma excluída com sucesso!")

        conexao.commit()
        conexao.close()

    except sqlite3.Error as erro:
        print("Não foi possível excluir a turma.")
        print(f"Erro: {erro}")
