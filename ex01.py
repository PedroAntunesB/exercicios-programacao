def maior(lista):
    return max(lista)

def menor(lista):
    return min(lista)

def media(lista):
    return sum(lista) / len(lista)

def pares(lista):
    return sum(1 for numero in lista if numero % 2 == 0)

def impares(lista):
    return sum(1 for numero in lista if numero % 2 != 0)


numeros = list(map(int, input("Digite os números separados por espaço: ").split()))

while True:
    print("\n--- MENU ---")
    print("1 - Maior valor")
    print("2 - Menor valor")
    print("3 - Média")
    print("4 - Quantidade de pares")
    print("5 - Quantidade de ímpares")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Maior valor:", maior(numeros))

    elif opcao == 2:
        print("Menor valor:", menor(numeros))

    elif opcao == 3:
        print("Média:", media(numeros))

    elif opcao == 4:
        print("Quantidade de pares:", pares(numeros))

    elif opcao == 5:
        print("Quantidade de ímpares:", impares(numeros))

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")