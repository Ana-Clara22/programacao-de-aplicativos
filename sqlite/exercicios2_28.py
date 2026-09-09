import sqlite3
from banco import conectar


def cadastrar_escola(nome, cidade):
    try:
        assert nome.strip() != "", "O nome da escola não pode ficar em branco."
        assert cidade.strip() != "", "A cidade não pode ficar em branco."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
            (nome.strip(), cidade.strip())
        )

        conexao.commit()
        conexao.close()

        print("Escola cadastrada com sucesso!")

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_escolas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        conexao.close()

        print("\n--- LISTA DE ESCOLAS ---")

        if not escolas:
            print("Nenhuma escola cadastrada.")
            return

        for escola in escolas:
            print(f"ID: {escola[0]} | Nome: {escola[1]} | Cidade: {escola[2]}")

    except sqlite3.Error as erro:
        print(f"Erro ao listar escolas: {erro}")


def alterar_escola(id_escola, nome, cidade):
    try:
        assert id_escola > 0, "O ID da escola deve ser maior que zero."
        assert nome.strip() != "", "O nome da escola não pode ficar em branco."
        assert cidade.strip() != "", "A cidade não pode ficar em branco."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE escolas
            SET nome = ?, cidade = ?
            WHERE id = ?
            """,
            (nome.strip(), cidade.strip(), id_escola)
        )

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            conexao.commit()
            print("Escola alterada com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro ao alterar escola: {erro}")


def excluir_escola(id_escola):
    try:
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM escolas WHERE id = ?",
            (id_escola,)
        )

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            conexao.commit()
            print("Escola excluída com sucesso!")

        conexao.close()

    except AssertionError as erro:
        print(f"Validação: {erro}")

    except sqlite3.IntegrityError:
        print(
            "Não foi possível excluir a escola. "
            "Ela possui turmas vinculadas."
        )

    except sqlite3.Error as erro:
        print(f"Erro ao excluir escola: {erro}")
