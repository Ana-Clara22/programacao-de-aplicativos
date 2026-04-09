notas = [ ] 

n1 = float(input("Nota 1: "))
notas.append(n1)
n2 = float(input("Nota 2: "))
notas.append(n2)
n3 = float(input("Nota 3: "))
notas.append(n3)
n4 = float(input("Nota 4: "))
notas.append(n4)

soma = 0
for numero in notas:
    soma = soma + numero

media = soma / 4

print("Média:", media)


if media >= 7:
    print("Aprovado")
elif media >= 5: 
    print("Recuperação")
else:
    print("Reprovado")