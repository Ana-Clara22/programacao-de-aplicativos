import banco
import escola
import turma
import aluno


def ler_inteiro(mensagem):
    """
    Lê um número inteiro digitado pelo usuário.
    Trata ValueError caso seja digitado texto.
    """
    try:
        return int(input(mensagem))
    except ValueError:
        print("Erro: digite um número inteiro válido.")
        return None
    

def menu_escolas():
    while True:
        print("\n===== MENU DE ESCOLAS =====")
        print("1 - Cadastrar escola")
        print("2 - Listar escolas")
        print("3 - Alterar escola")
        print("4 - Excluir escola")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da escola: ")
            cidade = input("Cidade: ")
            escola.cadastrar_escola(nome, cidade)

        elif opcao == "2":
            escola.listar_escolas()

        elif opcao == "3":
            id_escola = ler_inteiro("ID da escola: ")

            if id_escola is not None:
                nome = input("Novo nome da escola: ")
                cidade = input("Nova cidade: ")
                escola.alterar_escola(id_escola, nome, cidade)

        elif opcao == "4":
            id_escola = ler_inteiro("ID da escola que deseja excluir: ")

            if id_escola is not None:
                escola.excluir_escola(id_escola)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_turmas():
    while True:
        print("\n===== MENU DE TURMAS =====")
        print("1 - Cadastrar turma")
        print("2 - Listar turmas")
        print("3 - Alterar turma")
        print("4 - Excluir turma")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome_turma = input("Nome da turma: ")
            id_escola = ler_inteiro("ID da escola: ")

            if id_escola is not None:
                turma.cadastrar_turma(nome_turma, id_escola)

        elif opcao == "2":
            turma.listar_turmas()

        elif opcao == "3":
            id_turma = ler_inteiro("ID da turma: ")

            if id_turma is not None:
                nome_turma = input("Novo nome da turma: ")
                id_escola = ler_inteiro("Novo ID da escola: ")

                if id_escola is not None:
                    turma.alterar_turma(
                        id_turma,
                        nome_turma,
                        id_escola
                    )

        elif opcao == "4":
            id_turma = ler_inteiro("ID da turma que deseja excluir: ")

            if id_turma is not None:
                turma.excluir_turma(id_turma)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def menu_alunos():
    while True:
        print("\n===== MENU DE ALUNOS =====")
        print("1 - Cadastrar aluno")
        print("2 - Listar alunos")
        print("3 - Alterar aluno")
        print("4 - Excluir aluno")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ")
            idade = ler_inteiro("Idade: ")
            id_turma = ler_inteiro("ID da turma: ")

            if idade is not None and id_turma is not None:
                aluno.cadastrar_aluno(
                    nome,
                    idade,
                    id_turma
                )

        elif opcao == "2":
            aluno.listar_alunos()

        elif opcao == "3":
            id_aluno = ler_inteiro("ID do aluno: ")

            if id_aluno is not None:
                nome = input("Novo nome: ")
                idade = ler_inteiro("Nova idade: ")
                id_turma = ler_inteiro("Novo ID da turma: ")

                if idade is not None and id_turma is not None:
                    aluno.alterar_aluno(
                        id_aluno,
                        nome,
                        idade,
                        id_turma
                    )

        elif opcao == "4":
            id_aluno = ler_inteiro("ID do aluno que deseja excluir: ")

            if id_aluno is not None:
                aluno.excluir_aluno(id_aluno)

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


def main():
    banco.criar_tabelas()

    while True:
        print("\n" + "=" * 40)
        print("       SISTEMA DE GESTÃO ESCOLAR")
        print("=" * 40)
        print("1 - Gerenciar escolas")
        print("2 - Gerenciar turmas")
        print("3 - Gerenciar alunos")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_escolas()

        elif opcao == "2":
            menu_turmas()

        elif opcao == "3":
            menu_alunos()

        elif opcao == "0":
            print("Sistema encerrado. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
