
import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    #se o usuario digitar "turma B" em vez do numero do ID, o sistema quebra.
    # O try/except abaixo falhou em capturar ese erro. Qual o problema?

#R) A conversão int() gera um ValueError 
#R) Falta um execept para capturar o erro de escrita

    try:
        id_turma = int(input("Digite o ID numerico da turma:"))
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id turma) VALUES (?, ?)", ('nome', 'id_turma'))
        conexao.commit()
    except ValueError:
        print("Erro: Digite apenas numeros!")
    except sqlite3.Error:
        print("Erro no banco de dados!")
    finally:
        conexao.close()
            