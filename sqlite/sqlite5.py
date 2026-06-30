import sqlite3

def vincular_aluno_turma():
    nome = input("nome do aluno: ")
    
    # Se o usuário digitar "turma B" em vez do número do ID, o sistema quebra.
    # O try/except abaixo falhou em capturar esse erro. Qual o problema?


    try:
        id_turma = int(input("digite o ID numerico da turma"))

        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?,?)", (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("erro no banco de dados!")
        finally:
            conexao.close()

            