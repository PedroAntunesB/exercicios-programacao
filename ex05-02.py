def fibonacci_repeticao(n):
    a = 0
    b = 1

    for i in range(n):
        a, b = b, a + b

    return a


n = int(input("Digite o valor de n: "))

print("Termo:", fibonacci_repeticao(n))

# Comparação:
# A versão recursiva é mais simples de entender, mas fica bem lenta para valores grandes de n, porque recalcula várias vezes os mesmos termos.

# A versão com repetição é mais eficiente, pois calcula cada termo apenas uma vez. Então, para valores elevados de n, é melhor usar a versão com for.