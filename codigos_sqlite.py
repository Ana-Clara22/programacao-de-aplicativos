import sqlite3

cursor.execute(''' 
               CREATE TABLE IF NOTE EXIST ALUNOS( 
               id INTEGER PRIMARY AUTOINOREMENT, 
               nome TEXT NOT NULL, 
               idade INTEGER,
               telefone TEXT,
               turma TEXT,
               id_professor INTEGER
               FOREIN KEY (id_professor) REFERNCES professor(id)
               )
               ''')