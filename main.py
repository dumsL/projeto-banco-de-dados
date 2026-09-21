from funcionario import Funcionario
from funcionarioDAO import FuncionarioDAO

from cliente import Cliente
from clienteDAO import ClienteDAO

from conexao import conectar

funcionarioDAO = FuncionarioDAO()
clienteDAO = ClienteDAO()

# Solicita a senha apenas uma vez
conectar()

def menu_funcionarios():

    while True:

        print("\n===== FUNCIONÁRIOS =====")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Consultar")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":

            cpf = input("CPF: ")
            nome = input("Nome: ")
            funcao = input("Função: ")

            funcionario = Funcionario(
                cpf=cpf,
                nome=nome,
                funcao=funcao
            )

            funcionarioDAO.inserir(funcionario)

            print("Funcionário cadastrado!")

        elif op == "2":

            funcionarios = funcionarioDAO.listar()

            for f in funcionarios:
                print(f"ID: {f[0]}, CPF: {f[1]}, Nome: {f[2]}, Função: {f[3]}")

        elif op == "3":

            nome = input("Nome do funcionário: ")

            funcionarios = funcionarioDAO.buscar_por_nome(nome)

            if funcionarios:
                for funcionario in funcionarios:
                    print(f"ID: {funcionario.id_funcionario}, CPF: {funcionario.cpf}, Nome: {funcionario.nome}, Função: {funcionario.funcao}")
            else:
                print("Nenhum funcionário encontrado.")

        elif op == "4":

            nome_busca = input("Digite o nome do funcionário que deseja alterar: ")
            funcionarios = funcionarioDAO.buscar_por_nome(nome_busca)

            if funcionarios:
                print("\nFuncionários encontrados:")
                for funcionario in funcionarios:
                    print(f"ID: {funcionario.id_funcionario}, CPF: {funcionario.cpf}, Nome: {funcionario.nome}, Função: {funcionario.funcao}")

                cpf = input("\nDigite o CPF do funcionário que deseja alterar: ")

                # Verificar se o CPF existe
                funcionario = funcionarioDAO.buscar_por_cpf(cpf)
                if funcionario:
                    novo_nome = input("Novo nome: ")
                    nova_funcao = input("Nova função: ")

                    funcionarioDAO.atualizar(cpf, novo_nome, nova_funcao)
                    print("Atualizado com sucesso!")
                else:
                    print("Funcionário não encontrado com este CPF.")

            else:
                print("Nenhum funcionário encontrado com este nome.")

        elif op == "5":

            cpf = input("CPF: ")

            funcionarioDAO.excluir(cpf)

            print("Funcionário removido!")

        elif op == "0":
            break

        else:
            print("Opção inválida.")


def menu_clientes():

    while True:

        print("\n===== CLIENTES =====")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Consultar")
        print("4 - Atualizar")
        print("5 - Excluir")
        print("0 - Voltar")

        op = input("Escolha: ")

        if op == "1":

            cpf = input("CPF: ")
            nome = input("Nome: ")
            telefone = input("Telefone: ")

            cliente = Cliente(
                cpf=cpf,
                nome=nome,
                telefone=telefone
            )

            clienteDAO.inserir(cliente)

            print("Cliente cadastrado!")

        elif op == "2":

            clientes = clienteDAO.listar()

            for c in clientes:
                print(f"CPF: {c[0]}, Nome: {c[1]}, Email: {c[2]}, Rua: {c[3]}, Bairro: {c[4]}, Numero: {c[5]}, Teleone1: {c[6]}, Telefone2: {c[7]}")

        elif op == "3":

            nome = input("Nome do cliente: ")
            clientes = clienteDAO.buscar_por_nome(nome)

            if clientes:
                for cliente in clientes:
                    print(f"CPF: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]},Rua: {cliente[3]}, Bairro: {cliente[4]}, Numero: {cliente[5]}, "
                          f"Telefone1: {cliente[6]},Telefone2: {cliente[7]}")
            else:
                print("Nenhum cliente encontrado.")

        elif op == "4":

            cpf = input("CPF do cliente a ser alterado: ")

            cliente = clienteDAO.buscar_por_cpf(cpf)

            if cliente:
                print(f"Cliente encontrado: CPF: {cliente[0]}, Nome: {cliente[1]}, Telefone: {cliente[6]}")

                nome = input("Novo nome: ")
                telefone1 = input("Novo telefone: ")

                clienteDAO.atualizar(cpf, nome, telefone1)

                print("Cliente atualizado!")

            else:
                print("Cliente não encontrado.")

        elif op == "5":

            cpf = input("CPF: ")

            clienteDAO.excluir(cpf)

            print("Cliente removido!")

        elif op == "0":
            break

        else:
            print("Opção inválida.")


while True:

    print("\n=================================")
    print("      SISTEMA DE CADASTROS")
    print("=================================")
    print("1 - Gerenciar Funcionários")
    print("2 - Gerenciar Clientes")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu_funcionarios()

    elif opcao == "2":
        menu_clientes()

    elif opcao == "0":
        conectar().close()
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")