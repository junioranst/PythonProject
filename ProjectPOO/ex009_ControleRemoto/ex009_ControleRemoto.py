from rich import print
from rich.panel import Panel
import os

class ControleRemoto:
    def __init__(self, status = False):
        self.status = status
        self.canal_atual = 0
        self.volume_atual = 0
    def tela(self):
        if self.status == False:
            info = ':tv: [red]A TV esta desligada[/]:exclamation_mark:\n'
        else:

            canal1 = 'CANAL =   [white on yellow] 1 [/]  2   3   4   5\n'
            canal2 = 'CANAL =    1  [white on yellow] 2 [/]  3   4   5\n'
            canal3 = 'CANAL =    1   2  [white on yellow] 3 [/]  4   5\n'
            canal4 = 'CANAL =    1   2   3  [white on yellow] 4 [/]  5\n'
            canal5 = 'CANAL =    1   2   3   4  [white on yellow] 5 [/]\n'
            canais = (canal1, canal2, canal3, canal4, canal5)

            volume = 'VOLUME = [on bright_black]          [/]'
            volume1 = 'VOLUME = [on bright_black][on blue] [/]         [/]'
            volume2 = 'VOLUME = [on bright_black][on blue]   [/]       [/]'
            volume3 = 'VOLUME = [on bright_black][on blue]     [/]     [/]'
            volume4 = 'VOLUME = [on bright_black][on blue]       [/]   [/]'
            volume5 = 'VOLUME = [on bright_black][on blue]         [/] [/]'
            volume6 = 'VOLUME = [on blue]          [/]'
            volumes = (volume, volume1, volume2, volume3, volume4, volume5, volume6)

            info = (canais[self.canal_atual] + volumes[self.volume_atual])

        menu = Panel(info ,title='[ TV ]', width=40)
        print(menu)

    def liga_desliga(self):
        if self.status == False:
            self.status = True
        else:
            self.status = False


    def avancar_canal(self):
        if self.canal_atual == 4:
            self.canal_atual = 0
        else:
            self.canal_atual += 1
            return self.canal_atual

    def retroceder_canal(self):
        if self.canal_atual == 0:
            self.canal_atual = 4
        else:
            self.canal_atual -= 1
            return self.canal_atual



    def aumentar_volume(self):
        if self.volume_atual == 6:
            pass
        else:
            self.volume_atual += 1
            return self.volume_atual

    def diminuir_volume(self):
        if self.volume_atual == 0:
            pass
        else:
            self.volume_atual -= 1
            return self.volume_atual

c1 = ControleRemoto()

while True:
    os.system('cls')
    c1.tela()
    comando = (input(f'< CH {c1.canal_atual + 1} >   - VOL {c1.volume_atual} +\n' )).strip()
    match comando:
        case  0:
            break

        case '@':
            c1.liga_desliga()

        case '+':
            c1.aumentar_volume()

        case '-':
            c1.diminuir_volume()

        case '>':
            c1.avancar_canal()

        case '<':
            c1.retroceder_canal()