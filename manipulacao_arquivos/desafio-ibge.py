import csv

qtd_linhas = 0

with open('desafio-ibge.csv') as entrada:
    for cidade in csv.reader(entrada):
        if qtd_linhas  > 0:
            print('Nome Dest: {}, Nome Orig: {}'.format(cidade[8], cidade[3]))

        qtd_linhas += 1


print('Quantidade de Linhas: {}'.format(qtd_linhas))


