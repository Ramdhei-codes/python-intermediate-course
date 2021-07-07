import random

def insertion_sort(lista):
    n = len(lista)

    ordenada = [lista[0]]
    
    for i in range(1, n):
        valor_actual = lista[i]
        posicion_actual = i
        
        while posicion_actual > 0 and lista[posicion_actual-1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual-1]
            posicion_actual -= 1
        lista[posicion_actual] = valor_actual




def run():
    tamano_lista = int(input('¿Qué tamaño tiene la lista? '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)

    ordenada = insertion_sort(lista)

    print(ordenada)

if __name__ == '__main__':
    run()