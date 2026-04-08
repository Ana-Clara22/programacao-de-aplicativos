valor = float(input("Qual é o valor da compra? R$:"))
if valor > 100.00:
    desconto = valor * 0.10
    final = valor - desconto
    print(f"Sua compra teve um desconto: R${final}")
else:
    print(f"Valor da sua compra: R${valor}")

