from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, pagina):
        self.titulo = titulo
        self.pagina = pagina
        self.pag_atual = 1

        print(f':open_book: [blue]Voce abriu o livro [yellow2]{self.titulo}[/] que possui [red]{self.pagina} paginas[/] e voce esta na [orange3]pagina {self.pag_atual}[/]')

    def __str__(self):
        return (f'Livro {self.titulo}, possui {self.pagina} paginas')

    def avancar(self, proxima):
        self.proxima = proxima
        count = 0
        for pa in range(self.proxima):
            if self.pag_atual < self.pagina:
                count += 1
                sleep(0.2)
                self.pag_atual += 1
                print(f'[bright_white]Pagina {self.pag_atual} :play_button:[/]', end=' ')
                sleep(0.5)
            else:
                break
        print(f'Voce avançou [red]{count} paginas[/], e voce esta na [purple]pagina {self.pag_atual}[/]')
        if self.pag_atual == self.pagina:
            print(f':clap: [red1]Voce Terminou o Livro[/] [cyan]{self.titulo}[/]')



l1 = Livro('Rainbow Six', 20)
l1.avancar(5)
l1.avancar(8)
l1.avancar(10)


