import sqlite3

def deletar_escola_antiga():
    id_escola = int(input("ID da escola a remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute(f"DELETE FROM escolas WHERE id = {id_escola}")

    conexao.commit()
    conexao.close()
deletar_escola_antiga()

#A variável id_escola foi usada de forma errada no comando DELETE.