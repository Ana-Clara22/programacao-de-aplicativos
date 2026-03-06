codigo = int(input("Digite o codigo do drone: "))
autorizacao = input("possui a autorização da torre? S/N: ")

if codigo == 999 or autorizção == "S":
    print("OK! drone autorizado.")
    bateria = int(input("Nível de Bateria (0 a 100): "))
    clima = input("Clima (ensolarado/chuvoso): ")
    vento = float(input("Velocidade do Vento (km/h): "))

if bateria < 10:
    print("pouso autorizado imediatamente, por segurança") 
elif bateria >= 10:
    if (clima ==  "ensolarado" and vento < 30) or (clima == "chuvuso" and vento < 10):
        print("pouso autorizado")
    else:
        print("pouso negado, condiçõs de clima perigosas.")
else:
    print("ERRO: drone não identificado.")