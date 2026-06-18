import sqlite3

# ==========================
# Conexão com banco
# ==========================

conn = sqlite3.connect("escola_demonstracao.db")
cursor = conn.cursor()

# ==========================
# Criar tabela
# ==========================

def criar_tabela_professores():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT NOT NULL,
        telefone TEXT,
        materia TEXT,
        idade INTEGER,
        cpf TEXT,
        salario REAL,
        nome_escola TEXT
    )
    """)
    
    conn.commit()

# ==========================
# CREATE
# ==========================

def cadastrar_professor():
    nome = input("Nome Completo: ")
    telefone = input("Telefone: ")
    materia = input("Matéria: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salário: "))
    escola = input("Nome da Escola: ")

    cursor.execute("""
    INSERT INTO professores
    (nome_completo, telefone, materia, idade, cpf, salario, nome_escola)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (nome, telefone, materia, idade, cpf, salario, escola))

    conn.commit()

    print("Professor cadastrado com sucesso!")

# ==========================
# READ
# ==========================

def listar_professores():
    cursor.execute("SELECT * FROM professores")

    professores = cursor.fetchall()

    print("\n--- LISTA DE PROFESSORES ---")

    for professor in professores:
        print(professor)

# ==========================
# UPDATE
# ==========================

def alterar_professor():
    id_professor = int(input("Digite o ID do professor: "))

    novo_nome = input("Novo nome: ")
    novo_telefone = input("Novo telefone: ")
    nova_materia = input("Nova matéria: ")
    nova_idade = int(input("Nova idade: "))
    novo_cpf = input("Novo CPF: ")
    novo_salario = float(input("Novo salário: "))
    nova_escola = input("Nova escola: ")

    cursor.execute("""
    UPDATE professores
    SET nome_completo=?,
        telefone=?,
        materia=?,
        idade=?,
        cpf=?,
        salario=?,
        nome_escola=?
    WHERE id=?
    """,
    (
        novo_nome,
        novo_telefone,
        nova_materia,
        nova_idade,
        novo_cpf,
        novo_salario,
        nova_escola,
        id_professor
    ))

    conn.commit()

    print("Professor atualizado!")

# ==========================
# DELETE
# ==========================

def excluir_professor():
    id_professor = int(input("Digite o ID do professor: "))

    cursor.execute(
        "DELETE FROM professores WHERE id=?",
        (id_professor,)
    )

    conn.commit()

    print("Professor excluído!")

# ==========================
# MENU
# ==========================

def menu():

    criar_tabela_professores()

    opcao = 0

    while opcao != 5:

        print("\n===== MENU =====")
        print("1 - Cadastrar Professor")
        print("2 - Listar Professores")
        print("3 - Alterar Professor")
        print("4 - Excluir Professor")
        print("5 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            cadastrar_professor()

        elif opcao == 2:
            listar_professores()

        elif opcao == 3:
            alterar_professor()

        elif opcao == 4:
            excluir_professor()

        elif opcao == 5:
            print("Programa encerrado!")

        else:
            print("Opção inválida!")

menu()

conn.close()