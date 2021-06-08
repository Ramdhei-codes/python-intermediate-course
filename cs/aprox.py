import time

start_time = time.time()

objetivo = int(input('Escoge un número: '))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0


while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso


if abs(respuesta**2 - objetivo) >= epsilon:
    print('No encontramos la respuesta')
else:
    print(f'La reíz cuadrada de {objetivo} es {respuesta}')

print(f'Me tardé {time.time() - start_time} segundos')