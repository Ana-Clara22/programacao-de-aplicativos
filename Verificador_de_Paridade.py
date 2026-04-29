def eh_par(numero):
    return numero % 2 == 0

num = int(input("Digite um número: "))

if eh_par(num):
     print("Este número é par")                                                                                                       
else:
    print("Este número é ímpar")
