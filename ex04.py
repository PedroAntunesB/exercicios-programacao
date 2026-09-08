def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


numero = int(input("Digite um número inteiro não negativo: "))

if numero < 0:
    print("Digite um número não negativo.")
else:
    print("Fatorial:", fatorial(numero))

# Perguntas: 
# 1. Qual é o caso-base da função?
# É quando n é 0 ou 1. Nesse caso, a função retorna 1 e para de chamar ela mesma.

# 2. O que aconteceria se o caso-base não existisse?
# A função ficaria chamando ela mesma infinitamente até dar erro.
 
# 3. Qual seria uma versão não recursiva?
# Seria usando um for, por exemplo: