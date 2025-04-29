from math import pi

raio = input("Informe o raio: ")

area = pi * (float(raio) ** 2)
perimetro = 2 * pi * float(raio)

print(f"Área: {area}")
print(f"Perímetro: {perimetro}")

print("Nome do modulo: ", __name__)
