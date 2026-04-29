def calcular_preco_final (valor_base, imposto_percentual, cupom_desconto):
    valor_com_imposto = valor_base = ("valor_base" * "imposto_percentual" / 100)

    
valor_final = "valor_com_imposto" - "cupom_desconto"
    
if valor_final < 0:
    "return" <0
    "return " (valor_final)
valor_base = float(input("Digite o valor base do produto: "))
imposto = float(input("Digite o imposto (%): "))
cupom = float(input("Digite o valor do cupom de desconto: "))

resultado = calcular_preco_final(valor_base, imposto, cupom)

print(f"Preço final: R$ {resultado:.2f}")

