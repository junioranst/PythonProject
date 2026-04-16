from rich import print
from rich.panel import Panel

class Churrasco:
    valor_carne = 82.40
    pessoa_come = 0.4
    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas

    def __str__(self):
        return f'O {self.titulo} possui {self.pessoas} pessoas'

    def consumo_total(self):
        return self.pessoas * Churrasco.pessoa_come

    def custo_total(self):
        return Churrasco.valor_carne * self.consumo_total()

    def preco_pessoa(self):
        return self.custo_total() / self.pessoas



    def analise(self):
        info = f'Analisando o [yellow]{self.titulo}[/] com [red]{self.pessoas} convidados[/]'
        info += f'\nCada participante comerá [blue]{Churrasco.pessoa_come}Kg[/] e cada Kg custa [green]R${Churrasco.valor_carne:,.2f}[/]'
        info += f'\nRecomendo comprar [blue]{self.consumo_total():.3f}Kg[/] de carne.'
        info += f'\nO custo total será de [green]R${self.custo_total():,.2f}[/]'
        info += f'\nCada pessoa pagará [green]R${self.preco_pessoa():,.2f}[/]'
        p1 =Panel(info, title= self.titulo, width=60, style='bright_white')
        return p1



c1 = Churrasco('Churras dos Amigos', 15)
c2 = Churrasco('Churras dos Inimigos', 9)
c3 = Churrasco('Churras do Adriano', 55)


print(c1.analise())
print(c2.analise())
print(c3.analise())

print(c1)
print(c2)
print(c3)
