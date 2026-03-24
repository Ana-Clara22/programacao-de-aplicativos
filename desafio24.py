nomes = ["Alice", "Bob", "Carlos"]
dados = input("digite um nome de um pesquisador ")

if nomes == "Alice" or "Bob" or "Carlos":
    print(f"Acesso permitido! O pesquisador {nomes} está na posição {nomes.index(nomes)}")
    pergunta = input("Você deseja retirar esse nome da lista? S/N ")
    if nomes == "S":
        nomes.remove(dados)
        print(f"agora lista nova é {nomes}")
    else:
        print("programa encerrado")

else:
    print(f"Acesso negado o pesquisador {nomes} não foi encontrado")
    pergunta2 = input("deseja cadastrar esse novo pesquisador? S/N ")
    if pergunta2 == "S":
        nomes.append = (dados)
        print(f"agora lista nova é {nomes}")
