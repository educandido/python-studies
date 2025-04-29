arquivo = open('pessoas.csv')
dados = arquivo.read() # Lê e armazena todo o arquivo na variável. Ex.: consome muita memória dependendo do arquivo
arquivo.close()

for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
