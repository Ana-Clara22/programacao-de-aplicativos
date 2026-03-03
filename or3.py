usuario = "admin"
usuario = "root"
senha = 12345

usuario = input("digite seu usuario")
senha = int(input("digite a senha"))

if (usuario == "admin" or usuario == "root") and senha == 12345:
    print("acesso liberado")


