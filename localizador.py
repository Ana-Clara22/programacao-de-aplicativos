cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
cidade = input("digite um nome de uma cidade")

if cidades in cidade:
    print(f"A cidade {cidade} está na posição {cidade.index(cidade)}")
else:
    print("ERRO")