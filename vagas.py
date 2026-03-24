status = input("digite o seu status")
vagas = ["Ocupado", "Livre", "Ocupado", "Livre"]
numero = int(input("digite o numero da vaga de 0 a 3"))

if vagas %2 ==0 and status == "livre":
    print(f"vaga {vagas}")
else:
    print(f"vagas{1} não autorizada")
