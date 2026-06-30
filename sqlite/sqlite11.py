import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Adicionado o 'ON' para relacionar as tabelas corretamente
    cursor.execute("""
        SELECT alunos.nome, turmas.nome_turma 
        FROM alunos 
        INNER JOIN turmas ON alunos.turma_id = turmas.id
    """)

    # Corrigido de 'linhas' para 'linha' para bater com o print
    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} / Turma: {linha[1]}")
        
    conexao.close()

# Para testar:
# listar_alunos_e_turmas()
