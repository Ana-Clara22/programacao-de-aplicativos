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
