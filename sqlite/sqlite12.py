import sqlite3

# o aluno criou a conexão fora das funções para "facilitar"
# pq isso quebra o sistema quando usamos múltiplos arquivos (módulos)?
conexao = sqlite3.connect('sistema_escola.db')
cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,))
conexao.commit()