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
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
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
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")      # ------------

def atualizar():    #cria uma função
    print("\n--- Atualizar Aluno ---")      #quebra a linha e mostra de um jeito organizadono terminal 
    if not os.path.exists(BANCO_DADOS):     #se não existir o arquivo banco_dados
        print("Nenhum aluno cadastrado no sistema.")    #mostra no terminal que não tem alunos cadastrados no sistema 
        return     #encerra a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:        #com banco_dados aberto em modo de escrever
        alunos = json.load(f)      #ele pega o que em no arquivo f e transforma em m objeto
        
    cpf_busca = int(input("Digite o CPF do aluno que deseja editar: "))    #aqui digita o cpf para buscar
    
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca:
            print(f"Editando dados de: {aluno['nome']}")
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)       #salva a lista de alunos no formato json, atendendo o arquivo e organizando 
            print("Dados atualizados com sucesso!")
            return    #encerra a função 
            
    print("Aluno não encontrado.")

def excluir():
    print("\n--- Excluir Aluno ---")
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return     #encerra a função

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:          #com banco_dados aberto em modo de escrever
        alunos = json.load(f)         #ele pega o que em no arquivo f e transforma em m objeto      
        
    id_busca = int(input("Digite o ID do aluno que deseja remover: "))
    
    nova_lista = [a for a in alunos if a['id'] != id_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:    #com banco_dados aberto em modo de escrever
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)            #salva a lista de alunos no formato json, atendendo o arquivo e organizando 
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:     #com banco_dados aberto em modo de escrever
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()