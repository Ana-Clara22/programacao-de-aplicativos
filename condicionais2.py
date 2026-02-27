ataque = int(input("poder de ataque do herói"))
defesa = int(input("poder de defesa do vilão"))

dano = ataque - defesa

if ataque <= defesa:
    print("o vilão bloqueou o seu ataque, dano 0", dano)

elif ataque > defesa:
    print("ataque critico, você casou dano no vilão, o dano causado foi:", dano)
