def exibir_menu():
    print("===== MENU PRINCIPAL =====")
    print("1 - Iniciar")
    print("2 - Configurações")
    print("3 - Sair")
    print("==========================")

# chamada da função
exibir_menu()               #definição da função



#--------------------------------------------------------------------------------------------------------------------------------------------------


def saudar_usuario(nome):                                  #definição da função
    print(f"Olá, {nome}! Seja bem-vindo!")

# chamada da função
saudar_usuario("Maria")

#--------------------------------------------------------------------------------------------------------------------------------------------------

#Python function return calculate area" ou "Função python retornar maior valor

def calcular_area(largura, altura):
    area = largura * altura
    return area                                         #RETURN

# programa principal
resultado = calcular_area(5, 3)
print(f"A área é: {resultado}")                                #O valor retornado vai para o local onde a função foi chamada.

#--------------------------------------------------------------------------------------------------------------------------------------------------

def dobro(n):          # Linha 1
    resultado = n * 2  # Linha 2
    return resultado   # Linha 3

# Sua Explicação Linha por Linha:
# Linha 1: Define a função chamada dobro que espera receber um valor (parâmetro n).
# Linha 2: Cria uma variável interna (local) que armazena o dobro do valor recebido.
# Linha 3: "Cospe" o resultado para fora da função, finalizando a execução.

#--------------------------------------------------------------------------------------------------------------------------------------------------

# isso quebra o código 

# Veja este exemplo incorreto:                                                                                         

# def calcular_area(largura, altura):
# area = largura * altura
# return area

# O que acontece aqui?
# O Python usa indentação (espaços à esquerda) para entender o que pertence à função
# Como area = ... e return area estão na mesma coluna do def, eles não fazem parte da função

#Forma correta (com indentação)
 def calcular_area(largura, altura):
    area = largura * altura
    return area
# Agora as linhas estão indentadas (geralmente 4 espaços)
# Isso indica que elas pertencem à função


# Regra importante
# Tudo que faz parte da função deve estar indentado abaixo do def
# Se o return não estiver indentado:
# Ele não pertence à função
# Ou o código nem roda (erro de indentação)

#--------------------------------------------------------------------------------------------------------------------------------------------------

# não consegue (diretamente).

# Por quê?
# Porque variáveis criadas dentro de uma função têm escopo local — elas só existem dentro da função onde foram definidas.


#Exemplo
def minha_funcao():
    x = 10
    print("Dentro da função:", x)

minha_funcao()

print("Fora da função:", x)  # erro!                           Isso acontece porque x foi criada dentro da função e não existe fora dela.


#Como resolver isso?
✅  return (melhor prática)
def minha_funcao():
    x = 10
    return x

valor = minha_funcao()
print("Fora da função:", valor)



# Variáveis dentro da função → escopo local
# Não podem ser usadas fora diretamente
# Para “levar” o valor para fora → use return

#--------------------------------------------------------------------------------------------------------------------------------------------------


# Reutilização

# Você pode usar a função quantas vezes quiser sem reescrever o cálculo:

def somar(a, b):
    return a + b

print(somar(2, 3))
print(somar(10, 5))

# rganização do código

# Funções ajudam a deixar o código mais limpo e fácil de entender:

def calcular_area(l, a):
    return l * a


# Facilidade de manutenção

# Se precisar mudar o cálculo, você altera em um só lugar:

def calcular_area(l, a):
    return (l * a) / 2  # mudança feita aqui


#------------------------------------------------------FIM-------------------------------------------------------------------------------