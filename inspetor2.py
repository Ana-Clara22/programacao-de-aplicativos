curso = input("voce concluiu o curso de segurança? s/n: ")

if curso == "s":
    instrutor = input("o instrutor está na sala? s/n: ")
    if instrutor == "s":
        print("acesso liberado")
    else: 
        print("aguarde o instrutor")
else:
    print("acesso negado")