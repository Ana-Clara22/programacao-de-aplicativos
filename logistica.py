print("logistica de distribuição (DIVISÃO DE CARGAS) ")

pacote = int(input("qual é o codigo do pacote"))
peso = float(input("qual é o peso do pacote"))

print("------------------------------------------------")

if peso < 5 and (pacote % 10 == 0):
    print(f"pacote {pacote}: ENTREGA EXPRESSA")
elif peso > 50.0:
    print(f"pacote{pacote}: CARGA PESADA")
else:
    print("INFORMAÇÕES INVALIDAS")
