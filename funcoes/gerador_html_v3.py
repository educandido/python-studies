def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


def tag_lista(*itens):
    lista = ''.join([f'<li>{item}</li>' for item in itens])
    return f'<ul>{lista}</ul>'


if __name__ == "__main__":
    print(tag_bloco('Texto HTML'))
    print(tag_bloco('Texto inline', inline=True))
    print(tag_bloco('Deu erro!', classe='error', inline=False))
    print(tag_bloco(classe='titulo', texto='Titulo da Noticia'))

    print(tag_bloco(tag_lista('Item 1', 'Item 2'), classe='info'))
