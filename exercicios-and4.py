nome = "admin"
usuario = input("digite o seu usuario")
codigo = int(input ("digite o seu código"))

if usuario == "admin" and codigo == 999:
    print("acesso ao servidor liberado.")
    
else: 
    print("acesso negado!")