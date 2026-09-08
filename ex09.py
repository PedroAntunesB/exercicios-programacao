from datetime import datetime

fila = []
senha = 1

while True:
    print("\n--- SISTEMA DE ATENDIMENTO ---")
    print("1 - Adicionar pessoa")
    print("2 - Chamar próxima pessoa")
    print("3 - Consultar próxima pessoa")
    print("4 - Mostrar fila")
    print("5 - Quantidade de pessoas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        horario = datetime.now().strftime("%H:%M:%S")

        pessoa = [senha, nome, horario]
        fila.append(pessoa)

        print("Pessoa adicionada!")
        print("Senha:", senha)

        senha += 1

    elif opcao == "2":
        if len(fila) == 0:
            print("A fila está vazia.")
        else:
            pessoa = fila.pop(0)
            print("Próxima pessoa:", pessoa[1])
            print("Senha:", pessoa[0])

    elif opcao == "3":
        if len(fila) == 0:
            print("A fila está vazia.")
        else:
            print("Próxima pessoa:", fila[0][1])
            print("Senha:", fila[0][0])

    elif opcao == "4":
        if len(fila) == 0:
            print("A fila está vazia.")
        else:
            print("\n--- FILA ---")

            for pessoa in fila:
                print("Senha:", pessoa[0])
                print("Nome:", pessoa[1])
                print("Horário:", pessoa[2])
                print()

    elif opcao == "5":
        print("Pessoas aguardando:", len(fila))

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")

# Explicação
# Porque no atendimento normalmente funciona assim: quem chega primeiro é atendido primeiro.
# Por exemplo:
# João → Maria → Pedro
# O João chegou primeiro, então ele deve ser atendido primeiro.