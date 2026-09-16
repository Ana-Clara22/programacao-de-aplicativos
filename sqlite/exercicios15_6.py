def busca_binaria():
    vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    numero = int(input("Digite o número que deseja procurar: "))

    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == numero:
            print("Número encontrado no índice:", meio)
            return

        elif numero < vetor[meio]:
            fim = meio - 1

        else:
            inicio = meio + 1

    print("Número não encontrado!")


busca_binaria()
