sua_nota = float(input("digite sua nota"))
presenca = int(input("digite a porcentagem de presença"))

if sua_nota >= 7.0 and presenca >= 75:
    print("parabéns você foi aprovado")

elif sua_nota < 7.0 and presenca <75:
    print("reprovado, você não passou")
    