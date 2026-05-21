import json

aluno = {
    "nome": "Ricardo",
    "idade": 22,
    "aprovado": True,
    "materias": ["Lógica", "Python"]
}

#__________________________________________________________________________________________________

# Escrever

# 'w' para escrever do zero
with open('dados_aluno.json', 'w', encoding='utf-8') as arquivo:
    # dump = despejar/carregar
    # indent=4 deixa o arquivo organizado com espaços
    # ensure_ascii - Lidar com pontuação
    json.dump(aluno, arquivo, indent=4, ensure_ascii=False)

print("Arquivo JSON criado com sucesso!")

#__________________________________________________________________________________________________

# Ler

with open('dados_aluno.json', 'r', encoding='utf-8') as arquivo:
    # load = carregar
    dados_recuperados = json.load(arquivo)

# Agora podemos acessar as chaves normalmente
print(f"O aluno {dados_recuperados['nome']} está na matéria {dados_recuperados['materias'][0]}")


#_________________________________________________________________________________________________

# Alterar

# PASSO 1: Carregar o que já existe
with open('dados_aluno.json', 'r') as arquivo:
    dados = json.load(arquivo)

# PASSO 2: Modificar a informação na memória
dados['idade'] = 23  # O aluno fez aniversário
dados['materias'].append("JSON")  # Adicionamos uma nova matéria à lista

# PASSO 3: Salvar o dicionário atualizado de volta no arquivo
with open('dados_aluno.json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)

print("Dados atualizados!")




#__________________________________________________________________________________________________

# Excluir

import json

# 1. Carregar os dados para a memória
with open('dados_aluno.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# 2. Remover a chave específica usando 'del'
if 'idade' in dados:
    del dados['idade']
    print("Campo 'idade' removido com sucesso!")

# 3. Salvar o dicionário (agora menor) de volta no arquivo
with open('dados_aluno.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)


#__________________________________________________________________________________________________

# Excluir

# Supondo que o JSON tenha: {"materias": ["Lógica", "Python", "JSON"]}

with open('dados_aluno.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# Vamos remover a matéria "Lógica"
if "Lógica" in dados['materias']:
    dados['materias'].remove("Lógica")
    print("Matéria removida da lista!")

# Salvar a lista atualizada
with open('dados_aluno.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)