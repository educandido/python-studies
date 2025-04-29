# 0,1,1,2,3,5,8,13,21,34...


def fibonacci(quantidade, sequencia=(0,1)):

    if len(sequencia) == quantidade:
        return sequencia
    
    sequencia += (sum(sequencia[-2:]), )
    return fibonacci(quantidade, sequencia)


    
if __name__ == '__main__':   
    for fib in fibonacci(10):
        print(fib)
