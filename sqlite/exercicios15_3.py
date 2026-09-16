def maior():
    vetor = [10, 50, 30, 90, 20]

    maior = vetor[0]
    posicao = 0

    for i in range(len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i

    print("maior número:", maior)
    print("posição:", posicao)
