import sqlite3

try:
    conexao = sqlite3.connect("hospital.db")
    conexao.execute("PRAGMA foreign_keys = ON;")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS hospitais (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL
        );
    """)
   
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            crm TEXT NOT NULL,
            id_hospital INTEGER NOT NULL,
            FOREIGN KEY(id_hospital) REFERENCES hospitais(id)
        );
    """)

    conexao.commit()

except sqlite3.Error as erro:
    print("Erro ao criar o banco:", erro)

def cadastrar_hospital():
    try:
        nome = input("Nome do hospital: ")
        cidade = input("Cidade: ")

        cursor.execute(
            "INSERT INTO hospitais (nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )
        conexao.commit()
        print("Hospital cadastrado com sucesso!")

    except Exception as erro:
        print("Erro ao cadastrar hospital:", erro)

def cadastrar_medicos()
    try:
        nome = input("Nome do medico: ")
        crm = int(input("Crm do medico: "))
        id_hospital = int(input("Id do hospital: "))

        cursor.execute(
            
        )
      
