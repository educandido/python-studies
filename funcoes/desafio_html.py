def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop('html_class') # substitui a key html_class por class
    attrs = ' '.join(f'{k}="{v}" ' for k, v in kwargs.items())
    inner = ''.join(args)
    return f'<{tag} {attrs}>{inner}</{tag}>'


if __name__ == '__main__':
    print(  
        tag('p',
            tag('span', 'Curso de Pythonn 3, por '),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', 'e '),
            tag('strong', 'Leonardo Leitao', id='ll'),
            tag('span', '.'),
            html_class='alert')
    )
