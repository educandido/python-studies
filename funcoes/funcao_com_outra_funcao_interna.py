def soma(a, b):
    def soma_c(c):
        return a + b + c
    return soma_c


soma_5 = soma(2, 3)
print(soma_5(10))
print(soma(2, 3)(10))
