def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b


def potencia(a, b):
    return a ** b


def resto(a, b):
    if b == 0:
        return "Não é possível calcular o resto com divisor zero."
    return a % b


while True:
    print("\n--- CALCULADORA ---")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Resto da divisão")
    print("0 - Encerrar")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Calculadora encerrada.")
        break

    if opcao not in ["1", "2", "3", "4", "5", "6"]:
        print("Opção inválida.")
        continue

    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    if opcao == "1":
        print("Resultado:", soma(a, b))

    elif opcao == "2":
        print("Resultado:", subtracao(a, b))

    elif opcao == "3":
        print("Resultado:", multiplicacao(a, b))

    elif opcao == "4":
        print("Resultado:", divisao(a, b))

    elif opcao == "5":
        print("Resultado:", potencia(a, b))

    elif opcao == "6":
        print("Resultado:", resto(a, b))