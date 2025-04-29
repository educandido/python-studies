def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'

if __name__ == "__main__":
    print(tag_bloco('Texto HTML'))
    print(tag_bloco('Texto inline', inline=True))
    print(tag_bloco('Deu erro!', classe='error', inline=False))
    print(tag_bloco(classe='titulo', texto='Titulo da Noticia'))
