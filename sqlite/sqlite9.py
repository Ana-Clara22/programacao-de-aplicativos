import sqlite3

def atualizar_nome_aluno(id_aluno,novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # o professor pediu para mudar o nome do aluno de ID 3,
    # mas o sistema alterou o nome de TODOS os alunos do banco de dados! correção urgente: 

#R) # estava faltando o where pra executar a funçao que pede. No cursor execute tambem faltava a variavel. E os inputs para o nome novo

    cursor.execute("UPDATE alunos SET nome =? WHERE id_aluno ", (novo_nome,id_aluno))

    conexao.commit()
    conexao.close()

id = int(input("digite o id: "))
novo_id = int(input("digite o novo id: "))
print("novo id atualizado!")






