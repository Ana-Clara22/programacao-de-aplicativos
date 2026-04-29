
def esta_na_lista(lista_nomes, busca):
    for nome in lista_nomes:
        if nome == busca:
            return "Encontrado!"
    return "Não disponível"

ferramentas = ["Martelo", "Chave de fenda", "Alicate"]
item_procurado = input("Qual ferramenta você busca? ")

resultado = esta_na_lista(ferramentas, item_procurado)
print(f"Resultado da busca: {resultado}")