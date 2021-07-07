import random


def ordenamiento_burbuja(lista):

    n = len(lista)

    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]    
    return lista



def run():
    tamano_lista = int(input('¿Qué tamaño tiene la lista? '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)

    ordenada = ordenamiento_burbuja(lista)

    print(ordenada)

if __name__ == '__main__':
    run()