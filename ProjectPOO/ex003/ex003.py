from rich import print
from rich import inspect
class Funcionario():
    empresa = 'Passos Tech'
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentar(self, nome='', setor='', cargo=''):
        return f':handshake:Ola meu nome é [blue]{self.nome}[/], trabalho no setor de {self.setor} como {self.cargo} na empresa {Funcionario.empresa}'

    def __str__(self):
        return f'Ola meu nome é {self.nome}, trabalho no setor de {self.setor} como {self.cargo}'

c1 = Funcionario('Joao', 'Tecnologia','Programador')
c2 = Funcionario('Roberto', 'Estruturas','Mecanico')

#inspect(c1)
print(c1.apresentar())
print(c2.apresentar())