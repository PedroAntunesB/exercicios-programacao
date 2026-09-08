def soma_lista(lista):
    if len(lista) == 0:
        return 0

    return lista[0] + soma_lista(lista[1:])


numeros = [10, 20, 5, 3]

print("Soma:", soma_lista(numeros))