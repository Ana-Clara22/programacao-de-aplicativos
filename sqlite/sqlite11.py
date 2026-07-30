11-
import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT alunos.nome, turmas.nome_turma FROM alunos INNER JOIN turmas ON alunos.id_turma = turmas.id")

    for linha in cursor.fechall():
        print(f"Aluno: {linha[0]} | Turma:{linha[1]}")
    conexao.close

#R) Faltou o ON para ligar os alunos e turma