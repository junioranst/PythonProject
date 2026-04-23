from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.fav_jogos = list()
    def __str__(self):
        return f'Nome: {self.nome}, Nick: {self.nick}, Jogos Favoritos: '

    def add_favoritos(self, fav):
        self.fav_jogos.append(fav)
        self.fav_jogos = sorted(self.fav_jogos, key= str.lower)

    def ficha(self):
        info= f'Nome real: {self.nome}'
        info+= f'\nJogos favoritos:'
        for num, game in enumerate(self.fav_jogos):
            info += f'\n :video_game: {game}'

        p1 = Panel(info, title=f'Jogador <{self.nick}>', width=40)
        return p1


g1= Gamer('Marcio','Nickels')
g1.add_favoritos('call od dur')
g1.add_favoritos('Gta5')
print(g1.ficha())

