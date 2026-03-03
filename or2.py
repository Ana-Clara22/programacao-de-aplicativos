media_escolar = float(input("digite sua media escolar"))
renda_familiar = float(input("digite sua renda familiar"))
escola = input("você veio de escola pública? S ou N")

if media_escolar > 8.0 and (renda_familiar < 2000 or escola == "S"):
    print("você ganhou a bolsa")

elif media_escolar < 8.0 and (renda_familiar > 2000 or escola == "N"):
    print("vc não ganhou a bolsa")

