class Data:
    # python aceita um construtor
    def __init__(self, dia=1, mes=1, ano=1970):
        self.dia = dia
        self.mes = mes
        self.ano = ano


    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(17, 2, 1987)
# d1.dia = 17
# d1.mes = 2
# d1.ano = 1987
print(d1)

d2 = Data(ano=2025)
d2.dia = 20
# d2.mes = 12
# d2.ano = 2024
print(d2)
