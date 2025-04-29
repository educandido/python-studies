def todos_params(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == '__main__':
    todos_params('a', 'b', 'c')
    todos_params(1, 2, 3, nome='Edu', idade=37)
    todos_params('Edu', (1, 2, 3), tamanho='M', fragil=False)
    todos_params(nome="Joao", sexo='M')