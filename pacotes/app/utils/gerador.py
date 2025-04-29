from random import choice

lista_nomes = ['Eduardo', 'Renata', 'Maria', 'Helio']
lista_nomes_novos = ['Alexandre', 'Alvaro', 'Aline', 'Eduardo', 'Renata']


def novo_nome():
    return choice(lista_nomes_novos)
