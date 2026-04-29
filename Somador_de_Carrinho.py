def somar_carrinho(precos):
    total = 0
    for preco in precos:
        total += preco
    
    if total > 500:
        total *= 0.90
    return total

compras = [100.0, 250.0, 200.0] 
valor_final = somar_carrinho(compras)

print(f"O valor final a pagar é: R$ {valor_final}")