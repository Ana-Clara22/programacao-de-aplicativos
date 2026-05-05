def gerar_relatorio_saude(nome, peso, altura, idade):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Baixo peso"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    return f"{nome}, aos {idade} anos, possui IMC de {imc:.2f}, classificado como {categoria}."

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
idade = int(input("Digite sua idade: "))
relatorio = gerar_relatorio_saude(nome, peso, altura, idade)
print(relatorio)