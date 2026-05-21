import json
def criar_arquivo():
    with open('alunos.json', 'w') as arquivo:
        json.dump ("alunos.json", indent = 4, ensure_ascii=false)

cpf = int(input("digite seu cpf: "))
nome = (input("digite seu nome completo: "))
telefone = (input("digite seu telefone: "))
turma = int(input("digite sua turma:"))
idade = int(input("digite sua idade:"))
print()