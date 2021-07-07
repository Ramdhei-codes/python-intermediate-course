import random


def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2

        izquierda = lista[:medio]

        derecha = lista[medio:]

        print(izquierda, '*' * 5, derecha)

        merge_sort(izquierda)

        merge_sort(derecha)

        #iteradores para las sublistas
        i = 0
        j = 0

        #iterador lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i+=1
            else:
                lista[k] = derecha[j]
                j+=1
            k+=1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i+=1
            k+=1

        while j < len(derecha):
            lista[k] = derecha[j]
            j+=1
            k+=1
        
        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)
    return lista


def run():
    tamano_lista = int(input('¿Qué tamaño tiene la lista? '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)

    ordenada = merge_sort(lista)

    print(ordenada)

if __name__ == '__main__':
    run()