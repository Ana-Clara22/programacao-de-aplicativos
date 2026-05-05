def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    
    if possui_certificacao:
        return True, "aprovado por possuir certificação"
    elif nota_teste > 80 and anos_xp > 2:
        return True, "aprovado por boa nota e experiência suficiente"
    else:
        return False, "não atende aos critérios mínimos"

nota = int(input("digite sua nota: "))
experiencia = int(input("quantos anos de experiência você tem? "))
certificacao = input("possui certificação? (s/n): ")
if certificacao == "s":
    aprovado, motivo = verificar_aprovacao(nota, experiencia, certificacao)

if aprovado:
    print("Contratar")
else:
    print("Descartar")

print("Motivo:", motivo)