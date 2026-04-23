from importlib.metadata import pass_none
from rich import print

class Caneta:
    def __init__(self, cor):
        self.cor = cor
        self.tampa = False
    def destampar(self):
        self.tampa = True
        return

    def tampar(self):
        self.tampa = False
        return

    def escrever(self, texto):
        self.texto = texto
        if self.tampa == False:
            print(':prohibited: [bright_red]A caneta esta tampada :prohibited:[/]')
        else:
            if self.cor.lower() == 'vermelho':
                print(f'[red]{self.texto}[/]')
            elif self.cor.lower() == 'azul':
                print(f'[blue]{self.texto}[/]')
            elif self.cor.lower() == 'verde':
                print(f'[green]{self.texto}[/]')


c1 = Caneta('vermelho')
c1.destampar()
c1.escrever('cole amigo')

c2 = Caneta('azul')
c2.destampar()
c2.escrever('cole amigo como está as coisas')

c3 = Caneta('verde')
c3.destampar()
c3.escrever('cole amigo hoje vai ter jogo')

c1.tampar()
c1.escrever('cole amigo')