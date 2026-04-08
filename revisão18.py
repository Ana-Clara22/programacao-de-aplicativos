numeros = [12, 45, 7, 89, 23, 56]

maior_valor = numeros[0]

for numero in numeros:
    if numero > maior_valor:
        maior_valor = numero

print(f"O maior valor é: {maior_valor}")
