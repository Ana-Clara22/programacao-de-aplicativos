lista_secreta = ["123"]
tentativas = 0
acertou = False 

while tentativas < 3 and not acertou:
    palpite = input("Tente adivinhar a senha: ")
    
    if palpite in lista_secreta:
        print("Acesso liberado!")
        acertou = True
    else:
        print("Senha incorreta")
    
    tentativas += 1
if not acertou:
    print("Suas tentativas acabaram.")
    print("A senha era:", lista_secreta)