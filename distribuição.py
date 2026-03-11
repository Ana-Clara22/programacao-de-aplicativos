codigo = int(input("qual o codigo do pacote?"))
peso = float(input("digite o peso do pacote"))

if peso < 5 and (codigo % 10 == 0):
    print(f"pacote {codigo}: ENTREGA EXPRESSA")
elif peso > 50:
print(f"pacote{codigo}: CARGA PESADA")
