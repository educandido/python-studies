import app.utils


lista_nomes_v2 = app.utils.gerador.lista_nomes


def add_nome(nome):
    lista_nomes_v2.append(nome)
    return lista_nomes_v2
