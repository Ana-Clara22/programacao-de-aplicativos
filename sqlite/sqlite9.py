import sqlite3

def atualizar_nome_aluno(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE alunos SET nome = ? WHERE id = ?", (novo_nome, id_aluno))

    conexao.commit()
    conexao.close()
id_aluno = int(input("Digite o id do aluno: "))
novo_nome = input("Ddigite o novo nome do aluno: ")
atualizar_nome_aluno(id_aluno, novo_nome)

#Faltou usar o WHERE no UPDATE, então o sistema mudou o nome de todos os alunos e não só do aluno com o ID