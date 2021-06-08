import time

def square_root(num, epsilon):
    bajo = 0.0
    alto = max(1.0, num)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - num) >= epsilon:
        if respuesta**2 < num:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo)/2
    return respuesta


def run():
    objetivo = int(input('Ingresa un número: '))
    now = time.time()
    print(f'La raíz cuadrada de {objetivo} es {square_root(objetivo, 0.0001)}')
    print(f'Me demoré {time.time() - now} segs')


if __name__ == '__main__':
    run()
