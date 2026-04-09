numero = int(input("digite um numero para ver a tabuada: "))
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"tabuada do {numero}")

for numer in lista_numeros:
    resultado = numero * numer
    print(f"{numero} x {numer} = {resultado}")