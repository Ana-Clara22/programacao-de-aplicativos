import json    #importa do python para json
import os        #ve se o arquivo existe

BANCO_DADOS = 'alunos.json'       #isso é uma vaiavel para guardar o nome do arquivo

def cadastrar():      #cria uma função
    print("\n--- Novo Cadastro ---")    #quebra a linha e mostra de um jeito organizadono terminal 
    
    if os.path.exists(BANCO_DADOS):          #se existir um arquivo chamado banco de dados 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:     #com banco_dados aberto em modo de escrever
            alunos = json.load(f)    #aqui ele fez uma variavel para carregar o arquivo de texto
        alunos = []       #cria uma lista chamada alunos vazia 

    novo_aluno = {            #cria um dicionario e um objeto chamado novo_aluno
        "nome": input("Nome: "),      #da linha 16 ate a linha 20 tem a chaves que estão dentro do objeto
        "telefone": input("Telefone: "),      #cria a chave "telefone" no dicionário e guarda o valor digitado pelo usuário no teclado
        "turma": input("Turma: "),     #cria a chave "turma" no dicionário e guarda o valor digitado pelo usuário no teclado
        "idade": int(input("Idade: ")),   #cria a chave "idade" no dicionário e guarda o valor digitado pelo usuário no teclado
        "cpf": input("CPF: ")      #cria a chave "cpf" no dicionário e guarda o valor digitado pelo usuário no teclado
    }      #fecha o dicionario  
    
    alunos.append(novo_aluno)    #adiciona o dicionario nobo_aluno dentro da lista de alunos

    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:     #com banco_dados aberto em modo de escrever
        json.dump(alunos, f, indent=4, ensure_ascii=False)   #salva a lista de alunos no formato json, atendendo o arquivo e organizando 
        
    print("Aluno cadastrado com sucesso!")   #quebra a linha e mostra de um jeito organizadono terminal 


def listar():    #cria uma função
    print("\n--- Lista de Alunos ---")    #quebra a linha e mostra de um jeito organizadono terminal 
    
    if os.path.exists(BANCO_DADOS):           #se existir um arquivo chamado banco de dados 
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:      #com banco_dados aberto em modo de ler
            alunos = json.load(f)    #ele pega o que em no arquivo f e transforma em m objeto
    else:    #se nã existir um arquivo chamado banco_dados 
        alunos = []    #ai ele cria uma nova lista   

    if not alunos:     #se não tiver alunos
        print("Nenhum aluno cadastrado.")     #quebra a linha e mostra de um jeito organizadono terminal 
        return    #encerra a função

    for aluno in alunos:      #percorre cada aluno dentro da lista
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")   #exibe na tela todos os dados do aluno atual formatados e organizados de forma bem clara

def atualizar():    #cria uma função
    print("\n--- Atualizar Aluno ---")      #quebra a linha e mostra de um jeito organizadono terminal 
    if not os.path.exists(BANCO_DADOS):     #se não existir o arquivo banco_dados
        print("Nenhum aluno cadastrado no sistema.")    #mostra no terminal que não tem alunos cadastrados no sistema 
        return     #encerra a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:        #com banco_dados aberto em modo de escrever
        alunos = json.load(f)      #ele pega o que em no arquivo f e transforma em m objeto
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: "))    #aqui digita o cpf para buscar
    
    for aluno in alunos:    #cria um laço que vai passar de aluno em aluno dentro da lista
            print(f"Editando dados de: {aluno['nome']}")     #mostra uma mensagem na tela mostrando o nome do aluno que foi encontrado
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']   #essa linha pede um novo nome para o aluno
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']  #essa linha pede um novo telefone 
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']     #essa linha pede a nova turma do aluno
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])     #essa linha pede a nova idade do aluno
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']     #essa linha pede um novo cpf do aluno
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:        #abre o arquivo do meu bande dados no modo de escrita ('w')
                json.dump(alunos, f, indent=4, ensure_ascii=False)       #salva a lista de alunos no formato json, atendendo o arquivo e organizando 
            print("Dados atualizados com sucesso!")     #mostra a mensagem no terminal
            return    #encerra a função 
            
    print("Aluno não encontrado.")    #mostra a mensagem no terminal

def excluir():    #função excluir aluno
    print("\n--- Excluir Aluno ---")     #mostrando que aluno vai ser excluido
    if not os.path.exists(BANCO_DADOS):   #se nao existir
        print("Nenhum aluno cadastrado no sistema.")      #mostra a mensagem no terminal
        return     #encerra a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:          #com banco_dados aberto em modo de escrever
        alunos = json.load(f)         #ele pega o que em no arquivo f e transforma em m objeto      
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))   #nova variavel de remover o id do aluno digitado
    
    nova_lista = [a for a in alunos if a['id'] != id_busca]      #cria uma nova lista que nao tem os alunos com cpf digitado 
    
    if len(nova_lista) < len(alunos):     #se a nova lista for maior, volte a lista antiga
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:    #com banco_dados aberto em modo de escrever
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)            #salva a lista de alunos no formato json, atendendo o arquivo e organizando 
        print("Aluno removido com sucesso!")      #mostra a mensagem no terminal
    else:
        print("Aluno não encontrado.")       #mostra a mensagem no terminal

def menu():    #funcao de menu
    if not os.path.exists(BANCO_DADOS):   #se nao, verifique se existe o arquivo
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:     #com banco_dados aberto em modo de escrever
            json.dump([], f)   #escreve a lista nova no arquivo

    while True:
        print("\n=== SISTEMA ESCOLAR ===")      #mostra a mensagem no terminal
        print("1. Cadastrar Aluno")        #mostra a mensagem no terminal
        print("2. Listar Alunos")      #mostra a mensagem no terminal
        print("3. Atualizar Aluno")     #mostra a mensagem no terminal
        print("3. Atualizar Aluno")      #mostra a mensagem no terminal
        print("4. Excluir Aluno")       #mostra a mensagem no terminal
        print("5. Sair")       #mostra a mensagem no terminal
        
        opcao = input("Escolha uma opção: ")     # variavel de escolha de opcao 
        
        if opcao == '1': cadastrar()     # se opcao escolhida for 1, mostre cadastrar
        elif opcao == '2': listar()       # se nao. se escolhida 2, mostre listar
        elif opcao == '3': atualizar()      # se nao. se escolhida 3, mostre atualizar
        elif opcao == '4': excluir()     # se nao. se escolhida 4, mostre excluir
        elif opcao == '5': break         # se nao. se escolhida 5, quebrar codigo
        else: print("Opção inválida!")        # se nao, mostre opcao invalida 

menu()      # mostrando menu novamento (loop infinito)