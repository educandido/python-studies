try:
    arquivo = open('pessoas.csv')

    # Streaming: Não carrega todo o arquivo, mas sim parte do arquivo e vai percorrendo o mesmo, fornecendo parte dos dados
    for registro in arquivo:
        # print("Nome: {}, Idade: {}".format(registro.strip().split(',')[0], registro.strip().split(',')[1]))
        print("Nome: {}, Idade: {}".format(*registro.strip().split(',')))

except SyntaxError:
    pass
except IndexError:
    pass
finally:
    print('Finally')
    arquivo.close()

if arquivo.closed:
    print("Arquivo já foi fechado")
