def procurar_nome():
    alunos = ["Ana", "João", "Maria", "Pedro"]

    nome = input("Digite o nome: ")

    for i in range(len(alunos)):
        if alunos[i] == nome:
            print("Aluno encontrado!")
            return

    print("Aluno não encontrado!")
