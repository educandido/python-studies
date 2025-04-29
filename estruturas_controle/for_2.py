palavra = 'paralelepipedo'

for letra in palavra:
    print(letra, end=',')

print('Fim')


aprovados = ['Eduardo', 'Renata', 'Maria']
for nome in aprovados:
    print(nome)


for posicao, nome in enumerate(aprovados):
    print(posicao + 1, nome)

dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta',
               'Quinta', 'Sexta', 'Sábado', 'Domingo']
for dia in dias_semana:
    print(f'Hoje é {dia}')


for letra in set('Hello World'):
    print(letra)


for numero in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
    print(numero)
