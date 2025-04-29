from math import pi
import sys
import errno

class TerminalColor:
    ERRO = '\033[91m'
    NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    print("É necessário informar o raio.")
    print("Sintaxe: {} <raio>".format(sys.argv[0][2:]))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        # sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(TerminalColor.ERRO + 
              "O raio deve ser um valor numérico" + 
              TerminalColor.NORMAL)
        sys.exit(errno.EINVAL)
    else:
        raio = sys.argv[1] # [0] é o nome do arquivo. [1] é o parâmetro após o nome do arquivo
        area = circulo(raio)
        print("Area do circulo: ", area)


print("Fim")