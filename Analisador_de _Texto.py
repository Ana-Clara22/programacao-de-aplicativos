def contar_caracteres(texto):
    return len(texto)

usuario = input("Digite seu nome de usuário: ")

if contar_caracteres(usuario) < 5:
    print("Nome de usuário muito curto")
else:
    print("Nome aceito")
