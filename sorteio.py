id_usuario = int(input("digite o seu ID do usuario"))
valor = float(input("digite o valor da sua compra"))

if id_usuario % 2 == 0 and valor > 500:
    print(f"parabens, usuario{id_usuario}. Voce ganhou um cupom para sua compra de R$ {valor:>2f}")
else:
    print(f"obrigado pela compra, usuario{id_usuario}. continue acompanhado nossas promoções")
