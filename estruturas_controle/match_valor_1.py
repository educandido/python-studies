def get_tipo_dia(dia):
    match dia:
        case 1 | 7:
            return "Final de Semana"
        case 2 | 3 | 4 | 5 | 6:
            return "Dia Util"
        case _:
            return "Dia inválido"


if __name__ == "__main__":
    for dia in range(0, 9):
        print(f'{dia} -> {get_tipo_dia(dia)}')

 