def contar_valor():
    vetor = [10, 20, 10, 30, 10, 40]

    numero = int(input("digite o número: "))
    contador = 0

    for i in range(len(vetor)):
        if vetor[i] == numero:
            contador += 1

    print("o número aparece", contador, "vezes.")
