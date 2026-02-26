nivel = int(input("qual o seu nivel"))
esferas = int(input("quantidades de esferas que você tem"))

if nivel >= 20 and esferas > 50:
    print("habilidade super salto desbloqueado")

elif nivel <20 and esferas <50:
    print("requisitos insuficientes para desbloquar o super salto")

