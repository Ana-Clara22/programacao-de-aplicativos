def busca_sequencial():
    vetor = list(range(1, 101))

    numero = int(input("Digite o número que deseja procurar: "))

    comparacoes = 0

    for i in range(len(vetor)):
        comparacoes += 1

        if vetor[i] == numero:
            print("Busca sequencial")
            print("Número encontrado no índice:", i)
            print("Comparações:", comparacoes)
            return

    print("Número não encontrado!")
    print("Comparações:", comparacoes)


def busca_binaria():
    vetor = list(range(1, 101))

    numero = int(input("Digite o número que deseja procurar: "))

    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if vetor[meio] == numero:
            print("Busca binária")
            print("Número encontrado no índice:", meio)
            print("Comparações:", comparacoes)
            return

        elif numero < vetor[meio]:
            fim = meio - 1

        else:
            inicio = meio + 1

    print("Número não encontrado!")
    print("Comparações:", comparacoes)


busca_sequencial()
busca_binaria()

