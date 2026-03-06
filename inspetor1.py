comprimento = (input("O comprimento da peça está entre 10 e 12 cm? S/N: "))
largura = (input("A largura esta entre 5cm e 6cm? S/N: "))

if comprimento == "N": 
    print("REPROVADO: Problema no comprimento.")
else:
    print("A largura está entre 5cm e 6cm? S/N: ")
if largura == "S":
    print("PEÇA APROVADA.")
else:
    print("REPROVADO: Problema na largura.")
