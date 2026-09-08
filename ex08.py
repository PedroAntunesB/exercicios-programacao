historico = []

while True:
    print("\n--- HISTÓRICO ---")
    print("1 - Visitar nova página")
    print("2 - Visualizar página atual")
    print("3 - Voltar")
    print("4 - Exibir histórico")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        pagina = input("Digite a página: ")
        historico.append(pagina)
        print("Página visitada!")

    elif opcao == "2":
        if len(historico) == 0:
            print("Nenhuma página visitada.")
        else:
            print("Página atual:", historico[-1])

    elif opcao == "3":
        if len(historico) <= 1:
            print("Não há página anterior.")
        else:
            historico.pop()
            print("Voltando para:", historico[-1])

    elif opcao == "4":
        if len(historico) == 0:
            print("Histórico vazio.")
        else:
            print("\nHistórico:")
            for pagina in historico:
                print(pagina)

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")

# Uma pilha é boa para isso porque ela funciona tipo uma pilha de pratos: o último que você colocou é o primeiro que você tira.
# No histórico acontece a mesma coisa. Por exemplo:
# Google → YouTube → Instagram
# Se você clicar em voltar, sai o Instagram primeiro e você volta para o YouTube.
# Por isso usamos pop(): ele tira a última página adicionada ao histórico.