import random

def busqueda_lineal(lista, objetivo):
    """
    Algoritmo de búsqueda lineal
    y complejidad de O(n) donde
    n = el largo de la lista

    returns True si encontró objetivo en la lista
    """
    iteraciones = 0

    encontrado = False

    for elemento in lista:
        iteraciones += 1
        if elemento == objetivo:
            encontrado = True
            break

    return (encontrado, iteraciones)

def run():
    tamano_lista = int(input('¿Qué tamaño tiene la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? ' ))

    lista = [random.randint(0,100) for i in range(tamano_lista)]

    encontrado = busqueda_lineal(lista, objetivo)

    print(lista)

    print(f'El elemento {objetivo} {"está" if encontrado[0] else "no está"} en la lista y tomó {encontrado[1]} pasos')

if __name__ == '__main__':
    run()
