import sqlite3


def cadastrar_corporacao():
    try:
        conexao = sqlite3.connect("automoveis.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS corporacoes_industrias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                razao_social TEXT NOT NULL,
                codigo_industrial TEXT NOT NULL
            )
        """)

        razao_social = input("Digite a razão social da corporação: ")
        codigo_industrial = input("Digite o código industrial: ")

        cursor.execute("""
            INSERT INTO corporacoes_industrias
            (razao_social, codigo_industrial)
            VALUES (?, ?)
        """, (razao_social, codigo_industrial))

        conexao.commit()

        print("Corporação cadastrada com sucesso.")

    except ValueError:
        print("Digite um valor válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conexao.close()

def listar_corporacoes():
    try:
        conexao = sqlite3.connect("automoveis.db")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM corporacoes_industrias
        """)

        corporacoes = cursor.fetchall()

        print("\n===== LISTA DE CORPORAÇÕES =====")

        if not corporacoes:
            print("Nenhuma corporação cadastrada.")
            return

        for c in corporacoes:
            print(f"ID: {c[0]}")
            print(f"Razão social: {c[1]}")
            print(f"Código industrial: {c[2]}")
            print("-" * 30)

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conexao.close()

def atualizar_corporacao():
    try:
        conexao = sqlite3.connect("automoveis.db")
        cursor = conexao.cursor()

        print("\n===== ATUALIZAR CORPORAÇÃO =====")

        id_corporacao = int(
            input("Digite o ID da corporação: ")
        )

        cursor.execute("""
            SELECT * FROM corporacoes_industrias
            WHERE id = ?
        """, (id_corporacao,))

        c = cursor.fetchone()

        if not c:
            print("Corporação não encontrada.")
            return

        print(f"Razão social atual: {c[1]}")
        print(f"Código industrial atual: {c[2]}")

        razao_atualizada = input(
            "Digite a nova razão social: "
        )

        codigo_atualizado = input(
            "Digite o novo código industrial: "
        )

        cursor.execute("""
            UPDATE corporacoes_industrias
            SET razao_social = ?,
                codigo_industrial = ?
            WHERE id = ?
        """, (
            razao_atualizada,
            codigo_atualizado,
            id_corporacao
        ))

        conexao.commit()

        print("Corporação atualizada com sucesso.")

    except ValueError:
        print("Digite um valor válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conexao.close()


def atualizar_complexo():
    try:
        conexao = sqlite3.connect("automoveis.db")
        cursor = conexao.cursor()

        print("\n===== ATUALIZAR COMPLEXO =====")

        id_complexo = int(
            input("Digite o ID do complexo: ")
        )

        cursor.execute("""
            SELECT * FROM complexos_fabris
            WHERE id = ?
        """, (id_complexo,))

        c = cursor.fetchone()

        if not c:
            print("Complexo não encontrado.")
            return

        print(f"Cidade atual: {c[1]}")
        print(f"ID da corporação atual: {c[2]}")

        cidade_atualizada = input(
            "Digite a nova cidade polo: "
        )

        id_corporacao_atualizado = int(
            input("Digite o novo ID da corporação: ")
        )

        cursor.execute("""
            SELECT id FROM corporacoes_industrias
            WHERE id = ?
        """, (id_corporacao_atualizado,))

        corporacao = cursor.fetchone()

        if not corporacao:
            print("Esse ID de corporação não existe.")
            return

        cursor.execute("""
            UPDATE complexos_fabris
            SET cidade_polo = ?,
                id_corporacao = ?
            WHERE id = ?
        """, (
            cidade_atualizada,
            id_corporacao_atualizado,
            id_complexo
        ))

        conexao.commit()

        print("Complexo atualizado com sucesso.")

    except ValueError:
        print("Digite um valor válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conexao.close()

def excluir_complexo():
    try:
        conexao = sqlite3.connect("automoveis.db")
        cursor = conexao.cursor()

        listar_complexos()

        id_complexo = int(
            input("Digite o ID do complexo que deseja excluir: ")
        )

        cursor.execute("""
            DELETE FROM complexos_fabris
            WHERE id = ?
        """, (id_complexo,))

        if cursor.rowcount == 0:
            print("Complexo não encontrado.")
        else:
            conexao.commit()
            print("Complexo excluído com sucesso.")

    except ValueError:
        print("Digite um valor válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conexao.close()