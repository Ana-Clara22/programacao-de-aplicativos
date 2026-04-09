saldo = 500
opcao = 0 
while opcao != "3":
    print("-----Caixa eletrônico-----")
    print("1- Depositar")
    print("2- Sacar")
    print("3- Sair")

    opcao = input("O que você deseja fazer? ")

    if opcao == "1":
        depositar = float(input("Qual valor você deseja depositar?: R$"))
        saldo = saldo + depositar
        print(f"Depósito realizado R${saldo}")

    if opcao == "2":
        saque = float(input("Qual é o valor que você deseja sacar?: R$"))
        
        if saque <= saldo:
            saldo = saldo - saque
            print(f"Saque realizado! Novo saldo: R${saldo}")
        else:
            print("Operação negada! Saldo insuficiente.")

