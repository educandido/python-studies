class Data:
    def to_str(self): 
        # self -> objeto atual que está em execução, na chamada do método. Pode usar outro nome se quiser.
        return f'{self.dia}/{self.mes}/{self.ano}'
    

    # __str__ -> metodo padrao, nao tem necessidade de criar o to_str()
    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data()
d1.dia = 17
d1.mes = 2
d1.ano = 1987
print(d1.to_str())

d2 = Data()
d2.dia = 5
d2.mes = 12
d2.ano = 2024
print(d2)
