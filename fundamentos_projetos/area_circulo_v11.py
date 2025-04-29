from math import pi
import sys
from pathlib import Path

def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == "__main__":
    # raio = input("Informe o raio: ")

    if len(sys.argv) < 2:
        print("""\
              É necessário informar a área do círculo.
              Sintaxe:""", sys.argv[0] , """<raio>""")
        print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))
    else:
        raio = sys.argv[1] # [0] é o nome do arquivo. [1] é o parâmetro após o nome do arquivo
        area = circulo(raio)
        print("Area do circulo: ", area)
