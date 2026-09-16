def posicao_insercao():
    vetor = [10, 20, 30, 40, 50, 60, 70, 80]

    numero = int(input("Digite o número que deseja inserir: "))

    inicio = 0
    fim = len(vetor)

    while inicio < fim:
        meio = (inicio + fim) // 2

        if vetor[meio] < numero:
            inicio = meio + 1
        else:
            fim = meio

    print("O número deve ser inserido no índice:", inicio)


posicao_insercao()
