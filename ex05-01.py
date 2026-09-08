def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


n = int(input("Digite o valor de n: "))

print("Termo:", fibonacci_recursivo(n))