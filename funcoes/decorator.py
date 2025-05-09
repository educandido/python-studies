def log(function):
    def decorator(*args, **kwargs):
        print(f'Inicio da chamada da funcao: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')
        resultado = function(*args, **kwargs)
        print(f'Resultado da chamada: {resultado}')
        return resultado
    return decorator

@log
def soma(a, b):
    return a + b

@log
def sub(a, b):
    return a - b


if __name__ == '__main__':
    print(soma(2, 3))
    print(sub(5, b=2))
