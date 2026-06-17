import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

def criar_tabela():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS professores (
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
    conexao.commit()
    
def criar_professor():
    nome = input("nome Completo: ")
    telefone = input("telefone: ")
    materia = input("matéria: ")
    idade = int(input("idade: "))
    cpf = input("CPF: ")
    salario = float(input("salário: "))
    escola = input("nome da Escola: ")

    cursor.execute(f"""
    INSERT INTO professores
    (nome_completo, telefone, materia, idade, cpf, salario, nome_escola)
    VALUES ('{nome}', '{telefone}', '{materia}', {idade}, '{cpf}', {salario}, '{escola}')
    """)
    conexao.commit()
    print("professor cadastrado com sucesso!")
    conexao.commit()
    print("professor cadastrado com sucesso!")



def listar_professores():
    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()
    if not professores:
        print("nenhum professor cadastrado.")
        return
    for professor in professores:
        print("-" * 50)
        print(f"ID: {professor[0]}")
        print(f"nome: {professor[1]}")
        print(f"telefone: {professor[2]}")
        print(f"matéria: {professor[3]}")
        print(f"idade: {professor[4]}")
        print(f"CPF: {professor[5]}")
        print(f"salário: R$ {professor[6]:.2f}")
        print(f"escola: {professor[7]}")



def alterar_professor():
    listar_professores()
    id_professor = int(input("\n digite o ID do professor que deseja alterar: "))
    nome = input("novo nome completo: ")
    telefone = input("novo telefone: ")
    materia = input("nova matéria: ")
    idade = int(input("nova idade: "))
    cpf = input("novo CPF: ")
    salario = float(input("novo salário: "))
    escola = input("novo nome da escola: ")

    cursor.execute(f"""
    UPDATE professores
    SET nome_completo = '{nome}',
        telefone = '{telefone}',
        materia = '{materia}',
        idade = {idade},
        cpf = '{cpf}',
        salario = {salario},
        nome_escola = '{escola}'
    WHERE id = {id_professor}
"""),(nome, telefone, materia, idade, cpf, salario, escola, id_professor)
    


    
def excluir_professor():
    listar_professores()
    id_professor = int(input("\nDigite o ID do professor que deseja excluir: "))
    cursor.execute("DELETE FROM professores WHERE id = ?", (id_professor,))
    conexao.commit()
    if cursor.rowcount > 0:
        print("professor excluído com sucesso!")
    else:
        print("professor não encontrado.")
def menu():
    criar_tabela()
    while True:
        print("         MENU PROFESSORES     ")
        print("1 - fazer cadastro do professor")
        print("2 - listar professores cadastrados")
        print("3 - alterar cadastro de professor")
        print("4 - excluir cadastro do professor")
        print("5 - sair")
        opcao = input("escolha uma opção: ")
        if opcao == "1":
            criar_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            alterar_professor()
        elif opcao == "4":
            excluir_professor()
        elif opcao == "5":
            print("programa encerrado.")
            break
        else:
            print("opção inválida!")
menu()
conexao.close()