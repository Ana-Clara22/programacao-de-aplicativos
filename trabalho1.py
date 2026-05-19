import json

frase = input("Digite sua mensagem: ")

dados = {
    "mensagem": frase
}

with open("teste.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)

print("Mensagem salva com sucesso em teste.json!")