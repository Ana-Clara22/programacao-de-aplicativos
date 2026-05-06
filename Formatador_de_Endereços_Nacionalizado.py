def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    etiqueta = f"RUA: {rua}, Nº: {numero} - BAIRRO: {bairro} - CIDADE: {cidade} - CEP: {cep}"
    return etiqueta

rua = input("Digite a rua: ")
numero = input("Digite o número: ")
bairro = input("Digite o bairro: ")
cidade = input("Digite a cidade: ")
cep = input("Digite o CEP: ")

resultado = gerar_etiqueta(rua, numero, bairro, cidade, cep)
print("Etiqueta gerada:")
print(resultado)