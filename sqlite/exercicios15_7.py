def busca_palavra():
    palavras = ["banana", "casa", "gato", "laranja", "mesa", "uva"]

    palavra = input("Digite a palavra que deseja procurar: ")

    inicio = 0
    fim = len(palavras) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if palavras[meio] == palavra:
            print("Palavra encontrada no índice:", meio)
            return

        elif palavra < palavras[meio]:
            fim = meio - 1

        else:
            inicio = meio + 1

    print("Palavra não encontrada!")


busca_palavra()
