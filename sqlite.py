import sqlite3

# 1. CONEXÃO: Abre ou cria o arquivo do banco de dados
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

print("Passo 1: Conectado ao banco de dados.")

# 2. CRIAÇÃO DA TABELA: Definindo os campos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )
''')
print("Passo 2: Tabela e campos configurados.")

# 3. INFORMAÇÕES DO ALUNO: Criando as variáveis
nome_aluno = "Ana Clara Silva"
telefone_aluno = "(41) 99999-1234"
turma_aluno = "1º Ano A"
idade_aluno = 15
cpf_aluno = "123.456.789-10"

# 4. INSERÇÃO DIRETA: Colocando as variáveis direto dentro do texto SQL (F-String)
comando_inserir = f'''
    INSERT INTO alunos (nome, telefone, turma, idade, cpf)
    VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', {idade_aluno}, '{cpf_aluno}')
'''

# ➔ TEXT (Leva aspas porque é texto).

# ➔ TEXT (Leva aspas porque tem pontos e traços).

# ➔ INTEGER (NÃO leva aspas porque é número inteiro).

# ➔ REAL/FLOAT (NÃO leva aspas porque é número decimal).

# ➔ BOOL (0 ou 1) (NÃO leva aspas porque vira número inteiro no banco).

# Envia o comando completo para o banco de dados
cursor.execute(comando_inserir)

# 5. SALVAR E FECHAR
conexao.commit()
conexao.close()

print("Passo 3: Dados gravados com sucesso!")