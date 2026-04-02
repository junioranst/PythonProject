import random as r

lista = []
while True:
    n1 = input('digite um nome: ').lower().strip()
    if n1 == 'fim':
        break
    lista.append(n1)

nome = r.choice(lista)
print('=-' *20)
print(f'\033[97;43m {nome} \033[m')
print('=-' *20)
