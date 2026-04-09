nomes = ["Aline", "Marina", "Ana", "Paulo"]

antigo = input("Qual nome você quer mudar? ")
novo = input("Qual o novo nome? ")

for i in range(len(nomes)):
    if nomes[antigo] == antigo:
        nomes[novo] = novo

print("Lista atualizada:", nomes)