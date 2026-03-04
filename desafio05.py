saldo_inicial = 1000.00
menu = input("qual operação você ira realizar? 1(deposito) 2(saque) 3(extrato):")

if menu == "1":
    deposito = float(input("qual o valor que vc quer depositar"))
    if deposito > 0:

        valor_final = saldo_inicial + deposito

elif menu == "2":
   saque = float(input("qual o valor que vc quer sacar?"))
   if (saque > 0 and saque <= saldo) or valor == 100.00:
        valor_final = saldo_inicial - saque


elif menu == "3":
    print("seu saldo é: ", saldo_inicial)
    valor_final = saldo_inicial
    
print("seu saldo agora é; ", valor_final)

