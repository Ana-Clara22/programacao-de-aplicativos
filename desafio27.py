nome_do_cliente = str(input("digite o seu nome"))
valor_total_da_compra = float(input("digite o valor da compra"))
distancia_da_entrega = int(input("digite a distancia da entrega em km"))
cupom = input("digite se que cupom, sim ou não")
 
if valor_total_da_compra >= 1.000 and cupom =="sim":
    desconto_vip = 0.20 * valor_total_da_compra
    total = valor_total_da_compra - desconto_vip
    print("voce ganhou um desconto de 20%, seu valor agora é:", novo_valor_vip)

elif valor_total_da_compra >500 and valor_total_da_compra < 1000 and cupom == "sim":
    desconto_padrão = 0.10 * valor_total_da_compra
    total = valor_total_da_compra - desconto_padrão
    print("você ganhou um desconto de 10%, seu valor agora é:", novo_valor_padrão)
 
elif distancia_da_entrega <= 50 and novo_valor_vip > 200:
    print("você conseguiu frete gratis")
elif distancia_da_entrega <= 50 and novo_valor_padrão > 200:
    print("você conseguiu frete gratis")
elif distancia_da_entrega >50 and valor_total_da_compra < 1000:
    print("sem frete gratis")
elif distancia_da_entrega >50 and valor_total_da_compra < 500:
    print("sem frete gratis")
