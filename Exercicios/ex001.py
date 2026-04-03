import random as r

lista = []
while True:
    n1 = input('Digite um nome: (fim para parar)')
    if n1 == 'fim':
        break
    lista.append(n1)

nome = r.choice(lista)

print(f'\033[30;103m{nome}\033[m')