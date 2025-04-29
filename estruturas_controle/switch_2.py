def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }

    return dias.get(dia, '***Dia inválido***')


def tipo_dia(dia):
    if dia in(1, 7):
        return "Final de Semana"
    elif dia in range(2, 7):
        return "Dia Util"
    else:
        return "Dia inválido"
    
    
for dia in range(0,9):
    print(f'{dia}: {get_dia_semana(dia)} -> {tipo_dia(dia)}')
