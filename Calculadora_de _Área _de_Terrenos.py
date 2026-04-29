def calcular_area(largura, comprimento):
    return largura * comprimento

contador = 1
while contador <= 3:
    print(f"\nTerreno {contador}:")
    l = float(input("Largura: "))
    c = float(input("Comprimento: "))
    
    area = calcular_area(l, c)
    print(f"A área do terreno {contador} é: {area}m²")
    
    contador += 1 
