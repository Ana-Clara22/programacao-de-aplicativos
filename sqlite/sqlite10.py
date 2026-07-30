import sqlite3

def deletar_escola_antiga():
    id_escola = int(input(" ID da escola remover: "))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.crsor()
    
    cursor.execute(f"DELETE FROM escolas WHERE id =? {id_escola}")

    conexao.commit
    conexao.close

#R) Faltava um ponto de interrogaçao que mostra o que apagar id_escola
#R) E faltava um f e {} para chamar a variavel id_escola