arquivo = open('pessoas.csv')

# Streaming: Não carrega todo o arquivo, mas sim parte do arquivo e vai percorrendo o mesmo, fornecendo parte dos dados
for registro in arquivo:
    print("Nome: {}, Idade: {}".format(*registro.strip().split(',')))

arquivo.close()
