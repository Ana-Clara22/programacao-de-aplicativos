livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
livros = input("qual livro vc quer? ")
if livros_emprestados in livros_disponiveis:
    livros_disponiveis.remove(livros)
    livros_disponiveis.remove(livros)
else:
    print("desculpe este item não esta no acervo")

livros = input("digite o mome do livro que está devolvendo: ")
if livros in livros_emprestados: 
    livros_emprestados.remove(livros)
    livros_disponiveis.append(livros)
else:
    print("este livro não consta como emprestado")

del livros_emprestados[0:2]
print(f"estado fnal das duas listas {livros_disponiveis}  e {livros_emprestados}")