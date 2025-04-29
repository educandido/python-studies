
# O with fecha o arquivo implicitamente
with open('pessoas.csv') as arquivo:
   for registro in arquivo:
        # print("Nome: {}, Idade: {}".format(registro.strip().split(',')[0], registro.strip().split(',')[1]))
        print("Nome: {}, Idade: {}".format(*registro.strip().split(',')))


if arquivo.closed:
    print("Arquivo já foi fechado")
