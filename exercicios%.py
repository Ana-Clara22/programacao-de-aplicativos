senha = input("qual é a sua senha: ")
tentativas = int(input("qual o numero de tentativas? "))
token = input("voce possui um token? S/N")

if senha == "admin123" or (tentativas % 3 == 0 or token == "S"):
    print(f"tentativa n° {tentativas}: ACESSO CONCEDIDO. ")
else:
    print(f"tentativa n° {tentativas}: ACESSO BLOQUEADO POR PROTOCOLOGO")
    