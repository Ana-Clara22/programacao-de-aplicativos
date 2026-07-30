import sqlite3
def vincular_aluno_turma():
    nome = input(" Nome do aluno: ")
    try: 
        id_turma = int(input(" Digite o ID numérico da turma: "))

        conexao = sqlite3.connect (' sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except sqlite3.Error:
        print("Erro no banco de dados ")
    
    except ValueError:
        print("Erro de valor no cadastro tente novavamente")
        
    finally:
        conexao.close

#R) O primeiro erro é por que o id_turma é um int então escrevendo algo sem ser numero vai dar erro
#R) O segundo erro é a falta de except um que encontre o erro de escrita