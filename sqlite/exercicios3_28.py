import sqlite3

from banco import conectar


def cadastrar_turma(nome_turma, id_escola):
    try:
        assert nome_turma.strip() != "", "O nome da turma não pode ficar em branco."
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO turmas (nome_turma, id_escola)
            VALUES (?, ?)
            """,
            (nome_turma.strip(), id_escola)
        )

        conexao.commit()
        conexao.close()

        print("Turma cadastrada com sucesso!")

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Não foi possível cadastrar a turma: "
            "a escola informada não existe."
        )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_turmas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        conexao.close()

        print("\n--- LISTA DE TURMAS ---")

        if not turmas:
            print("Nenhuma turma cadastrada.")
            return

        for turma in turmas:
            print(
                f"ID: {turma[0]} | "
                f"Turma: {turma[1]} | "
                f"ID Escola: {turma[2]}"
            )

    except sqlite3.Error as erro:
        print(f"Erro ao listar turmas: {erro}")


def alterar_turma(id_turma, nome_turma, id_escola):
    try:
        assert id_turma > 0, "O ID da turma deve ser maior que zero."
        assert nome_turma.strip() != "", "O nome da turma não pode ficar em branco."
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE turmas
            SET nome_turma = ?, id_escola = ?
            WHERE id = ?
            """,
            (nome_turma.strip(), id_escola, id_turma)
        )

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            conexao.commit()
            print("Turma alterada com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Não foi possível alterar a turma: "
            "a escola informada não existe."
        )

    except sqlite3.Error as erro:
        print(f"Erro ao alterar turma: {erro}")


def excluir_turma(id_turma):
    try:
        assert id_turma > 0, "O ID da turma deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM turmas WHERE id = ?",
            (id_turma,)
        )

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            conexao.commit()
            print("Turma excluída com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Não foi possível excluir a turma. "
            "Ela possui alunos vinculados."
        )

    except sqlite3.Error as erro:
        print(f"Erro ao excluir turma: {erro}")
