def primeira_ultima():
    vetor = [10, 20, 10, 30, 10, 40]

    numero = int(input("Digite o número: "))

    primeira = -1
    ultima = -1

    for i in range(len(vetor)):
        if vetor[i] == numero:
            if primeira == -1:
                primeira = i
            ultima = i

    print("Primeira posição:", primeira)
    print("Última posição:", ultima)
