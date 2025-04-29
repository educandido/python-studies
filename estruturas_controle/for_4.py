from random import randint

"""
for x in range(1, 11):
    if x == 6:
        break
    print(x)
else:
    print('Fim!')
"""

def sortear_dado():
    return randint(1,6)

for x in range(1, 7):
    if x % 2 != 0:
        continue
    elif x == sortear_dado():
        print(f'ACERTOU! -> {x}')
        break
else:
    print('Errou o número sorteado')
