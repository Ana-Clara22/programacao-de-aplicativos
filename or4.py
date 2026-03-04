valor = float(input("Digite o valor da compra: "))
prime = input("você é prime? S ou N: ")

frete = 50.00

if (valor >= 500.00 or prime == "S") and valor >100.00:
    print("você ganhou freta gratis")
    valor_total = valor + frete
    print("seu valor total é", valor_total)

else:
    frete= 50.00
    valor_total = valor + frete
    print("você não ganhou frete gratis")
    print("seu valor total é", valor_total)
