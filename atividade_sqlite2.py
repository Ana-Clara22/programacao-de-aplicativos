import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

def criar_tabelas():

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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        turma TEXT,
        professor_id INTEGER,

        FOREIGN KEY(professor_id)
        REFERENCES professores(id)
    )
    """)

    conexao.commit()

def criar_professor():

    nome = input("Nome Completo: ")
    telefone = input("Telefone: ")
    materia = input("Matéria: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salário: "))
    escola = input("Nome da Escola: ")

    cursor.execute(f'''
    INSERT INTO professores
    (nome_completo, telefone, materia, idade, cpf, salario, nome_escola)
    VALUES ('{nome}', '{telefone}', '{materia}', {idade}, '{cpf}', {salario}, '{escola}')
    ''')

    conexao.commit()

    print("Professor cadastrado com sucesso!")

def listar_professores():

    cursor.execute("SELECT * FROM professores")

    professores = cursor.fetchall()

    print("        PROFESSORES          ")

    for professor in professores:

        print(f"""
ID: {professor[0]}
Nome: {professor[1]}
Telefone: {professor[2]}
Matéria: {professor[3]}
Idade: {professor[4]}
CPF: {professor[5]}
Salário: R$ {professor[6]}
Escola: {professor[7]}
        """)

def alterar_professor():
    listar_professores()

    id_professor = int(input("Digite o ID do professor: "))
    nome = input("Novo nome: ")
    telefone = input("Novo telefone: ")
    materia = input("Nova matéria: ")
    idade = int(input("Nova idade: "))
    cpf = input("Novo CPF: ")
    salario = float(input("Novo salário: "))
    escola = input("Nova escola: ")

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
    (nome, telefone, materia, idade,
     cpf, salario, escola, id_professor))
    conexao.commit()
    print("Professor atualizado!")

def excluir_professor():
    listar_professores()
    id_professor = int(input("Digite o ID do professor: "))

    cursor.execute(f'''
    DELETE FROM professores
    WHERE id = ?
    ''', (id_professor,))

    conexao.commit()
    print("Professor excluído!")

def criar_aluno():

    nome = input("Nome do aluno: ")
    idade = int(input("Idade: "))
    turma = input("Turma: ")

    print("Professores disponíveis:")
    listar_professores()

    professor_id = int(
        input("Digite o ID do professor responsável: ")
    )

    cursor.execute(f'''
    INSERT INTO alunos
    (nome, idade, turma, professor_id)
    VALUES ('{nome}', '{idade}', '{turma}', {professor_id}')
    ''')
    conexao.commit()
    print("Aluno cadastrado!")

def listar_alunos():
    cursor.execute(f'''
    SELECT
        alunos.id,
        alunos.nome,
        alunos.idade,
        alunos.turma,
        professores.nome_completo
    FROM alunos
    INNER JOIN professores
    ON alunos.professor_id = professores.id
    ''')

    alunos = cursor.fetchall()
    print("        ALUNOS      ")

    for aluno in alunos:

        print(f'''
ID: {aluno[0]}
Nome: {aluno[1]}
Idade: {aluno[2]}
Turma: {aluno[3]}
Professor: {aluno[4]}
        ''')


def menu():
    criar_tabelas()
    while True:

        print(f'''
1 - Criar Professor
2 - Listar Professores
3 - Alterar Professor
4 - Excluir Professor
5 - Sair
''')
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            alterar_professor()
        elif opcao == "4":
            excluir_professor()
        elif opcao == "5":
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida!")
menu()

conexao.close()
