def senha_valida(senha):
    while len(senha) < 6:
        print("senha invalida!")
        senha = input ("digite a sua senha novamnte")
        if len (senha) >= 6:
            print("senha cadastrada com sucesso")

pedir_senha = input("digite sua senha")
senha_valida(pedir_senha)
  