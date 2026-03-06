temperatura = float(input("digite a temperatura atual (°C): "))

if temperatura <= 30:
    print("clima estável!")

else:
    print("alerta de calor!")
    umidade = float(input("digite a umidade atual (%)"))
    if umidade < 40:
        print("ação: ligar irrigaçâo!")
    else:
         print("açâo: ligar apenas ventiladores!")
