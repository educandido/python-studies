from math import pi
import sys
from pathlib import Path

def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessário informar o raio.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
    else:
        raio = sys.argv[1] # [0] é o nome do arquivo. [1] é o parâmetro após o nome do arquivo
        area = circulo(raio)
        print("Area do circulo: ", area)
