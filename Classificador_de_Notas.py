def avaliar_desempenho(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota > 5:
        return "Regular"
    else:
        return "Insuficiente"
    
nota_usuario = int(input("Qual a sua nota? "))
mensagem = avaliar_desempenho(nota_usuario)
print(mensagem)

    
