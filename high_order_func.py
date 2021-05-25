#Import reduce
from functools import reduce

def run():

    numbers = [1,3,4,5,6,7]

    # Use of map
    squares = list(map(lambda x: x**2, numbers))
    print(squares)

    # Use of filter
    evens = list(filter(lambda x: x%2 == 0, numbers))
    print("Filtrados: ",evens)

if __name__ == '__main__':
    run()