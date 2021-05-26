def divisores(num):
    divs = []

    for i in range(1, num+1):
        if num % i == 0:
            divs.append(i)
    
    return divs
    

def run():
    try:
        num = input('Ingresa un número: ')
        assert num.isnumeric(), 'Ingrese in valor numérico'
        assert num > 0, 'Ingrese un numero positivo'
        print(divisores(num))
    except ValueError:
        print('Ingresa un enetero positivo')

if __name__ == '__main__':
    run()