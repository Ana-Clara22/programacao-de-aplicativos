def converter_km_para_ms(velocidade_km):
    return velocidade_km / 3.6

vel = float(input("Digite a velocidade em km/h: "))

if vel > 80:
    ms = converter_km_para_ms(vel)
    print(f"Velocidade: {ms:.2f} m/s. Reduza a velocidade!")
else:
    print("Velocidade dentro do limite.")
