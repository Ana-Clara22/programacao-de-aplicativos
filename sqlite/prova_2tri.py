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


def cadastrar_complexo():
    try:
        conexao = sqlite3.connect("automoveis.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS complexos_fabris (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cidade_polo TEXT NOT NULL,
                id_corporacao INTEGER NOT NULL,
                FOREIGN KEY (id_corporacao)
                REFERENCES corporacoes_industrias (id)
            )
        """)

        cidade_polo = input("Digite a cidade polo: ")
        id_corporacao = int(
            input("Digite o ID da corporação: ")
        )

        cursor.execute("""
            SELECT id FROM corporacoes_industrias
            WHERE id = ?
        """, (id_corporacao,))

        corporacao = cursor.fetchone()

        if not corporacao:
            print("Esse ID de corporação não existe.")
            return

        cursor.execute("""
            INSERT INTO complexos_fabris
            (cidade_polo, id_corporacao)
            VALUES (?, ?)
        """, (cidade_polo, id_corporacao))

        conexao.commit()

        print("Complexo fabril cadastrado com sucesso.")

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


def listar_complexos():
    try:
        conexao = sqlite3.connect("automoveis.db")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT
                complexos_fabris.id,
                complexos_fabris.cidade_polo,
                complexos_fabris.id_corporacao,
                corporacoes_industrias.razao_social
            FROM complexos_fabris
            INNER JOIN corporacoes_industrias
            ON complexos_fabris.id_corporacao =
               corporacoes_industrias.id
        """)

        complexos = cursor.fetchall()

        print("\n===== LISTA DE COMPLEXOS FABRIS =====")

        if not complexos:
            print("Nenhum complexo cadastrado.")
            return

        for c in complexos:
            print(f"ID: {c[0]}")
            print(f"Cidade polo: {c[1]}")
            print(f"ID da corporação: {c[2]}")
            print(f"Corporação: {c[3]}")
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


def excluir_corporacao():
    try:
        conexao = sqlite3.connect("automoveis.db")
        cursor = conexao.cursor()

        listar_corporacoes()

        id_corporacao = int(
            input("Digite o ID da corporação que deseja excluir: ")
        )

        cursor.execute("""
            SELECT id FROM complexos_fabris
            WHERE id_corporacao = ?
        """, (id_corporacao,))

        complexo = cursor.fetchone()

        if complexo:
            print("Não é possível excluir essa corporação.")
            print("Existe um complexo vinculado a ela.")
            return

        cursor.execute("""
            DELETE FROM corporacoes_industrias
            WHERE id = ?
        """, (id_corporacao,))

        if cursor.rowcount == 0:
            print("Corporação não encontrada.")
        else:
            conexao.commit()
            print("Corporação excluída com sucesso.")

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


def criar_tabelas():
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

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS complexos_fabris (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cidade_polo TEXT NOT NULL,
                id_corporacao INTEGER NOT NULL,
                FOREIGN KEY (id_corporacao)
                REFERENCES corporacoes_industrias (id)
            )
        """)

        conexao.commit()

    except Exception as e:
        print(f"Ocorreu um erro ao criar as tabelas: {e}")
    finally:
        conexao.close()


def menu():
    criar_tabelas()

    try:
        opcao = 0

        while opcao != 9:

            print("\n")
            print("-------------------- MENU ------------------")
            print("1 - Cadastrar corporação")
            print("2 - Cadastrar complexo")
            print("3 - Listar corporações")
            print("4 - Listar complexos")
            print("5 - Atualizar corporação")
            print("6 - Atualizar complexo")
            print("7 - Excluir corporação")
            print("8 - Excluir complexo")
            print("9 - Fechar programa")

            opcao = int(
                input("Digite o que você deseja fazer: ")
            )

            if opcao == 1:
                cadastrar_corporacao()

            elif opcao == 2:
                cadastrar_complexo()

            elif opcao == 3:
                listar_corporacoes()

            elif opcao == 4:
                listar_complexos()

            elif opcao == 5:
                atualizar_corporacao()

            elif opcao == 6:
                atualizar_complexo()

            elif opcao == 7:
                excluir_corporacao()

            elif opcao == 8:
                excluir_complexo()

            elif opcao == 9:
                print("===== PROGRAMA ENCERRADO =====")

            else:
                print("Opção inválida.")

    except ValueError:
        print("Digite um valor válido.")


menu()
