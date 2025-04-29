from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    
    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))


    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]


    def procurar(self, descricao):
        # Possivel IndexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]


    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


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
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa')
    casa.add('Lavar prato')
    print(casa)

    print(casa.procurar('Lavar prato'))
    casa.procurar('Lavar prato').concluir()
    print(casa.procurar('Lavar prato').feito)

    for tarefa in casa.tarefas:
        print(f'- {tarefa}')
    
    print(casa)

    print('---------------------')
    mercado = Projeto('Compras no Mercado')
    mercado.add('Frutas secas')
    mercado.add('Carne')
    mercado.add('Produtos de limpeza')
    print(mercado)
          
    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
         
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')



if __name__ == '__main__':
    main()
