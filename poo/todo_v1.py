from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()


    def concluir(self):
        self.feito = True

    
    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')
    

def main():
    casa = []
    casa.append(Tarefa('Lavar prato'))
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Cozinhar'))
    # Desafio -> 'Lavar prato'

    
    for tarefa in casa:
        print(tarefa)
        if tarefa.descricao == 'Passar roupa':
            print('Encontrou: '+ tarefa.descricao)
            tarefa.concluir()


    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Cozinhar']


    for tarefa in casa:
        print(tarefa)


if __name__ == '__main__':
    main()
