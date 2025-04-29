def calc_preco_final(preco_bruto, calc_imposto, **params):
    return preco_bruto + preco_bruto * calc_imposto(**params)


def imposto_x(importado):
    return 0.20 if importado else 0.10


def imposto_y(explosivo, fator_mult=1):
    return 0.10 * fator_mult if explosivo else 0


if __name__ == '__main__':
    preco_bruto = 100.00
    preco_final = calc_preco_final(preco_bruto, imposto_x, importado=True)
    print(preco_final)
    preco_final = calc_preco_final(preco_final, imposto_y, 
                                   explosivo=True, fator_mult=1.5)
    print(preco_final)
