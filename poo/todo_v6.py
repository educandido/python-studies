from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []


    def __iter__(self):
        return self.tarefas.__iter__()
    

    # Sobrecarga do operador +=
    # Projeto += tarefa
    # casa += 'Lavar banheiro'
    def __iadd__(self, tarefa):
        tarefa.dono = self
        self._add_tarefa(tarefa)
        return self

   
    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)


    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('vencimento', None)))

    
    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)
     


    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]


    def procurar(self, descricao):
        # Possivel IndexError
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]


    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento


    def concluir(self):
        self.feito = True

    
    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)    


class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias
        self.dono = None

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias)
        nova_tarefa = TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
        if self.dono:
            self.dono += nova_tarefa
        return nova_tarefa


def main():
    casa = Projeto('Tarefas de Casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3, minutes=12))
    casa.add(TarefaRecorrente('Trocar Lencois', datetime.now(), 7))
    casa.add(casa.procurar('Trocar Lencois').concluir())

    casa += TarefaRecorrente('Lavar banheiro', datetime.now(), 10)
    casa.procurar('Lavar banheiro').concluir()

    print(casa)

    print(casa.procurar('Lavar prato'))
    casa.procurar('Lavar prato').concluir()
    print(casa.procurar('Lavar prato').feito)

    for tarefa in casa:
        print(f'- {tarefa}')
    
    print(casa)

    print('---------------------')
    mercado = Projeto('Compras no Mercado')
    mercado.add('Frutas secas', datetime.now() - timedelta(minutes=10))
    mercado.add('Carne')
    mercado.add('Produtos de limpeza', datetime.now() + timedelta(days=3, minutes=1))
    print(mercado)
          
    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
         
    for tarefa in mercado:
        print(f'- {tarefa}')



if __name__ == '__main__':
    main()
