from app.utils.gerador import lista_nomes

def nome_existe(nome):
    return True if nome in lista_nomes else False
