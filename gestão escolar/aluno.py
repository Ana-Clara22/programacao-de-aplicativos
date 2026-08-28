import sqlite3
from banco import conectar


def cadastrar_aluno(nome, idade, id_turma):
    try:
        assert nome.strip() != "", "O nome do aluno não pode ser vazio."
        assert idade >= 3, "A idade do aluno deve ser igual ou superior a 3 anos."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO alunos (nome, idade, id_turma)
            VALUES (?, ?, ?)
            """,
            (nome, idade, id_turma)
        )

        conexao.commit()
        conexao.close()

        print("Aluno cadastrado com sucesso!")

    except AssertionError as erro:
        print(f"Erro de validação: {erro}")

    except sqlite3.Error as erro:
        print("Não foi possível cadastrar o aluno.")
        print(f"Erro: {erro}")


def listar_alunos():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        conexao.close()

        print("\n--- ALUNOS ---")

        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(
                    f"ID: {aluno[0]} | "
                    f"Nome: {aluno[1]} | "
                    f"Idade: {aluno[2]} | "
                    f"ID Turma: {aluno[3]}"
                )

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def alterar_aluno(id_aluno, nome, idade, id_turma):
    try:
        assert nome.strip() != "", "O nome do aluno não pode ser vazio."
        assert idade >= 3, "A idade do aluno deve ser igual ou superior a 3 anos."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE alunos
            SET nome = ?, idade = ?, id_turma = ?
            WHERE id = ?
            """,
            (nome, idade, id_turma, id_aluno)
        )

        if cursor.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            print("Aluno alterado com sucesso!")

        conexao.commit()
        conexao.close()

    except AssertionError as erro:
        print(f"Erro de validação: {erro}")

    except sqlite3.Error as erro:
        print("Não foi possível alterar o aluno.")
        print(f"Erro: {erro}")


def excluir_aluno(id_aluno):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM alunos WHERE id = ?",
            (id_aluno,)
        )

        if cursor.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            print("Aluno excluído com sucesso!")

        conexao.commit()
        conexao.close()

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
