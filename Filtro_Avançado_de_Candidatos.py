def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    
    if possui_certificacao == 's':
        return "contratar"
    elif nota_teste > 80 and anos_xp > 2:
        return "contratar"
    else:
        return "descartar"

nota = int(input("digite sua nota: "))
experiencia = int(input("quantos anos de experiência você tem? "))
certificacao = input("possui certificação? (s/n): ")
retorno = verificar_aprovacao(nota, experiencia, certificacao)
print(retorno)
