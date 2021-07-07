def decorador(func):
    def new_func():
        print('Decorators demo:')
        func()
    return new_func

@decorador
def greet():
    print(f'Hi , I am a human')

greet()


