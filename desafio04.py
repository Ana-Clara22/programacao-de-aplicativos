cargo = input("seu cargo: ")
código_de_acesso = int(input("digite o codigo de acesso: "))
botão = input("botão de emergencia pressionado? S ou N: ")
eqipamento_epi = input("EPI completo? S ou N: ")

if (cargo == "engenheiro" or "tecnico") and (código_de_acesso == 1234 or botão == "S") and eqipamento_epi == "S":
    print("acesso liberado")
else:
    print("acesso negado")
