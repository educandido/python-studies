PALAVRAS_PROIBIDAS = ('futebol', 'política', 'religião')

textos = ['João gosta de futebol e política',
          'A praia foi divertida']


if __name__ == '__main__':
    for texto in textos:
        for palavra in texto.lower().split():
            if palavra in PALAVRAS_PROIBIDAS:
                print(f"Texto possui pelo menos uma palavra proibida: {palavra}")
                break
        else:
            print("Texto autorizado: ", texto)






