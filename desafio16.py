def criar_arquivo():
    open('viagens.txt.', 'w'). close()

def criar():
    lugar = input("DESTINO: ")
    with open('viagens.txt', 'a') as f:
        f.write(lugar + '\n')
    print("Destino adicionado à lista!")


def ler():
    with open('viagens.txt', 'r') as f:
        lugares = f.readlines()

        i = 0
        for l in lugares:
            print(f"{i} - {l.strip()}") 
            i += 1


def atualizar():
    ler()
    idx = int(input("Digite o ID do lugar que deseja alterar: "))
    novo_nome = input("Novo lugar: ")

    with open('viagens.txt', 'r') as f:
        linhas = f.readlines()

    linhas[idx] = novo_nome + '\n'

    with open('viagens.txt', 'w') as f:
        f.writelines(linhas)
    print("Lugar Atualizado!")


def deletar():
    ler()
    idx = int(input("Digite o ID do lugar que deseja excluir: "))
    
    with open('viagens.txt', 'r') as f:
        linhas = f.readlines()
    
    del linhas[idx] 
    
    with open('viagens.txt', 'w') as f:
        f.writelines(linhas)
    print("Lugar removido!")

while True:
    print("\n1-Cadastrar | 2-Listar | 3-Editar | 4-Excluir | 5-Sair")
    opcao = input("Escolha: ")
    
    if opcao == '1': 
        criar()
    elif opcao == '2': 
        ler()
    elif opcao == '3': 
        atualizar()
    elif opcao == '4': 
        deletar()
    elif opcao == '5': 
        print("Encerrando Programa...")
        break