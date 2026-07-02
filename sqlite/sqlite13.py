import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    dados = cursor.fetchall()

    print("Primeiro print:", dados)
    print("Segundo print:", dados)

    conexao.close()

#R) O fetchall() só consegue pegar os dados uma vez, depois disso o cursor fica vazio.