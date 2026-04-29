def aplicar_promocao(lista_precos):
    nova_lista = []
    for preco in lista_precos:
        if preco > 100:
            nova_lista.append(preco * 0.85)
        else:
            nova_lista.append(preco)
    return nova_lista
 
    
compras = [150.0, 80.0, 200.0, 50.0]
lista_atualizada = aplicar_promocao(compras)

print(f"Lista original: {compras}")
print(f"Lista com descontos: {lista_atualizada}")
