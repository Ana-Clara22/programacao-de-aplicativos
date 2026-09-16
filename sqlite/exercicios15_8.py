def busca_comparacoes():
    vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numero = int(input("Digite o número que deseja procurar: "))

    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if vetor[meio] == numero:
            print("Número encontrado no índice:", meio)
            print("Quantidade de comparações:", comparacoes)
            return

        elif numero < vetor[meio]:
            fim = meio - 1

        else:
            inicio = meio + 1

    print("Número não encontrado!")
    print("Quantidade de comparações:", comparacoes)


busca_comparacoes()
