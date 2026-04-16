from rich import print
from rich import inspect
from rich.panel import Panel

class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = f'R${preco:,.2f}'

    def etiqueta(self):
        p1 =Panel(f'{self.nome:^46} {'':-^46} {self.preco:-^46}', title=f'Produto', width=50, height=5,style='bright_white')
        return p1


p1 = Produto('Mouse', 20)
print(p1.etiqueta())

p2 = Produto('Carro Eletrico', 35)
print(p2.etiqueta())

p3 = Produto('Cubo Mágico',35.50)
print(p3.etiqueta())

p4 = Produto('Hyper X',2050.00)
print(p4.etiqueta())