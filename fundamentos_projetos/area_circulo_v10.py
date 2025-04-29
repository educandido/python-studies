from math import pi
import sys

def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == "__main__":
    # raio = input("Informe o raio: ")
    raio = sys.argv[1]
    area = circulo(raio)
    print("Area do circulo: ", area)
