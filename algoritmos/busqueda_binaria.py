import random

def busqueda_binaria(lista, comienzo, final, objetivo, iters=0):
    iters += 1
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, iters)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio+1, final, objetivo, iters)
    else:
        return busqueda_binaria(lista, comienzo, medio-1, objetivo, iters)

def run():
    tamano_lista = int(input('¿Qué tamaño tiene la lista? '))
    objetivo = int(input('¿Qué número quieres encontrar? ' ))

    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)

    print(f'El elemento {objetivo} {"está" if encontrado[0] else "no está"} en la lista y tomó {encontrado[1]} pasos')

if __name__ == '__main__':
    run()