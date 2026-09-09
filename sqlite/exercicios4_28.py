import sqlite3
from banco import conectar


def cadastrar_aluno(nome, idade, id_turma):
    try:
        assert nome.strip() != "", "O nome do aluno não pode ficar em branco."
        assert idade >= 3, "A idade do aluno deve ser igual ou superior a 3 anos."
        assert id_turma > 0, "O ID da turma deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO alunos (nome, idade, id_turma)
            VALUES (?, ?, ?)
            """,
            (nome.strip(), idade, id_turma)
        )

        conexao.commit()
        conexao.close()

        print("Aluno cadastrado com sucesso!")

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Não foi possível cadastrar o aluno: "
            "a turma informada não existe."
        )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_alunos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        conexao.close()

        print("\n--- LISTA DE ALUNOS ---")

        if not alunos:
            print("Nenhum aluno cadastrado.")
            return

        for aluno in alunos:
            print(
                f"ID: {aluno[0]} | "
                f"Nome: {aluno[1]} | "
                f"Idade: {aluno[2]} | "
                f"ID Turma: {aluno[3]}"
            )

    except sqlite3.Error as erro:
        print(f"Erro ao listar alunos: {erro}")


def alterar_aluno(id_aluno, nome, idade, id_turma):
    try:
        assert id_aluno > 0, "O ID do aluno deve ser maior que zero."
        assert nome.strip() != "", "O nome do aluno não pode ficar em branco."
        assert idade >= 3, "A idade do aluno deve ser igual ou superior a 3 anos."
        assert id_turma > 0, "O ID da turma deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE alunos
            SET nome = ?, idade = ?, id_turma = ?
            WHERE id = ?
            """,
            (nome.strip(), idade, id_turma, id_aluno)
        )

        if cursor.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            conexao.commit()
            print("Aluno alterado com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Não foi possível alterar o aluno: "
            "a turma informada não existe."
        )

    except sqlite3.Error as erro:
        print(f"Erro ao alterar aluno: {erro}")


def excluir_aluno(id_aluno):
    try:
        assert id_aluno > 0, "O ID do aluno deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM alunos WHERE id = ?",
            (id_aluno,)
        )

        if cursor.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            conexao.commit()
            print("Aluno excluído com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro ao excluir aluno: {erro}")
