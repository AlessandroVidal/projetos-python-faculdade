print("Desenvolvido por Alessandro Vidal Bispo | RU - 5478620")
print("Bem-vindo à Empresa de Contabilidade")

lista_funcionarios = []
id_global = 594934


def cadastrar_funcionario(id_func):
    print(f"\nCadastro do funcionário (ID: {id_func})")
    nome = input("Nome do funcionário: ")
    setor = input("Setor: ")

    try:
        salario = float(input("Salário: R$ "))
    except ValueError:
        print("Entrada inválida para salário. Cadastro cancelado.")
        return

    funcionario = {
        "id": id_func,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")


def exibir_funcionario(f):
    print(f'ID: {f["id"]} | Nome: {f["nome"]} | Setor: {f["setor"]} | Salário: R$ {f["salario"]:.2f}')


def consultar_funcionario():
    while True:
        print("\nConsulta de funcionários")
        print("1. Consultar todos")
        print("2. Consultar por ID")
        print("3. Consultar por setor")
        print("4. Retornar ao menu")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if not lista_funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                for f in lista_funcionarios:
                    exibir_funcionario(f)

        elif opcao == "2":
            try:
                id_busca = int(input("Digite o ID: "))
            except ValueError:
                print("ID inválido.")
                continue

            encontrado = False
            for f in lista_funcionarios:
                if f["id"] == id_busca:
                    exibir_funcionario(f)
                    encontrado = True
                    break

            if not encontrado:
                print("Funcionário não encontrado.")

        elif opcao == "3":
            setor_busca = input("Digite o setor: ").strip().lower()
            encontrados = [f for f in lista_funcionarios if f["setor"].strip().lower() == setor_busca]

            if encontrados:
                for f in encontrados:
                    exibir_funcionario(f)
            else:
                print("Funcionário não encontrado nesse setor.")

        elif opcao == "4":
            return

        else:
            print("Opção inválida.")


def remover_funcionario():
    while True:
        try:
            id_remover = int(input("Digite o ID do funcionário para remover: "))
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        for f in lista_funcionarios:
            if f["id"] == id_remover:
                lista_funcionarios.remove(f)
                print("Funcionário removido com sucesso!")
                return

        print("Funcionário não encontrado. Tente novamente.")


while True:
    print("\nMENU PRINCIPAL")
    print("1. Cadastrar funcionário")
    print("2. Consultar funcionário")
    print("3. Remover funcionário")
    print("4. Encerrar programa")

    escolha = input("Escolha a opção: ")

    if escolha == "1":
        cadastrar_funcionario(id_global)
        id_global += 1
    elif escolha == "2":
        consultar_funcionario()
    elif escolha == "3":
        remover_funcionario()
    elif escolha == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
