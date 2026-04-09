salarios = [2000.00, 2500.00, 4000.00, 1500.00, 900.00]
for s in salarios:
    if s <= 2000.00:
        imposto = s * 0.10
        percentual = "10%"
    else:
        imposto = s * 0.20
    sobra = s - imposto

    print(f"salário {s}, e foi cobrado {percentual}, de imposto")