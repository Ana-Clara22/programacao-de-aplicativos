ano = int(input("que ano é: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0 ):
    print(f"0 ano {ano} é bissexto")
else:
    print(f"0 ano {ano} é um ano comum")
