def sofrer_dano(vida_atual, valor_dano):
    nova_vida = vida_atual - valor_dano
    return nova_vida

vida_personagem = 100
print(f"Início da Batalha! Vida: {vida_personagem}")

while vida_personagem > 0:
    dano = float(input("Quanto de dano o monstro causou? "))
    vida_personagem = sofrer_dano(vida_personagem, dano)
    
    if vida_personagem > 0:
        print(f"Vida restante: {vida_personagem}")
    else:
        print("Vida chegou a 0.")

print("Game Over!")