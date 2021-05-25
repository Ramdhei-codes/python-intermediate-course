import math

def run():
    sq_roots = {i:math.sqrt(i) for i in range(0,101) if i%3 != 0}

    # for i in range(0,101):
    #     if i%3 != 0:
    #         sq_roots[i] = i**3
    
    print(sq_roots)

if __name__ == '__main__':
    run()