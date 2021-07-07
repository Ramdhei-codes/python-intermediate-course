import time
import sys

def factorial_loop(n):
    respuesta = 1

    while n > 1:
        respuesta = respuesta * n
        n -= 1
    
    return respuesta

def factorial_rec(n):
    if n == 1:
        return 1
    
    return n * factorial_rec(n-1)


def run():

    sys.setrecursionlimit(1000000000)

    n = 10000

    comienzo = time.time()

    factorial_loop(n)

    print(f'Factorial del loop: {time.time() - comienzo}')

    comienzo = time.time()

    factorial_rec(n)

    print(f'Factorial recursivo: {time.time() - comienzo}')


if __name__ == '__main__':
    run()