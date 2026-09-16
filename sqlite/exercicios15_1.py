def busca_sequencial():
    vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numero = int(input("digite o número: "))

    for i in range(len(vetor)):
        if vetor[i] == numero:
            print("número encontrado no índice:", i)
            return

    print("número não encontrado!")
