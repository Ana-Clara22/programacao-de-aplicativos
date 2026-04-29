def analisar_vendas(nome, lista_vendas, meta_mensal):
    media = sum(lista_vendas) / len(lista_vendas)
    if media >= meta_mensal:
        status = "bateu"
    else:
        status = "não bateu"
    return f"O vendedor {nome} teve média de {media:.2f} e {status} a meta"
nome = "Carlos"
vendas = [1200, 1500, 1100, 1900]
meta = 1400
resultado = analisar_vendas(nome, vendas, meta)
print(resultado)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        