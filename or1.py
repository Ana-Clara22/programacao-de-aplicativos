idade = int(input("digite sua idade"))
ingresso_vip = input("tem ingresso vip? S ou N")
lista = input("seu nome está na lista? S ou N")

if idade >= 18 and (ingresso_vip == "S" or lista == "S"):
    print("acesso liberado")
