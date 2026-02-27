valor_total_de_compra = float(input("digite o valor da compra"))
cupom = input("digite o nome do cupom")
nome = "DEV10"
desconto = valor_total_de_compra * 0.10
novo_valor = valor_total_de_compra - desconto

if cupom == "DEV10":
    print("cupom aplicado", novo_valor)

else:
    print("cupom invalido!", valor_total_de_compra)
    

