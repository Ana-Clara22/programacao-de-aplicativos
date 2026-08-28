import sqlite3
from banco import conectar


def cadastrar_escola(nome, cidade):
    try:
        assert nome.strip() != "", "O nome da escola não pode ser vazio."
        assert cidade.strip() != "", "A cidade não pode ser vazia."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )

        conexao.commit()
        conexao.close()

        print("Escola cadastrada com sucesso!")

    except AssertionError as erro:
        print(f"Erro de validação: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def listar_escolas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        conexao.close()

        print("\n--- ESCOLAS ---")

        if not escolas:
            print("Nenhuma escola cadastrada.")
        else:
            for escola in escolas:
                print(f"ID: {escola[0]} | Nome: {escola[1]} | Cidade: {escola[2]}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def alterar_escola(id_escola, nome, cidade):
    try:
        assert nome.strip() != "", "O nome da escola não pode ser vazio."
        assert cidade.strip() != "", "A cidade não pode ser vazia."

        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "UPDATE escolas SET nome = ?, cidade = ? WHERE id = ?",
            (nome, cidade, id_escola)
        )

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            print("Escola alterada com sucesso!")

        conexao.commit()
        conexao.close()

    except AssertionError as erro:
        print(f"Erro de validação: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


def excluir_escola(id_escola):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM escolas WHERE id = ?",
            (id_escola,)
        )

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            print("Escola excluída com sucesso!")

        conexao.commit()
        conexao.close()

    except sqlite3.Error as erro:
        print("Não foi possível excluir a escola.")
        print(f"Erro: {erro}")