import sqlite3

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
    REFERENCES corporacoes_industrias(id)
)
""")

def registrar():
    tipo = input("1-corporacao 2-complexo: ")

    if tipo == "1":
        razao = input("razao social: ")
        codigo = input("codigo industrial: ")

        cursor.execute(
            "INSERT INTO corporacoes_industrias (razao_social, codigo_industrial) VALUES (?, ?)",
            (razao, codigo)
        )

    elif tipo == "2":
        cidade = input("cidade polo: ")
        id_corporacao = int(input("id da corporacao: "))

        cursor.execute(
            "INSERT INTO complexos_fabris (cidade_polo, id_corporacao) VALUES (?, ?)",
            (cidade, id)
        )

    conexao.commit()
    print("cadastro realizado!")


def alterar():
    tipo = input("1-corporacao 2-complexo: ")
    id = int(input("id: "))

    if tipo == "1":
        razao = input("nova razao social: ")
        codigo = input("novo codigo industrial: ")

        cursor.execute(
            "UPDATE corporacoes_industrias SET razao_social=?, codigo_industrial=? WHERE id=?",
            (razao, codigo, id)
        )

    elif tipo == "2":
        cidade = input("nova cidade polo: ")

        cursor.execute(
            "UPDATE complexos_fabris SET cidade_polo=? WHERE id=?",
            (cidade, id)
        )

    conexao.commit()
    print("cadastro atualizado!")

def deletar():
    tipo = input("1-corporacao 2-complexo: ")
    id = int(input("id: "))

    if tipo == "1":
        cursor.execute(
            "DELETE FROM corporacoes_industrias WHERE id=?",
            (id,)
        )

    elif tipo == "2":
        cursor.execute(
            "DELETE FROM complexos_fabris WHERE id=?",
            (id,)
        )

    conexao.commit()
    print("cadastro deletado!")

while True:
    print("\n1-registrar")
    print("2-alterar")
    print("3-deletar")
    print("4-sair")

    opcao = input("opcao: ")

    if opcao == "1":
        registrar()
    elif opcao == "2":
        alterar()
    elif opcao == "3":
        deletar()
    elif opcao == "4":
        break
    else:
        print("opcao invalida!")

conexao.close()
