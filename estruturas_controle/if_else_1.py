import sys


def help(msg):
    print(msg)


def conceito(nota):
    if nota > 10:
        conceito = "Nota inválida"
    elif nota >= 9.1:
        conceito = "A"
    elif nota >= 8.1:
        conceito = "A-"
    elif nota >= 7.1:
        conceito = "B"
    elif nota >= 6.1:
        conceito = "B-"
    elif nota >= 5.1:
        conceito = "C"
    elif nota >= 4.1:
        conceito = "C-"
    elif nota >= 3.1:
        conceito = "D"
    elif nota >= 2.1:
        conceito = "D-"
    elif nota >= 1.1:
        conceito = "E"
    elif nota >= 0:
        conceito = "E-"
    else:
        conceito = "Nota inválida"
    
    return conceito


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help("Deve informar a nota.")
    elif not sys.argv[1].isnumeric():
        help("A nota deve ser um número.")
        sys.exit()
    else:
        nota = float(sys.argv[1])
        print(conceito(nota))


print("Fim")
