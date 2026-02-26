sua_idade = int(input("digite sua idade"))
seu_dinheiro = float(input("quanto de dinheiro você tem"))

if sua_idade >= 18 and seu_dinheiro >= 50.0:
    print("acesso autorizado! Bem vindo ao evento")

elif sua_idade <18 and seu_dinheiro > 50.0:
    print("acesso negado")
