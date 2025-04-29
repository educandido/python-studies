# 0,1,1,2,3,5,8,13,21,34...


def fibonacci(quantidade):
    resultado = [0, 1]
    for _ in range(2, quantidade): # _ pois a variável não é utilizada
        resultado.append( sum(resultado[-2:]) )

    return resultado

    
if __name__ == '__main__':
    for fib in fibonacci(5):    
        print(fib, end=',')

