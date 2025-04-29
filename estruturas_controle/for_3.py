produto = {'Nome': 'Caneta', 'Preço': 7.99, 'Importado': True, 'Estoque': 200}


for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)


for chave, valor in produto.items():
    print(f'{chave} = {valor}')

